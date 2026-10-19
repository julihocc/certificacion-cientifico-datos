"""Datos de la práctica de ventas: limpieza, modelo estrella y medidas.

La limpieza se explica paso a paso en el Módulo 44; el modelo, en el 45, y las
medidas, en el 47. Los notebooks de los módulos 45 a 50 y las apps de Streamlit
importan este archivo para no repetir esos pasos.

Uso rápido:

    import ventas
    con = ventas.conectar()          # modelo en DuckDB desde datos-modelo/*.parquet
    ventas.kpis(con, paises=["US", "CANADA"])

Ejecutar `python ventas.py` comprueba el modelo contra las cifras de referencia.
"""

from __future__ import annotations

from pathlib import Path

import duckdb
import pandas as pd

RUTA = Path(__file__).resolve().parent
DATOS = RUTA / "datos-ventas"
MODELO = RUTA / "datos-modelo"

# Cifras de referencia del extracto completo
FILAS_VENTAS = 1_499_000
VENTAS_TOTALES = 41_940_958_825

# Códigos ISO 3166-1 alfa-3 para los mapas de Plotly
ISO3 = {
    "US": "USA",
    "CANADA": "CAN",
    "MEXICO": "MEX",
    "BRAZIL": "BRA",
    "SPAIN": "ESP",
    "COLOMBIA": "COL",
    "CHILE": "CHL",
    "PERU": "PER",
    "PORTUGAL": "PRT",
    "FRANCE": "FRA",
}

NOMBRES_MES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]

COLUMNAS_VENTAS = {
    "Date": "fecha",
    "ID_Country": "id_pais",
    "ID_Store": "id_tienda",
    "ID_Client": "id_cliente",
    "ID_Product": "id_producto",
    "Quantity": "cantidad",
    "Price": "precio",
}
ORDEN_VENTAS = ["fecha", "id_pais", "id_tienda", "id_cliente", "id_producto", "cantidad", "precio", "importe"]

# Relaciones del modelo estrella: (columna de la tabla de hechos, dimensión)
RELACIONES = [
    ("id_pais", "paises"),
    ("id_tienda", "tiendas"),
    ("id_cliente", "clientes"),
    ("id_producto", "productos"),
]

# Columnas por las que se puede agrupar o filtrar en las medidas. El nombre de la
# tienda no es único (las tiendas 40 y 197 se llaman "Schumm Inc"): para agrupar
# por tienda hay que incluir id_tienda junto con tienda.
DIMENSIONES = {
    "pais", "categoria", "subcategoria", "producto", "id_tienda", "tienda", "formato",
    "anio", "trimestre", "mes", "anio_mes",
}


# ---------------------------------------------------------------------------
# Limpieza (Módulo 44)
# ---------------------------------------------------------------------------

def leer_paises() -> pd.DataFrame:
    """paises.txt: separado por |, sin encabezado y con filas repetidas."""
    paises = pd.read_csv(DATOS / "paises.txt", sep="|", header=None, names=["id_pais", "pais"])
    return paises.drop_duplicates().sort_values("id_pais", ignore_index=True)


def leer_clientes() -> pd.DataFrame:
    """Hoja t_customer: el cliente viene empaquetado en ID|658|Nombre/Apellido|mail:...|tel."""
    hoja = pd.read_excel(DATOS / "catalogo.xlsx", sheet_name="t_customer", dtype=str)
    # Filtrar por contenido elimina a la vez las filas vacías y el pie del extracto
    validas = hoja[hoja["ID_Client"].str.startswith("ID|", na=False)]
    partes = validas["ID_Client"].str.split("|", expand=True)
    nombre = partes[2].str.split("/", n=1, expand=True)
    clientes = pd.DataFrame({
        "id_cliente": partes[1].astype(int),
        "nombre": nombre[0],
        "apellido": nombre[1],
        "correo": partes[3].str.removeprefix("mail:"),
        "telefono": partes[4],
    })
    return clientes.sort_values("id_cliente", ignore_index=True)


def leer_productos() -> pd.DataFrame:
    """Hoja t_product: clave dentro de 'ID-1000|Product' y duplicados inactivos."""
    hoja = pd.read_excel(DATOS / "catalogo.xlsx", sheet_name="t_product")
    activos = hoja[hoja["Active"] == 1]
    productos = pd.DataFrame({
        "id_producto": activos["Product ID"].str.extract(r"ID-(\d+)\|", expand=False).astype(int),
        "categoria": activos["Category"],
        "subcategoria": activos["Sub-Category"],
        "producto": activos["Product Name"],
    })
    return productos.sort_values("id_producto", ignore_index=True)


def leer_tiendas() -> pd.DataFrame:
    """Hoja t_store: dos filas basura, formatos mal escritos y tiendas Open/Closed."""
    hoja = pd.read_excel(DATOS / "catalogo.xlsx", sheet_name="t_store", header=2)
    abiertas = hoja[hoja["Status"] == "Open"]
    tiendas = pd.DataFrame({
        "id_tienda": abiertas["ID_Store"].astype(int),
        "tienda": abiertas["Name_Store"],
        "direccion": abiertas["Addres"],
        # Primero recortar espacios y después pasar a mayúsculas: "   A" -> "A"
        "formato": abiertas["Format"].str.strip().str.upper(),
    })
    return tiendas.sort_values("id_tienda", ignore_index=True)


def leer_ventas() -> pd.DataFrame:
    """ventas-2019.csv más la carpeta ventas-por-anio/, en una sola tabla de hechos."""
    archivos = [DATOS / "ventas-2019.csv", *sorted((DATOS / "ventas-por-anio").glob("*.csv"))]
    # utf-8-sig quita el BOM; usecols=range(8) descarta la columna fantasma de la coma final
    partes = [pd.read_csv(archivo, encoding="utf-8-sig", usecols=range(8)) for archivo in archivos]
    ventas = pd.concat(partes, ignore_index=True)
    # ID_T no es clave: cada archivo vuelve a empezar en 1
    ventas = ventas.drop(columns="ID_T").rename(columns=COLUMNAS_VENTAS)
    ventas["fecha"] = pd.to_datetime(ventas["fecha"], format="%m/%d/%Y")
    ventas["importe"] = ventas["cantidad"] * ventas["precio"]
    return ventas[ORDEN_VENTAS]


def calendario(inicio, fin) -> pd.DataFrame:
    """Tabla de calendario continua, un día por fila (Módulo 47)."""
    fechas = pd.date_range(pd.Timestamp(inicio).normalize(), pd.Timestamp(fin).normalize(), freq="D")
    return pd.DataFrame({
        "fecha": fechas,
        "anio": fechas.year,
        "trimestre": fechas.quarter,
        "mes": fechas.month,
        "nombre_mes": [NOMBRES_MES[m - 1] for m in fechas.month],
        "anio_mes": fechas.strftime("%Y-%m"),
    })


def guardar_modelo(destino: Path = MODELO) -> dict[str, Path]:
    """Escribe el modelo limpio en Parquet: el "cerrar y aplicar" de la práctica.

    La tabla de hechos se guarda ordenada por fecha, con enteros pequeños y sin la
    columna importe, que la vista de DuckDB recalcula como cantidad * precio.
    """
    destino.mkdir(parents=True, exist_ok=True)
    hechos = leer_ventas().drop(columns="importe").sort_values(["fecha", "id_pais", "id_tienda"], kind="stable")
    hechos = hechos.astype({
        "id_pais": "int8",
        "id_tienda": "int16",
        "id_cliente": "int16",
        "id_producto": "int16",
        "cantidad": "int16",
        "precio": "int16",
    })
    hechos["fecha"] = hechos["fecha"].dt.date
    tablas = {
        "ventas": hechos,
        "paises": leer_paises(),
        "clientes": leer_clientes(),
        "productos": leer_productos(),
        "tiendas": leer_tiendas(),
    }
    rutas = {}
    for nombre, tabla in tablas.items():
        ruta = destino / f"{nombre}.parquet"
        tabla.to_parquet(ruta, index=False, compression="zstd")
        rutas[nombre] = ruta
    return rutas


# ---------------------------------------------------------------------------
# Modelo en DuckDB (Módulo 45)
# ---------------------------------------------------------------------------

def conectar(origen: str = "parquet") -> duckdb.DuckDBPyConnection:
    """Abre una base DuckDB en memoria con el modelo estrella.

    origen="parquet" lee datos-modelo/ (rápido; lo usan las apps).
    origen="csv" limpia los archivos originales con las funciones leer_*.

    Crea las tablas ventas, paises, clientes, productos, tiendas y calendario, y la
    vista ventas_detalle, que une la tabla de hechos con sus dimensiones.
    """
    con = duckdb.connect()
    if origen == "parquet":
        for nombre in ("paises", "clientes", "productos", "tiendas"):
            ruta = (MODELO / f"{nombre}.parquet").as_posix()
            con.execute(f"CREATE VIEW {nombre} AS SELECT * FROM read_parquet('{ruta}')")
        ruta = (MODELO / "ventas.parquet").as_posix()
        con.execute(
            "CREATE VIEW ventas AS "
            "SELECT *, CAST(cantidad AS BIGINT) * precio AS importe "
            f"FROM read_parquet('{ruta}')"
        )
    elif origen == "csv":
        tablas = {
            "ventas": leer_ventas(),
            "paises": leer_paises(),
            "clientes": leer_clientes(),
            "productos": leer_productos(),
            "tiendas": leer_tiendas(),
        }
        for nombre, tabla in tablas.items():
            con.register("tmp", tabla)
            con.execute(f"CREATE TABLE {nombre} AS SELECT * FROM tmp")
            con.unregister("tmp")
        con.execute("ALTER TABLE ventas ALTER fecha TYPE DATE")
    else:
        raise ValueError(f"origen debe ser 'parquet' o 'csv', no {origen!r}")

    inicio, fin = con.execute("SELECT min(fecha), max(fecha) FROM ventas").fetchone()
    # Años completos, como CALENDARAUTO en Power BI
    con.register("tmp", calendario(f"{inicio.year}-01-01", f"{fin.year}-12-31"))
    con.execute("CREATE TABLE calendario AS SELECT * EXCLUDE (fecha), CAST(fecha AS DATE) AS fecha FROM tmp")
    con.unregister("tmp")

    con.execute("""
        CREATE VIEW ventas_detalle AS
        SELECT v.*, p.pais, pr.categoria, pr.subcategoria, pr.producto, t.tienda, t.formato,
               year(v.fecha) AS anio, quarter(v.fecha) AS trimestre, month(v.fecha) AS mes,
               strftime(v.fecha, '%Y-%m') AS anio_mes
        FROM ventas v
        JOIN paises p USING (id_pais)
        JOIN productos pr USING (id_producto)
        JOIN tiendas t USING (id_tienda)
    """)
    return con


def validar_modelo(con: duckdb.DuckDBPyConnection) -> pd.DataFrame:
    """Revisa cada relación de la tabla de hechos con su dimensión.

    Una relación sana es 1:* (clave única en la dimensión) y no tiene ventas
    huérfanas (claves de la tabla de hechos que no existen en la dimensión).
    """
    filas = []
    for clave, dimension in RELACIONES:
        filas_dim, distintas = _cursor(con).execute(
            f"SELECT count(*), count(DISTINCT {clave}) FROM {dimension}"
        ).fetchone()
        huerfanas = _cursor(con).execute(
            f"SELECT count(*) FROM ventas v ANTI JOIN {dimension} d USING ({clave})"
        ).fetchone()[0]
        sin_ventas = _cursor(con).execute(
            f"SELECT count(*) FROM {dimension} d ANTI JOIN ventas v USING ({clave})"
        ).fetchone()[0]
        filas.append({
            "relacion": f"{dimension}[{clave}] -> ventas[{clave}]",
            "filas_dimension": filas_dim,
            "claves_distintas": distintas,
            "cardinalidad": "1:*" if filas_dim == distintas else "*:*",
            "ventas_huerfanas": huerfanas,
            "claves_sin_ventas": sin_ventas,
        })
    return pd.DataFrame(filas)


# ---------------------------------------------------------------------------
# Medidas (Módulos 46 a 48)
# ---------------------------------------------------------------------------

def _cursor(con: duckdb.DuckDBPyConnection) -> duckdb.DuckDBPyConnection:
    # Un cursor por consulta permite compartir la conexión entre hilos (Streamlit)
    return con.cursor()


def _consulta(con, sql: str, params: list | None = None) -> pd.DataFrame:
    return _cursor(con).execute(sql, params or []).df()


def filtro_sql(paises=None, desde=None, hasta=None, categorias=None) -> tuple[str, list]:
    """Traduce los filtros a una cláusula WHERE con parámetros.

    None significa "sin filtro"; una lista vacía no deja pasar ninguna fila, que
    es lo correcto cuando la seguridad por filas no asigna países a un usuario.
    """
    condiciones, params = [], []
    if paises is not None:
        condiciones.append("list_contains(?, pais)")
        params.append(list(paises))
    if categorias is not None:
        condiciones.append("list_contains(?, categoria)")
        params.append(list(categorias))
    if desde is not None:
        condiciones.append("fecha >= ?")
        params.append(pd.Timestamp(desde).date())
    if hasta is not None:
        condiciones.append("fecha <= ?")
        params.append(pd.Timestamp(hasta).date())
    where = ("WHERE " + " AND ".join(condiciones)) if condiciones else ""
    return where, params


def _columnas(columnas) -> list[str]:
    columnas = [columnas] if isinstance(columnas, str) else list(columnas)
    desconocidas = set(columnas) - DIMENSIONES
    if desconocidas:
        raise ValueError(f"Columnas no válidas: {sorted(desconocidas)}; usa {sorted(DIMENSIONES)}")
    return columnas


def kpis(con, **filtros) -> dict:
    """Tarjetas del tablero: totales, mediana de precio y venta promedio."""
    where, params = filtro_sql(**filtros)
    cursor = _cursor(con).execute(f"""
        SELECT CAST(coalesce(sum(importe), 0) AS BIGINT) AS ventas_total,
               CAST(coalesce(sum(cantidad), 0) AS BIGINT) AS cantidad_total,
               median(precio) AS precio_mediana,
               avg(importe) AS ventas_promedio,
               count(*) AS transacciones
        FROM ventas_detalle {where}
    """, params)
    nombres = [columna[0] for columna in cursor.description]
    return dict(zip(nombres, cursor.fetchone()))


def ventas_por(con, columnas, **filtros) -> pd.DataFrame:
    """Ventas agregadas por una o varias columnas de las dimensiones."""
    columnas = _columnas(columnas)
    grupo = ", ".join(columnas)
    where, params = filtro_sql(**filtros)
    return _consulta(con, f"""
        SELECT {grupo},
               CAST(sum(importe) AS BIGINT) AS ventas_total,
               CAST(sum(cantidad) AS BIGINT) AS cantidad_total,
               avg(importe) AS ventas_promedio,
               median(importe) AS ventas_mediana,
               count(*) AS transacciones
        FROM ventas_detalle {where}
        GROUP BY {grupo}
        ORDER BY ventas_total DESC
    """, params)


def tabla_por_pais(con, **filtros) -> pd.DataFrame:
    """Tabla del Módulo 46: mediana y total de ventas, y % de la cantidad total."""
    tabla = ventas_por(con, "pais", **filtros)
    tabla["pct_cantidad"] = tabla["cantidad_total"] / tabla["cantidad_total"].sum()
    tabla["iso3"] = tabla["pais"].map(ISO3)
    return tabla[["pais", "iso3", "ventas_mediana", "ventas_total", "cantidad_total", "pct_cantidad", "ventas_promedio"]]


def serie_temporal(con, nivel: str = "month", **filtros) -> pd.DataFrame:
    """Ventas por día, semana, mes, trimestre o año (nivel de date_trunc)."""
    if nivel not in {"day", "week", "month", "quarter", "year"}:
        raise ValueError("nivel debe ser day, week, month, quarter o year")
    where, params = filtro_sql(**filtros)
    return _consulta(con, f"""
        SELECT CAST(date_trunc('{nivel}', fecha) AS DATE) AS periodo,
               CAST(sum(importe) AS BIGINT) AS ventas_total,
               CAST(sum(cantidad) AS BIGINT) AS cantidad_total
        FROM ventas_detalle {where}
        GROUP BY periodo
        ORDER BY periodo
    """, params)


def ventas_mensuales(con, por: str | None = None, desde=None, hasta=None, **filtros) -> pd.DataFrame:
    """Medidas de inteligencia de tiempo por mes (Módulo 47).

    Para cada mes del calendario (y, si se indica, cada valor de `por`):
    ventas, mes anterior, mismo mes del año anterior, acumulado del año (YTD),
    diferencia mensual y variaciones.

    Los meses salen del calendario, no de las ventas: un mes sin ventas sigue
    ocupando su lugar y el "mes anterior" no se desplaza. Como en DAX, el filtro de
    fechas se aplica al final, así que el mes anterior al primero del rango sí se ve.
    """
    grupo = _columnas(por) if por else []
    por_sql = ", ".join(grupo)
    where, params = filtro_sql(**filtros)
    particion = f"PARTITION BY {por_sql}" if grupo else ""
    particion_anio = f"PARTITION BY {por_sql + ', ' if grupo else ''}m.anio"
    grupos = f"(SELECT DISTINCT {por_sql} FROM ventas_detalle {where})" if grupo else "(SELECT 1 AS _uno)"
    union = f"USING (anio, mes{', ' + por_sql if grupo else ''})"
    sql = f"""
        WITH meses AS (
            SELECT DISTINCT anio, mes, anio_mes, nombre_mes FROM calendario
        ),
        rejilla AS (
            SELECT * FROM meses CROSS JOIN {grupos}
        ),
        base AS (
            SELECT {por_sql + ',' if grupo else ''} anio, mes,
                   CAST(sum(importe) AS BIGINT) AS ventas, avg(importe) AS ventas_promedio
            FROM ventas_detalle {where}
            GROUP BY ALL
        )
        SELECT {''.join(f'm.{c}, ' for c in grupo)} m.anio, m.mes, m.anio_mes, m.nombre_mes,
               b.ventas, b.ventas_promedio,
               lag(b.ventas) OVER (w) AS ventas_mes_anterior,
               lag(b.ventas, 12) OVER (w) AS ventas_mismo_mes_anio_anterior,
               sum(b.ventas) OVER ({particion_anio} ORDER BY m.mes) AS ventas_ytd
        FROM rejilla m LEFT JOIN base b {union}
        WINDOW w AS ({particion} ORDER BY m.anio, m.mes)
        ORDER BY {''.join(f'm.{c}, ' for c in grupo)} m.anio, m.mes
    """
    # Con agrupación, los filtros aparecen dos veces: en la rejilla y en la base
    tabla = _consulta(con, sql, params * 2 if grupo else params)
    tabla = tabla.drop(columns="_uno", errors="ignore")
    # Medidas como float64: los meses sin dato quedan en NaN (el "blanco" de DAX)
    medidas = ["ventas", "ventas_promedio", "ventas_mes_anterior", "ventas_mismo_mes_anio_anterior", "ventas_ytd"]
    tabla[medidas] = tabla[medidas].astype("float64")
    tabla["dif_mensual"] = tabla["ventas"] - tabla["ventas_mes_anterior"]
    tabla["var_mensual"] = tabla["dif_mensual"] / tabla["ventas_mes_anterior"].where(tabla["ventas_mes_anterior"] != 0)
    tabla["var_anual"] = (tabla["ventas"] - tabla["ventas_mismo_mes_anio_anterior"]) / tabla[
        "ventas_mismo_mes_anio_anterior"
    ].where(tabla["ventas_mismo_mes_anio_anterior"] != 0)
    # El filtro de fechas va al final, sobre meses completos
    primer_dia = pd.to_datetime(tabla["anio_mes"] + "-01")
    dentro = pd.Series(True, index=tabla.index)
    if desde is not None:
        dentro &= primer_dia >= pd.Timestamp(desde).to_period("M").to_timestamp()
    if hasta is not None:
        dentro &= primer_dia <= pd.Timestamp(hasta).to_period("M").to_timestamp()
    return tabla[dentro].reset_index(drop=True)


# ---------------------------------------------------------------------------
# Autoverificación
# ---------------------------------------------------------------------------

def _verificar(origen: str) -> None:
    con = conectar(origen)
    filas, total = con.execute("SELECT count(*), CAST(sum(importe) AS BIGINT) FROM ventas_detalle").fetchone()
    print(f"[{origen}] filas de ventas: {filas:,} | ventas totales: {total:,}".replace(",", " "))
    assert filas == FILAS_VENTAS, filas
    assert total == VENTAS_TOTALES, total
    modelo = validar_modelo(con)
    assert (modelo["cardinalidad"] == "1:*").all() and (modelo["ventas_huerfanas"] == 0).all(), modelo
    print(modelo.to_string(index=False))


if __name__ == "__main__":
    _verificar("csv")
    if (MODELO / "ventas.parquet").exists():
        _verificar("parquet")
    print("Modelo correcto.")

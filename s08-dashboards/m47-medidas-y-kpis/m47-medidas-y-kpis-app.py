"""Módulo 47: medidas y KPIs de ventas.

Barra lateral con filtro de países y de meses; pestaña "Resumen" con las tarjetas
de KPIs y la línea mensual frente al año anterior, y pestaña "Validación de
medidas" con la tabla por país y mes, un mapa y la comparación de ventas con y sin
impuestos.

Se lanza desde la raíz del repositorio:

    uv run streamlit run s08-dashboards/m47-medidas-y-kpis/m47-medidas-y-kpis-app.py
"""

import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "practica-ventas"))
import ventas as practica  # noqa: E402

st.set_page_config(page_title="Medidas y KPIs", page_icon=":material/functions:", layout="wide")

IMPUESTO = 0.20  # ventas_con_impuestos = importe * 1.20
DESCUENTO = 0.10  # precio_con_descuento = precio * 0.90


# --- 1. Conexión y consultas en caché ---------------------------------------
@st.cache_resource
def conexion():
    # Una sola conexión DuckDB para todas las sesiones; las columnas calculadas
    # se definen una vez, como una vista sobre ventas_detalle
    con = practica.conectar()
    con.execute(f"""
        CREATE VIEW ventas_calculadas AS
        SELECT *,
               importe * {1 + IMPUESTO} AS ventas_con_impuestos,
               precio * {1 - DESCUENTO} AS precio_con_descuento
        FROM ventas_detalle
    """)
    return con


@st.cache_data(show_spinner=False)
def opciones():
    con = conexion()
    paises = practica.ventas_por(con, "pais")["pais"].tolist()  # de mayor a menor venta
    meses = con.execute("SELECT DISTINCT anio_mes FROM calendario ORDER BY anio_mes").df()["anio_mes"].tolist()
    return paises, meses


# Los filtros llegan como un diccionario de tuplas y fechas: es hashable para la caché
@st.cache_data(max_entries=200, show_spinner=False)
def kpis(filtros: dict) -> dict:
    return practica.kpis(conexion(), **filtros)


@st.cache_data(max_entries=200, show_spinner=False)
def mensuales(filtros: dict, por: str | None = None) -> pd.DataFrame:
    # ventas_mensuales aplica el filtro de fechas al final: el primer mes del
    # rango conserva su mes anterior y su mismo mes del año anterior
    return practica.ventas_mensuales(conexion(), por=por, **filtros)


@st.cache_data(max_entries=200, show_spinner=False)
def por_pais(filtros: dict) -> pd.DataFrame:
    return practica.tabla_por_pais(conexion(), **filtros)


@st.cache_data(max_entries=200, show_spinner=False)
def con_impuestos(filtros: dict) -> pd.DataFrame:
    where, params = practica.filtro_sql(**filtros)
    return conexion().cursor().execute(f"""
        SELECT pais,
               CAST(sum(importe) AS DOUBLE) AS ventas,
               CAST(sum(ventas_con_impuestos) AS DOUBLE) AS ventas_con_impuestos
        FROM ventas_calculadas {where}
        GROUP BY pais
        ORDER BY ventas DESC
    """, params).df()


# --- 2. Formato --------------------------------------------------------------
def numero(valor, decimales=0) -> str:
    # Separador de miles con espacio, como en el resto de la sección
    if valor is None or pd.isna(valor):
        return "—"
    return f"{valor:,.{decimales}f}".replace(",", " ")


def nombre_mes(anio_mes: str) -> str:
    anio, mes = anio_mes.split("-")
    return f"{practica.NOMBRES_MES[int(mes) - 1]} {anio}"


# --- 3. Barra lateral: el contexto de filtro ---------------------------------
paises_disponibles, meses_disponibles = opciones()

with st.sidebar:
    st.header("Filtros")
    paises = st.multiselect("Países", paises_disponibles, default=paises_disponibles, key="paises")
    mes_inicio, mes_fin = st.select_slider(
        "Meses",
        options=meses_disponibles,
        value=(meses_disponibles[0], meses_disponibles[-1]),
        key="meses",
    )
    st.caption("Las medidas de tiempo trabajan con meses completos del calendario.")

if not paises:
    st.warning("Elige al menos un país en la barra lateral.", title="Sin países")
    st.stop()

desde = pd.Timestamp(f"{mes_inicio}-01").date()
hasta = (pd.Timestamp(f"{mes_fin}-01") + pd.offsets.MonthEnd(0)).date()
filtros = {"paises": tuple(paises), "desde": desde, "hasta": hasta}

st.title("Medidas y KPIs de ventas")
st.caption(
    f"{len(paises)} de {len(paises_disponibles)} países · "
    f"de {nombre_mes(mes_inicio)} a {nombre_mes(mes_fin)}"
)

resumen, validacion = st.tabs(["Resumen", "Validación de medidas"])

# --- 4. Resumen --------------------------------------------------------------
with resumen:
    totales = kpis(filtros)
    serie = mensuales(filtros)
    ultimo = serie.dropna(subset=["ventas"]).iloc[-1]

    col1, col2, col3 = st.columns(3)
    col1.metric("Ventas totales", numero(totales["ventas_total"]), border=True, height="stretch")
    col2.metric("Venta promedio", numero(totales["ventas_promedio"], 2), border=True, height="stretch",
                help="Promedio del importe por transacción: sum(importe) / count(*).")
    # Mes contra mes: el delta es la variación frente al mes anterior (si existe)
    delta = None if pd.isna(ultimo["var_mensual"]) else f"{ultimo['var_mensual']:+.1%}"
    col3.metric(f"Ventas de {nombre_mes(ultimo['anio_mes'])}", numero(ultimo["ventas"]), delta,
                delta_description="frente al mes anterior" if delta else None,
                border=True, height="stretch")

    with st.container(border=True):
        st.subheader("Ventas mensuales frente al año anterior")
        largo = serie.melt(
            id_vars="anio_mes",
            value_vars=["ventas", "ventas_mismo_mes_anio_anterior"],
            var_name="medida",
            value_name="importe",
        ).replace({"medida": {"ventas": "Ventas", "ventas_mismo_mes_anio_anterior": "Mismo mes del año anterior"}})
        figura = px.line(
            largo, x="anio_mes", y="importe", color="medida", markers=True,
            labels={"anio_mes": "Mes", "importe": "Ventas", "medida": ""},
        )
        figura.update_layout(legend={"orientation": "h", "y": 1.1}, hovermode="x unified")
        st.plotly_chart(figura, alt="Línea de ventas mensuales con la línea del mismo mes del año anterior")

# --- 5. Validación de medidas ------------------------------------------------
with validacion:
    tabla = mensuales(filtros, por="pais")
    columnas = ["pais", "anio", "mes", "ventas", "ventas_promedio", "ventas_mes_anterior",
                "ventas_mismo_mes_anio_anterior", "ventas_ytd", "dif_mensual"]
    tabla = tabla[columnas].round({"ventas_promedio": 2})

    with st.container(border=True):
        st.subheader("Medidas por país, año y mes")
        st.caption("El mes anterior de una fila es el valor de ventas de la fila de arriba; "
                   "el acumulado del año se reinicia en enero.")
        st.dataframe(
            tabla,
            hide_index=True,
            column_config={
                "pais": "País",
                "anio": st.column_config.NumberColumn("Año", format="%d"),
                "mes": st.column_config.NumberColumn("Mes", format="%d"),
                "ventas": st.column_config.NumberColumn("Ventas", format="localized"),
                "ventas_promedio": st.column_config.NumberColumn("Venta promedio", format="localized"),
                "ventas_mes_anterior": st.column_config.NumberColumn("Mes anterior", format="localized"),
                "ventas_mismo_mes_anio_anterior": st.column_config.NumberColumn(
                    "Mismo mes del año anterior", format="localized"),
                "ventas_ytd": st.column_config.NumberColumn("Acumulado del año", format="localized"),
                "dif_mensual": st.column_config.NumberColumn("Diferencia mensual", format="localized"),
            },
            alt="Tabla de medidas por país, año y mes",
        )
        st.download_button(
            "Descargar CSV",
            tabla.to_csv(index=False).encode("utf-8"),
            file_name="validacion-medidas.csv",
            mime="text/csv",
            icon=":material/download:",
        )

    col_mapa, col_barras = st.columns(2)
    with col_mapa, st.container(border=True):
        st.subheader("Venta promedio por país")
        paises_tabla = por_pais(filtros)
        mapa = px.scatter_geo(
            paises_tabla,
            locations="iso3",
            size="ventas_promedio",
            hover_name="pais",
            hover_data={"iso3": False, "ventas_promedio": ":,.2f", "ventas_total": ":,.0f"},
            labels={"ventas_promedio": "Venta promedio", "ventas_total": "Ventas totales"},
            projection="natural earth",
        )
        mapa.update_layout(margin={"l": 0, "r": 0, "t": 0, "b": 0})
        st.plotly_chart(mapa, alt="Mapa de burbujas con la venta promedio de cada país")

    with col_barras, st.container(border=True):
        st.subheader("Ventas con y sin impuestos")
        barras = con_impuestos(filtros).melt(id_vars="pais", var_name="medida", value_name="importe")
        barras["medida"] = barras["medida"].map({"ventas": "Ventas",
                                                 "ventas_con_impuestos": "Ventas con impuestos (+20 %)"})
        figura = px.bar(
            barras, x="pais", y="importe", color="medida", barmode="group",
            labels={"pais": "País", "importe": "Importe", "medida": ""},
        )
        figura.update_layout(legend={"orientation": "h", "y": 1.1})
        st.plotly_chart(figura, alt="Barras agrupadas de ventas y ventas con impuestos por país")

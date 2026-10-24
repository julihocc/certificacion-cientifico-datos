"""Módulo 48: tablero de ventas interactivo.

Filtros en la barra lateral, título dinámico, KPIs, filtro cruzado desde el
gráfico de países, treemap con exploración en profundidad, serie temporal con
selector de nivel, tabla con minigráficos y un diálogo de detalle por país.

Se lanza desde la raíz del repositorio:

    uv run streamlit run s08-dashboards/m48-interactividad/m48-interactividad-app.py
"""

import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "practica-ventas"))
import ventas as practica  # noqa: E402

st.set_page_config(page_title="Ventas interactivas", page_icon=":material/touch_app:", layout="wide")


# --- 1. Conexión y consultas en caché ---------------------------------------
@st.cache_resource
def conexion():
    # Una sola conexión DuckDB para todas las sesiones y todas las ejecuciones
    return practica.conectar()


@st.cache_data(show_spinner=False)
def opciones():
    con = conexion()
    paises = practica.ventas_por(con, "pais")["pais"].tolist()  # de mayor a menor venta
    categorias = sorted(practica.ventas_por(con, "categoria")["categoria"])
    inicio, fin = con.execute("SELECT min(fecha), max(fecha) FROM ventas").fetchone()
    return paises, categorias, inicio, fin


# Los filtros llegan como un diccionario de tuplas y fechas: es hashable para la caché
@st.cache_data(max_entries=200, show_spinner=False)
def kpis(filtros: dict) -> dict:
    return practica.kpis(conexion(), **filtros)


@st.cache_data(max_entries=200, show_spinner=False)
def ventas_por(columnas: tuple, filtros: dict) -> pd.DataFrame:
    return practica.ventas_por(conexion(), list(columnas), **filtros)


@st.cache_data(max_entries=200, show_spinner=False)
def serie(nivel: str, filtros: dict) -> pd.DataFrame:
    return practica.serie_temporal(conexion(), nivel, **filtros)


@st.cache_data(max_entries=200, show_spinner=False)
def tabla_con_minigrafico(filtros: dict) -> pd.DataFrame:
    tabla = practica.tabla_por_pais(conexion(), **filtros)
    mensual = practica.ventas_por(conexion(), ["pais", "anio_mes"], **filtros).sort_values("anio_mes")
    # Una lista de cantidades mensuales por país: la celda que dibuja LineChartColumn
    tendencia = mensual.groupby("pais")["cantidad_total"].agg(list).rename("cantidad_mensual")
    return tabla.merge(tendencia, on="pais")


# --- 2. Funciones puras: selección y título ----------------------------------
def pais_del_punto(punto: dict) -> str:
    # custom_data[0] es el país; en barras horizontales también está en "y"
    datos = punto.get("customdata")
    return datos[0] if datos else punto.get("y")


def paises_de_seleccion(seleccion, disponibles: list[str]) -> list[str] | None:
    """Países seleccionados en el gráfico, en el orden de `disponibles`.

    Devuelve None si no hay selección (sin filtro cruzado). Los países que ya no
    están entre los disponibles (porque cambió la barra lateral) se descartan.
    """
    puntos = (seleccion or {}).get("points", [])
    elegidos = {pais_del_punto(punto) for punto in puntos}
    paises = [pais for pais in disponibles if pais in elegidos]
    return paises or None


def lista_legible(elegidos, todos, todos_texto: str, unidad: str, maximo: int = 3) -> str:
    """"todos los países", "US y CANADA" o "5 países", según cuántos haya."""
    elegidos = list(elegidos)
    if set(elegidos) == set(todos):
        return todos_texto
    if len(elegidos) > maximo:
        return f"{len(elegidos)} {unidad}"
    if len(elegidos) == 1:
        return elegidos[0]
    return ", ".join(elegidos[:-1]) + " y " + elegidos[-1]


def titulo_dinamico(paises, todos_paises, categorias, todas_categorias, desde, hasta) -> str:
    return (
        f"Ventas de {lista_legible(paises, todos_paises, 'todos los países', 'países')}"
        f" · {lista_legible(categorias, todas_categorias, 'todas las categorías', 'categorías')}"
        f" · del {desde:%d/%m/%Y} al {hasta:%d/%m/%Y}"
    )


def millones(valor) -> str:
    return f"{valor / 1e6:,.1f} M".replace(",", " ").replace(".", ",")


def entero(valor) -> str:
    return f"{valor:,.0f}".replace(",", " ")


# --- 3. Barra lateral: filtros -----------------------------------------------
PAISES, CATEGORIAS, INICIO, FIN = opciones()


def restablecer():
    # Un callback se ejecuta antes que el script: aquí sí se puede cambiar el estado de los widgets
    st.session_state["paises"] = PAISES
    st.session_state["categorias"] = CATEGORIAS
    st.session_state["fechas"] = (INICIO, FIN)
    st.query_params.pop("detalle", None)


# Estado inicial de los filtros, en un solo lugar y antes de crear los widgets
st.session_state.setdefault("paises", PAISES)
st.session_state.setdefault("categorias", CATEGORIAS)
st.session_state.setdefault("fechas", (INICIO, FIN))

with st.sidebar:
    st.header("Filtros")
    # Con el valor en session_state no hace falta default=: el widget lo toma de su key
    paises = st.multiselect("Países", PAISES, key="paises")
    categorias = st.pills("Categorías", CATEGORIAS, selection_mode="multi", key="categorias")
    desde, hasta = st.slider("Rango de fechas", min_value=INICIO, max_value=FIN, format="DD/MM/YYYY", key="fechas")
    st.button("Restablecer filtros", icon=":material/restart_alt:", on_click=restablecer, width="stretch")

if not paises or not categorias:
    st.warning("Elige al menos un país y una categoría en la barra lateral.", icon=":material/filter_alt_off:")
    st.stop()

# Filtros de la barra lateral: llegan a todos los elementos de la página
filtros = {"paises": tuple(paises), "categorias": tuple(categorias), "desde": desde, "hasta": hasta}

# Reservamos el sitio del título y los KPIs: se rellenan cuando se conoce la selección del gráfico
cabecera = st.container()


# --- 4. Filtro cruzado: gráfico de países seleccionable ----------------------
def al_seleccionar():
    # Si se selecciona un solo país, se abre su detalle (y queda en la URL)
    seleccion = st.session_state["grafico_paises"]["selection"]
    elegidos = paises_de_seleccion(seleccion, PAISES)
    if elegidos and len(elegidos) == 1:
        st.query_params["detalle"] = elegidos[0]


columna_paises, columna_productos = st.columns([2, 3])

with columna_paises.container(border=True):
    st.subheader("Ventas por país")
    por_pais = ventas_por(("pais",), filtros).sort_values("ventas_total")
    figura = px.bar(
        por_pais,
        x="ventas_total",
        y="pais",
        orientation="h",
        custom_data=["pais", "ventas_promedio", "transacciones", "cantidad_total"],
        labels={"ventas_total": "Ventas", "pais": ""},
    )
    figura.update_traces(
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "Ventas: %{x:,.0f}<br>"
            "Venta promedio: %{customdata[1]:,.0f}<br>"
            "Transacciones: %{customdata[2]:,}<br>"
            "Unidades: %{customdata[3]:,}<extra></extra>"
        )
    )
    figura.update_layout(height=380, margin=dict(l=0, r=10, t=10, b=0), separators=", ")
    evento = st.plotly_chart(
        figura,
        key="grafico_paises",
        on_select=al_seleccionar,
        selection_mode=("points", "box"),
        alt="Ventas totales por país; seleccionar barras filtra el resto del tablero",
    )
    st.caption("Haz clic en una barra (Mayús + clic para varias) para filtrar el tablero; doble clic para quitar la selección.")

seleccion = paises_de_seleccion(evento.selection, paises)
# Filtro cruzado: la selección del gráfico se suma a los filtros de la barra lateral
filtros_cruzados = {**filtros, "paises": tuple(seleccion)} if seleccion else filtros


# --- 5. Jerarquía: treemap categoría → subcategoría → producto ---------------
with columna_productos.container(border=True):
    st.subheader("Ventas por categoría, subcategoría y producto")
    jerarquia = ventas_por(("categoria", "subcategoria", "producto"), filtros_cruzados)
    treemap = px.treemap(
        jerarquia,
        path=[px.Constant("Todas"), "categoria", "subcategoria", "producto"],
        values="ventas_total",
        maxdepth=3,  # se ven dos niveles; un clic en una subcategoría baja a sus productos
    )
    treemap.update_traces(
        hovertemplate="<b>%{label}</b><br>Ventas: %{value:,.0f}<br>%{percentRoot:.1%} del total<extra></extra>",
        root_color="lightgrey",
    )
    treemap.update_layout(height=380, margin=dict(l=0, r=0, t=10, b=0), separators=", ")
    st.plotly_chart(treemap, alt="Treemap de ventas por categoría y subcategoría; clic para bajar a productos")
    st.caption("Clic en un rectángulo para bajar un nivel; clic en la barra superior para subir.")


# --- 6. Serie temporal con selector de nivel ---------------------------------
NIVELES = {"month": "Mes", "quarter": "Trimestre", "year": "Año"}

with st.container(border=True):
    st.subheader("Evolución de las ventas")
    nivel = st.segmented_control(
        "Nivel de la fecha", list(NIVELES), format_func=NIVELES.get, default="month", required=True, key="nivel"
    )
    evolucion = serie(nivel, filtros_cruzados)
    linea = px.line(evolucion, x="periodo", y="ventas_total", markers=True, labels={"periodo": "", "ventas_total": "Ventas"})
    linea.update_traces(hovertemplate="%{x|%b %Y}<br>Ventas: %{y:,.0f}<extra></extra>")
    linea.update_layout(height=320, margin=dict(l=0, r=0, t=10, b=0), separators=", ")
    st.plotly_chart(linea, alt=f"Ventas por {NIVELES[nivel].lower()} con los filtros activos")


# --- 7. Tabla por país con minigráfico ---------------------------------------
with st.container(border=True):
    st.subheader("Resumen por país")
    tabla = tabla_con_minigrafico(filtros_cruzados)
    st.dataframe(
        tabla,
        hide_index=True,
        column_order=["pais", "ventas_total", "ventas_promedio", "pct_cantidad", "cantidad_mensual"],
        column_config={
            "pais": st.column_config.TextColumn("País", pinned=True),
            "ventas_total": st.column_config.NumberColumn("Ventas", format="localized"),
            "ventas_promedio": st.column_config.NumberColumn("Venta promedio", format="%.0f"),
            "pct_cantidad": st.column_config.NumberColumn("% de unidades", format="percent"),
            "cantidad_mensual": st.column_config.LineChartColumn(
                "Unidades por mes", width="medium", help="Suma de unidades vendidas en cada mes del rango"
            ),
        },
        alt="Ventas, venta promedio, porcentaje de unidades y tendencia mensual por país",
    )


# --- 8. Diálogo de detalle por país (obtener detalles) -----------------------
def cerrar_detalle():
    st.query_params.pop("detalle", None)


@st.dialog("Detalle del país", width="large", on_dismiss=cerrar_detalle)
def detalle_pais(pais: str, filtros: dict):
    # Mantiene categorías y fechas de la barra lateral; solo cambia el país
    filtros_pais = {**filtros, "paises": (pais,)}
    st.subheader(f"{pais}: productos más vendidos")
    st.caption(
        f"{lista_legible(filtros['categorias'], CATEGORIAS, 'Todas las categorías', 'categorías')}"
        f" · del {filtros['desde']:%d/%m/%Y} al {filtros['hasta']:%d/%m/%Y}"
    )
    resumen = kpis(filtros_pais)
    with st.container(horizontal=True):
        st.metric("Ventas", millones(resumen["ventas_total"]), border=True)
        st.metric("Unidades", entero(resumen["cantidad_total"]), border=True)
        st.metric("Venta promedio", entero(resumen["ventas_promedio"]), border=True)
    top = ventas_por(("categoria", "subcategoria", "producto"), filtros_pais).head(10)
    st.dataframe(
        top,
        hide_index=True,
        column_order=["producto", "categoria", "subcategoria", "ventas_total", "ventas_promedio"],
        column_config={
            "producto": "Producto",
            "categoria": "Categoría",
            "subcategoria": "Subcategoría",
            "ventas_total": st.column_config.NumberColumn("Ventas", format="localized"),
            "ventas_promedio": st.column_config.NumberColumn("Venta promedio", format="%.0f"),
        },
        alt=f"Los diez productos con más ventas en {pais}",
    )
    if st.button("Volver al tablero", icon=":material/arrow_back:"):
        cerrar_detalle()
        st.rerun()


# El país del detalle viene de la URL: se valida antes de usarlo
pais_detalle = st.query_params.get("detalle")
if pais_detalle in PAISES:
    detalle_pais(pais_detalle, filtros)


# --- 9. Título dinámico y KPIs (en el contenedor reservado arriba) -----------
with cabecera:
    st.title(titulo_dinamico(seleccion or paises, PAISES, categorias, CATEGORIAS, desde, hasta))
    if seleccion:
        st.caption(f"Filtro cruzado activo desde el gráfico de países: {', '.join(seleccion)}.")
    resumen = kpis(filtros_cruzados)
    with st.container(horizontal=True):
        st.metric("Ventas", millones(resumen["ventas_total"]), border=True)
        st.metric("Unidades", entero(resumen["cantidad_total"]), border=True)
        st.metric("Transacciones", entero(resumen["transacciones"]), border=True)
        st.metric("Venta promedio", entero(resumen["ventas_promedio"]), border=True)

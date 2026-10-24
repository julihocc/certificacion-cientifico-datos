"""Mi primer dashboard: ventas 2019-2021 con formato condicional (Módulo 46).

Ejecutar desde la raíz del repositorio:

    uv run streamlit run s08-dashboards/m46-formato-condicional/m46-formato-condicional-app.py
"""

import sys
from pathlib import Path

import plotly.express as px
import streamlit as st
from matplotlib.colors import LinearSegmentedColormap

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "practica-ventas"))
import ventas as practica  # noqa: E402

# --- 1. Configuración, conexión y consultas en caché ---
st.set_page_config(page_title="Mi primer dashboard", page_icon=":material/bar_chart:", layout="wide")

# Escala de dos colores para el texto: los dos extremos contrastan con un fondo blanco
NARANJA_AZUL = LinearSegmentedColormap.from_list("naranja_azul", ["#b35806", "#2166ac"])
GRANULARIDAD = {"Día": "day", "Mes": "month", "Año": "year"}


@st.cache_resource
def conexion():
    # Una sola conexión DuckDB para todas las sesiones; ventas.py abre un cursor por consulta
    return practica.conectar()


@st.cache_data
def lista_paises(_con):
    return sorted(practica.tabla_por_pais(_con)["pais"])


@st.cache_data
def leer_kpis(_con, paises):
    return practica.kpis(_con, paises=paises)


@st.cache_data
def leer_tabla(_con, paises):
    return practica.tabla_por_pais(_con, paises=paises)


@st.cache_data
def leer_categorias(_con, paises):
    return practica.ventas_por(_con, "categoria", paises=paises)


@st.cache_data
def leer_serie(_con, nivel, paises):
    return practica.serie_temporal(_con, nivel, paises=paises)


def millones(valor):
    # 41940958825 -> "41 941.0 M"
    return f"{valor / 1e6:,.1f} M".replace(",", " ")


con = conexion()

# --- 2. Encabezado y filtro de países ---
st.title("Mi primer dashboard")
st.caption("Autor: Juliho Castillo Colmenares · Ventas de una cadena de tiendas, 2019–2021")

with st.sidebar:
    st.header("Filtros")
    seleccion = st.multiselect(
        "Países",
        lista_paises(con),
        placeholder="Todos los países",
        help="Sin selección se muestran los diez países.",
        key="paises",
    )
# En ventas.py una lista vacía no deja pasar ninguna fila; aquí "nada elegido" significa "todos"
paises = tuple(sorted(seleccion)) if seleccion else None

# --- 3. Indicadores clave ---
kpis = leer_kpis(con, paises)
with st.container(horizontal=True):
    st.metric("Ventas totales", millones(kpis["ventas_total"]), border=True)
    st.metric("Cantidad total", millones(kpis["cantidad_total"]), border=True)
    st.metric("Mediana del precio", f"{kpis['precio_mediana']:,.0f}".replace(",", " "), border=True)

# --- 4. Mapa de burbujas y anillo por categoría ---
tabla = leer_tabla(con, paises)
categorias = leer_categorias(con, paises)

izquierda, derecha = st.columns(2)
with izquierda.container(border=True):
    st.subheader("Ventas por país")
    mapa = px.scatter_geo(
        tabla,
        locations="iso3",
        size="ventas_total",
        hover_name="pais",
        hover_data={"iso3": False, "ventas_total": ":,.0f"},
        projection="natural earth",
        size_max=40,
    )
    mapa.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=360)
    st.plotly_chart(mapa, alt="Mapa de burbujas con las ventas totales de cada país")

with derecha.container(border=True):
    st.subheader("Cantidad por categoría")
    anillo = px.pie(categorias, names="categoria", values="cantidad_total", hole=0.5)
    anillo.update_traces(texttemplate="%{value:,.0f}<br>%{percent:.1%}")
    anillo.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=360)
    st.plotly_chart(anillo, alt="Gráfico de anillo con la cantidad vendida por categoría")

# --- 5. Tendencia de ventas con granularidad ---
with st.container(border=True):
    st.subheader("Tendencia de ventas")
    etiqueta = st.segmented_control(
        "Granularidad", list(GRANULARIDAD), default="Mes", required=True, key="granularidad"
    )
    serie = leer_serie(con, GRANULARIDAD[etiqueta], paises)
    linea = px.line(serie, x="periodo", y="ventas_total", labels={"periodo": "", "ventas_total": "Ventas"})
    linea.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=320)
    st.plotly_chart(linea, alt=f"Línea con las ventas totales por {etiqueta.lower()}")

# --- 6. Tabla por país con formato condicional ---
# Límites fijos, calculados sobre los diez países: el color no cambia de significado al filtrar
completa = leer_tabla(con, None)
max_mediana = float(completa["ventas_mediana"].max())
max_ventas = float(completa["ventas_total"].max()) / 1e6
uniforme = 1 / len(tabla)  # participación de cada país si todos vendieran lo mismo

vista = tabla[["pais", "ventas_mediana", "ventas_total", "pct_cantidad"]].assign(
    ventas_total=tabla["ventas_total"] / 1e6
)
estilo = (
    vista.style
    .background_gradient(subset=["ventas_mediana"], cmap="Blues", vmin=0, vmax=max_mediana)
    .text_gradient(subset=["pct_cantidad"], cmap=NARANJA_AZUL, vmin=0.9 * uniforme, vmax=1.1 * uniforme)
)

with st.container(border=True):
    st.subheader("Ventas por país")
    st.dataframe(
        estilo,
        hide_index=True,
        column_config={
            "pais": st.column_config.TextColumn("País"),
            "ventas_mediana": st.column_config.NumberColumn("Mediana de ventas", format="%.0f"),
            "ventas_total": st.column_config.ProgressColumn(
                "Ventas totales (M)", format="%.1f", min_value=0, max_value=max_ventas
            ),
            "pct_cantidad": st.column_config.NumberColumn("% de la cantidad", format="percent"),
        },
        alt="Tabla de ventas por país con mediana, total y porcentaje de la cantidad",
    )
    st.caption(
        "Fondo: mediana de ventas (0 a máximo de los diez países). Barras: ventas totales. "
        "Color de fuente: % de la cantidad, de naranja (10 % por debajo del reparto uniforme) "
        "a azul (10 % por encima)."
    )

    # --- 7. Descarga de la tabla filtrada ---
    st.download_button(
        "Descargar CSV",
        data=tabla.drop(columns="ventas_promedio").to_csv(index=False).encode("utf-8"),
        file_name="ventas-por-pais.csv",
        mime="text/csv",
        icon=":material/download:",
        on_click="ignore",
    )

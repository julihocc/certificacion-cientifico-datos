"""Proyecto P05: dashboard de COVID-19 por país.

Lee las series de tiempo globales del JHU CSSE COVID-19 Data Repository
(copia local en ``datos/``, licencia CC BY 4.0) y muestra cinco rankings por
país a una fecha de corte, un mapa y una descarga en CSV.

Desde la raíz del repositorio:

    uv run streamlit run proyectos/p05-dashboard-covid/p05-dashboard-covid-app.py
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATOS = Path(__file__).parent / "datos"
ARCHIVOS = {
    "confirmados": "casos-confirmados.csv",
    "muertes": "muertes.csv",
    "recuperados": "recuperados.csv",
}
DESCRIPTIVAS = ["Province/State", "Country/Region", "Lat", "Long"]
# Entradas de Country/Region que no son países
NO_PAISES = ["Diamond Princess", "MS Zaandam", "Summer Olympics 2020", "Winter Olympics 2022", "Antarctica"]
AUTOR = "Juliho Castillo Colmenares"
FUENTE = (
    "Datos: [COVID-19 Data Repository](https://github.com/CSSEGISandData/COVID-19) del "
    "CSSE de la Universidad Johns Hopkins (archivado en marzo de 2023), licencia CC BY 4.0."
)


def miles(numero):
    """Entero con espacios como separador de miles (1 234 567)."""
    return f"{numero:,.0f}".replace(",", " ")


# ---------------------------------------------------------------------------
# Datos
# ---------------------------------------------------------------------------
@st.cache_data(show_spinner="Leyendo las series de tiempo...")
def cargar_series():
    """Las tres series en formato largo: una fila por provincia y día."""
    series = {}
    for medida, archivo in ARCHIVOS.items():
        ancho = pd.read_csv(DATOS / archivo)
        largo = ancho.melt(id_vars=DESCRIPTIVAS, var_name="fecha", value_name=medida)
        largo["fecha"] = pd.to_datetime(largo["fecha"], format="%m/%d/%y")
        largo["Province/State"] = largo["Province/State"].fillna("")
        series[medida] = largo
    return series


def maximo_y_suma(largo, medida, corte):
    """Máximo de cada provincia hasta la fecha de corte y suma por país."""
    hasta = largo[largo["fecha"] <= corte]
    por_provincia = hasta.groupby(["Country/Region", "Province/State"])[medida].max()
    return por_provincia.groupby("Country/Region").sum()


@st.cache_data
def recuperados_por_dia():
    """Total diario de recuperados de cada país (suma del máximo acumulado de sus provincias)."""
    rec = cargar_series()["recuperados"].sort_values("fecha")
    rec["acumulado"] = rec.groupby(["Country/Region", "Province/State"])["recuperados"].cummax()
    return rec.groupby(["Country/Region", "fecha"])["acumulado"].sum().unstack("Country/Region")


@st.cache_data
def fechas():
    """Primera y última fecha de las series, y último día con recuperados informados."""
    series = cargar_series()
    conf = series["confirmados"]["fecha"]
    rec = series["recuperados"].groupby("fecha")["recuperados"].sum()
    return conf.min().date(), conf.max().date(), rec[rec > 0].index.max()


@st.cache_data
def tabla_por_pais(corte, fecha_rec):
    """Medidas por país: totales a la fecha de corte y recuperación a ``fecha_rec``."""
    series = cargar_series()
    tabla = pd.DataFrame({
        "confirmados": maximo_y_suma(series["confirmados"], "confirmados", corte),
        "muertes": maximo_y_suma(series["muertes"], "muertes", corte),
        "confirmados_a_fecha_rec": maximo_y_suma(series["confirmados"], "confirmados", fecha_rec),
        "recuperados": maximo_y_suma(series["recuperados"], "recuperados", fecha_rec),
    })
    # División segura: sin casos, la tasa queda vacía (NaN) en lugar de dar error
    tabla["mortalidad"] = 100 * tabla["muertes"] / tabla["confirmados"].where(tabla["confirmados"] > 0)
    tabla["recuperacion"] = 100 * tabla["recuperados"] / tabla["confirmados_a_fecha_rec"].where(
        tabla["confirmados_a_fecha_rec"] > 0
    )
    # Último día (hasta fecha_rec) en que aumentó el total de recuperados del país
    diario = recuperados_por_dia().loc[:fecha_rec]
    aumentos = diario.diff().gt(0)
    tabla["recuperados_hasta"] = aumentos.apply(lambda col: col[col].index.max())
    tabla["es_pais"] = ~tabla.index.isin(NO_PAISES)
    return tabla.rename_axis("pais").reset_index()


@st.cache_data
def puntos_del_mapa(corte):
    """Confirmados y muertes por provincia (o país) con coordenadas válidas."""
    series = cargar_series()
    claves = ["Country/Region", "Province/State", "Lat", "Long"]
    conf = series["confirmados"]
    conf = conf[conf["fecha"] <= corte].groupby(claves, dropna=False)["confirmados"].max()
    muer = series["muertes"]
    muer = muer[muer["fecha"] <= corte].groupby(["Country/Region", "Province/State"])["muertes"].max()
    puntos = conf.reset_index().merge(muer.reset_index(), on=["Country/Region", "Province/State"])
    # Cruceros, repatriados y "Unknown" no tienen coordenadas (vacías o 0, 0)
    validos = puntos["Lat"].notna() & ~((puntos["Lat"] == 0) & (puntos["Long"] == 0))
    puntos = puntos[validos & (puntos["confirmados"] > 0)].copy()
    puntos["lugar"] = puntos["Province/State"].where(puntos["Province/State"] != "", puntos["Country/Region"])
    return puntos


# ---------------------------------------------------------------------------
# Página
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Dashboard de COVID-19", page_icon=":material/coronavirus:", layout="wide")

primera, ultima, ultima_rec = fechas()

with st.sidebar:
    st.header("Controles")
    corte = st.date_input("Fecha de corte", value=ultima, min_value=primera, max_value=ultima, format="DD/MM/YYYY")
    minimo = st.number_input(
        "Mínimo de casos para las tasas",
        min_value=0,
        value=10_000,
        step=1_000,
        help="Un país entra en los rankings de mortalidad y recuperación solo si tiene al menos estos casos confirmados.",
    )
    top_n = st.slider("Países por tabla", min_value=5, max_value=30, value=10)
    solo_paises = st.toggle(
        "Excluir entradas que no son países",
        value=True,
        help="Cruceros (Diamond Princess, MS Zaandam), Juegos Olímpicos 2020 y 2022, y Antártida.",
    )
    st.caption(FUENTE)

corte = pd.Timestamp(corte)
fecha_rec = min(corte, ultima_rec)

st.title("Dashboard de COVID-19")
st.caption(f"Autor: {AUTOR} · Valores acumulados al {corte:%d/%m/%Y}")

tabla = tabla_por_pais(corte, fecha_rec)
if solo_paises:
    tabla = tabla[tabla["es_pais"]]

confirmados = tabla["confirmados"].sum()
muertes = tabla["muertes"].sum()
with st.container(horizontal=True):
    st.metric("Casos confirmados", miles(confirmados), border=True)
    st.metric("Muertes", miles(muertes), border=True)
    st.metric("Mortalidad global", f"{100 * muertes / confirmados:.2f} %" if confirmados else "—", border=True)
    st.metric("Países con casos", f"{(tabla['confirmados'] > 0).sum()}", border=True)

PAIS = st.column_config.TextColumn("País")
ENTERO = "localized"
TASA = "%.2f %%"


def mostrar(titulo, datos, columnas, config, alt, nota=None):
    with st.container(border=True):
        st.subheader(titulo)
        if datos.empty:
            st.info("Ningún país cumple las condiciones con esta fecha de corte.")
        else:
            st.dataframe(datos[columnas], hide_index=True, column_config={"pais": PAIS, **config}, alt=alt)
        if nota:
            st.caption(nota)


con_casos = tabla[tabla["confirmados"] > 0]
col1, col2 = st.columns(2)
with col1:
    mostrar(
        "Países con más contagios",
        con_casos.nlargest(top_n, "confirmados"),
        ["pais", "confirmados"],
        {"confirmados": st.column_config.NumberColumn("Confirmados", format=ENTERO)},
        "Países con más casos confirmados",
    )
with col2:
    mostrar(
        "Países con más decesos",
        tabla[tabla["muertes"] > 0].nlargest(top_n, "muertes"),
        ["pais", "muertes"],
        {"muertes": st.column_config.NumberColumn("Muertes", format=ENTERO)},
        "Países con más muertes",
    )

# El mínimo de casos se aplica antes de ordenar: así los países con pocos casos
# (o sin casos, con tasa vacía) no llegan a los rankings de tasas
elegibles = tabla[(tabla["confirmados"] >= max(minimo, 1)) & tabla["mortalidad"].notna()]
config_mortalidad = {
    "mortalidad": st.column_config.NumberColumn("Mortalidad", format=TASA),
    "confirmados": st.column_config.NumberColumn("Confirmados", format=ENTERO),
}
nota_minimo = f"Solo países con al menos {miles(minimo)} casos confirmados."
col3, col4, col5 = st.columns(3)
with col3:
    mostrar(
        "Países con mayor tasa de mortalidad",
        elegibles.nlargest(top_n, "mortalidad"),
        ["pais", "mortalidad", "confirmados"],
        config_mortalidad,
        "Países con mayor tasa de mortalidad",
        nota_minimo,
    )
with col4:
    mostrar(
        "Países con menor tasa de mortalidad",
        elegibles.nsmallest(top_n, "mortalidad"),
        ["pais", "mortalidad", "confirmados"],
        config_mortalidad,
        "Países con menor tasa de mortalidad",
        nota_minimo,
    )
with col5:
    # Los países que nunca informaron recuperados (tasa 0) no entran
    recuperacion = tabla[(tabla["confirmados_a_fecha_rec"] >= max(minimo, 1)) & (tabla["recuperados"] > 0)]
    mostrar(
        "Países con mayor índice de recuperación",
        recuperacion.nlargest(top_n, "recuperacion"),
        ["pais", "recuperacion", "recuperados_hasta"],
        {
            "recuperacion": st.column_config.NumberColumn("Recuperación", format=TASA),
            "recuperados_hasta": st.column_config.DateColumn("Último aumento", format="DD/MM/YYYY"),
        },
        "Países con mayor índice de recuperación",
        f"Recuperados y confirmados al {fecha_rec:%d/%m/%Y}: la serie de recuperados dejó de "
        f"actualizarse el {ultima_rec:%d/%m/%Y}. Se excluyen los países sin recuperados informados. "
        + nota_minimo,
    )

with st.container(border=True):
    st.subheader("Casos confirmados por provincia o país")
    puntos = puntos_del_mapa(corte)
    if solo_paises:
        puntos = puntos[~puntos["Country/Region"].isin(NO_PAISES)]
    if puntos.empty:
        st.info("No hay casos confirmados con esta fecha de corte.")
    else:
        mapa = px.scatter_geo(
            puntos,
            lat="Lat",
            lon="Long",
            size="confirmados",
            hover_name="lugar",
            hover_data={"Country/Region": True, "confirmados": ":,", "muertes": ":,", "Lat": False, "Long": False},
            labels={"Country/Region": "País", "confirmados": "Confirmados", "muertes": "Muertes"},
            projection="natural earth",
            size_max=40,
        )
        mapa.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=480)
        st.plotly_chart(mapa, alt="Mapa de casos confirmados por provincia o país")
    st.caption("Las filas sin coordenadas (cruceros, viajeros repatriados, provincia desconocida) no aparecen en el mapa.")

descarga = tabla.drop(columns="es_pais").sort_values("confirmados", ascending=False)
st.download_button(
    "Descargar la tabla por país (CSV)",
    data=descarga.to_csv(index=False).encode("utf-8"),
    file_name=f"covid-por-pais-{corte:%Y-%m-%d}.csv",
    mime="text/csv",
    icon=":material/download:",
)

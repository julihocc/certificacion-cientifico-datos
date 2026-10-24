"""Resumen: KPIs, mapa, anillo, tendencia y tabla con formato condicional (Módulo 46)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import plotly.express as px
import streamlit as st

import comun
import estilo

filtro = comun.filtros()
comun.detener_si_vacio(filtro)

st.title("Resumen de ventas")
st.caption(comun.descripcion(filtro))

# Franja superior: los KPI, lo primero que se lee
k = comun.kpis(**filtro)
with st.container(horizontal=True):
    st.metric("Ventas totales", estilo.millones(k["ventas_total"]), border=True)
    st.metric("Unidades vendidas", estilo.entero(k["cantidad_total"]), border=True)
    st.metric("Precio mediano", estilo.entero(k["precio_mediana"] or 0), border=True)
    st.metric("Transacciones", estilo.entero(k["transacciones"]), border=True)

if k["transacciones"] == 0:
    st.info("No hay ventas con estos filtros.", icon=":material/filter_alt_off:")
    st.stop()

tabla = comun.tabla_por_pais(**filtro)
categorias = comun.ventas_por("categoria", **filtro)

# Franja central: dónde se vende y en qué se reparte
izquierda, derecha = st.columns([3, 2])
with izquierda.container(border=True, height="stretch"):
    mapa = px.scatter_geo(
        tabla, locations="iso3", size="ventas_total", hover_name="pais",
        hover_data={"iso3": False, "ventas_total": ":,.0f"},
        labels={"ventas_total": "Ventas"},
        projection="natural earth", color_discrete_sequence=[estilo.PRIMARIO],
        title="Ventas por país", size_max=40,
    )
    mapa.update_geos(fitbounds="locations")
    mapa.update_layout(height=380)
    st.plotly_chart(estilo.ajustar(mapa), theme=None, alt="Mapa de burbujas con las ventas por país")
with derecha.container(border=True, height="stretch"):
    anillo = px.pie(
        categorias, names="categoria", values="cantidad_total", hole=0.55,
        color="categoria", color_discrete_map=estilo.COLORES_CATEGORIA,
        title="Unidades por categoría",
    )
    anillo.update_traces(textinfo="percent", sort=False,
                         marker=dict(line=dict(color=estilo.FONDO, width=2)),
                         hovertemplate="%{label}: %{value:,.0f} unidades<extra></extra>")
    anillo.update_layout(height=380)
    st.plotly_chart(estilo.ajustar(anillo), theme=None, alt="Gráfico de anillo con las unidades por categoría")

with st.container(border=True):
    serie = comun.serie_temporal("month", **filtro)
    serie["ventas_m"] = serie["ventas_total"] / 1e6
    tendencia = px.line(serie, x="periodo", y="ventas_m", title="Tendencia de ventas mensuales",
                        labels={"periodo": "", "ventas_m": "Ventas (millones)"})
    tendencia.update_traces(line=dict(width=2), hovertemplate="%{x|%m/%Y}: %{y:,.1f} M<extra></extra>")
    tendencia.update_layout(height=320, xaxis_tickformat="%m/%Y")
    st.plotly_chart(estilo.ajustar(tendencia), theme=None, alt="Gráfico de líneas con las ventas por mes")

# Franja inferior: el detalle exacto, con formato condicional
st.subheader("Detalle por país")
detalle = tabla.assign(ventas_m=tabla["ventas_total"] / 1e6)[
    ["pais", "ventas_mediana", "ventas_m", "pct_cantidad"]
]
estilada = (
    detalle.style
    .apply(estilo.fondo_degradado, subset=["ventas_mediana"])       # color de fondo
    .apply(estilo.texto_degradado, subset=["pct_cantidad"])         # color de fuente
    .format({"ventas_mediana": estilo.entero, "pct_cantidad": estilo.porcentaje})
)
st.dataframe(
    estilada,
    hide_index=True,
    column_config={
        "pais": st.column_config.TextColumn("País"),
        "ventas_mediana": st.column_config.Column("Mediana de ventas"),
        "ventas_m": st.column_config.ProgressColumn(              # barras de datos
            "Ventas totales (M)", format="%.1f", min_value=0, max_value=float(detalle["ventas_m"].max()),
        ),
        "pct_cantidad": st.column_config.Column("% de unidades"),
    },
    alt="Tabla de ventas por país con formato condicional",
)
st.download_button(
    "Descargar tabla (CSV)", tabla.to_csv(index=False).encode("utf-8"),
    file_name="ventas-por-pais.csv", mime="text/csv", icon=":material/download:",
)

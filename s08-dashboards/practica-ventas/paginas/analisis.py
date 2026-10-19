"""Análisis por país: filtro cruzado, mapa de árbol y diálogo de detalle (Módulo 48)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import plotly.express as px
import streamlit as st

import comun
import estilo

filtro = comun.filtros()
comun.detener_si_vacio(filtro)

st.title("Análisis por país")
st.caption(comun.descripcion(filtro))

por_pais = comun.ventas_por("pais", **filtro).sort_values("ventas_promedio")
if por_pais.empty:
    st.info("No hay ventas con estos filtros.", icon=":material/filter_alt_off:")
    st.stop()


@st.dialog("Detalle del país", width="large")
def detalle(pais: str, filtro: dict) -> None:
    """Equivalente a una página de obtención de detalles: el contexto es el país elegido."""
    del_pais = dict(filtro, paises=(pais,))
    st.subheader(pais)
    serie = comun.serie_temporal("month", **del_pais)
    mini = px.area(serie, x="periodo", y="cantidad_total", labels={"periodo": "", "cantidad_total": "Unidades"},
                   title="Unidades vendidas por mes")
    mini.update_traces(line=dict(width=2, color=estilo.PRIMARIO))
    mini.update_layout(height=220)
    st.plotly_chart(estilo.ajustar(mini), theme=None, alt=f"Unidades vendidas por mes en {pais}")
    productos = comun.ventas_por(("categoria", "subcategoria", "producto"), **del_pais)
    productos = productos.sort_values("ventas_promedio", ascending=False)
    st.dataframe(
        productos[["categoria", "subcategoria", "producto", "ventas_promedio", "ventas_total"]]
        .style.format({"ventas_promedio": estilo.entero, "ventas_total": estilo.entero}),
        hide_index=True, height=320,
        column_config={
            "categoria": "Categoría", "subcategoria": "Subcategoría", "producto": "Producto",
            "ventas_promedio": "Venta promedio", "ventas_total": "Ventas totales",
        },
        alt=f"Productos vendidos en {pais}",
    )


izquierda, derecha = st.columns([2, 3])
with izquierda.container(border=True, height="stretch"):
    barras = px.bar(
        por_pais, x="ventas_promedio", y="pais", orientation="h", custom_data=["pais"],
        title="Venta promedio por país", labels={"ventas_promedio": "Venta promedio", "pais": ""},
        color_discrete_sequence=[estilo.PRIMARIO],
    )
    barras.update_traces(hovertemplate="%{y}: %{x:,.0f}<extra></extra>")
    barras.update_layout(height=420, clickmode="event+select")
    evento = st.plotly_chart(estilo.ajustar(barras), theme=None, on_select="rerun", selection_mode="points",
                             key="seleccion_paises", alt="Barras con la venta promedio por país")
    st.caption("Haz clic en una o varias barras (Mayús + clic) para filtrar el mapa de árbol; doble clic para limpiar.")

# Filtro cruzado: la selección del gráfico de barras filtra el mapa de árbol
puntos = evento.selection.points if evento and evento.selection else []
visibles = set(por_pais["pais"])
elegidos = sorted({p["customdata"][0] for p in puntos if p.get("customdata")} & visibles)
filtro_cruzado = dict(filtro, paises=tuple(elegidos)) if elegidos else filtro

with derecha.container(border=True, height="stretch"):
    subcategorias = comun.ventas_por(("categoria", "subcategoria"), **filtro_cruzado)
    titulo = "Ventas por subcategoría" + (f" — {', '.join(elegidos)}" if elegidos else "")
    arbol = px.treemap(
        subcategorias, path=[px.Constant("Todas"), "categoria", "subcategoria"], values="ventas_total",
        color="categoria", color_discrete_map=estilo.COLORES_CATEGORIA | {"(?)": estilo.FONDO_SECUNDARIO},
        title=titulo,
    )
    arbol.update_traces(hovertemplate="%{label}: %{value:,.0f}<extra></extra>", marker=dict(line=dict(width=2)))
    arbol.update_layout(height=420)
    st.plotly_chart(estilo.ajustar(arbol), theme=None, alt="Mapa de árbol con las ventas por categoría y subcategoría")

st.subheader("Detalle de productos")
with st.container(horizontal=True, vertical_alignment="bottom"):
    opciones = sorted(visibles)
    pais = st.selectbox("País", opciones, index=opciones.index(elegidos[0]) if elegidos else 0)
    if st.button("Ver detalle", icon=":material/open_in_new:", type="primary"):
        detalle(pais, filtro)

"""Medidas de tiempo: mes anterior, año anterior, acumulado del año (Módulo 47)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import comun
import estilo
import ventas

filtro = comun.filtros()
comun.detener_si_vacio(filtro)

st.title("Medidas de tiempo")
st.caption(comun.descripcion(filtro))

mensual = comun.ventas_mensuales(**filtro)
con_datos = mensual.dropna(subset=["ventas"])
if con_datos.empty:
    st.info("No hay ventas con estos filtros.", icon=":material/filter_alt_off:")
    st.stop()


def variacion(valor) -> str | None:
    return None if pd.isna(valor) else f"{valor * 100:+.1f} %"


ultimo = con_datos.iloc[-1]
mes = f"{ultimo['nombre_mes']} {ultimo['anio']}"
st.markdown(f"Último mes del periodo con ventas: **{mes}**.")
with st.container(horizontal=True):
    st.metric(f"Ventas de {mes}", estilo.millones(ultimo["ventas"]),
              delta=variacion(ultimo["var_mensual"]), help="Variación frente al mes anterior.", border=True)
    anterior = ultimo["ventas_mismo_mes_anio_anterior"]
    st.metric("Mismo mes del año anterior", "—" if pd.isna(anterior) else estilo.millones(anterior),
              delta=variacion(ultimo["var_anual"]), help="Variación del mes actual frente a este valor.",
              border=True)
    st.metric("Acumulado del año (YTD)", estilo.millones(ultimo["ventas_ytd"]), border=True,
              help="Ventas desde el 1 de enero hasta el final del mes.")
    st.metric("Venta promedio", estilo.entero(ultimo["ventas_promedio"]), border=True,
              help="Importe medio por transacción en el mes.")

izquierda, derecha = st.columns(2)
with izquierda.container(border=True, height="stretch"):
    # Mismo eje para las dos series: las dos son ventas en la misma unidad
    meses = pd.to_datetime(mensual["anio_mes"] + "-01")
    fig = go.Figure()
    fig.add_bar(x=meses, y=mensual["ventas"] / 1e6, name="Ventas del mes",
                marker_color=estilo.PALETA[0], hovertemplate="%{x|%m/%Y}: %{y:,.1f} M<extra></extra>")
    fig.add_scatter(x=meses, y=mensual["ventas_mismo_mes_anio_anterior"] / 1e6,
                    name="Mismo mes del año anterior", mode="lines+markers",
                    line=dict(color=estilo.PALETA[1], width=2), marker=dict(size=8),
                    hovertemplate="%{x|%m/%Y}: %{y:,.1f} M<extra></extra>")
    fig.update_layout(title="Ventas frente al año anterior", height=360, xaxis_tickformat="%m/%Y",
                      yaxis_title="Ventas (millones)")
    st.plotly_chart(estilo.ajustar(fig), theme=None, alt="Barras de ventas mensuales con la línea del mismo mes del año anterior")
with derecha.container(border=True, height="stretch"):
    acumulado = con_datos.assign(anio=con_datos["anio"].astype(str), ytd_m=con_datos["ventas_ytd"] / 1e6)
    fig = px.line(acumulado, x="mes", y="ytd_m", color="anio", markers=True, title="Acumulado del año por mes",
                  labels={"mes": "", "ytd_m": "Ventas acumuladas (millones)", "anio": ""})
    fig.update_traces(line=dict(width=2), marker=dict(size=8))
    fig.update_layout(height=360, xaxis=dict(tickmode="array", tickvals=list(range(1, 13)),
                                             ticktext=[m.capitalize() for m in ventas.NOMBRES_MES]))
    st.plotly_chart(estilo.ajustar(fig), theme=None, alt="Líneas del acumulado de ventas del año, una por año")

st.subheader("Tabla de validación")
st.caption("El mes anterior de cada fila es la venta de la fila de arriba, y el acumulado se reinicia en enero.")
columnas = {
    "anio_mes": "Mes", "ventas": "Ventas", "ventas_mes_anterior": "Mes anterior",
    "ventas_mismo_mes_anio_anterior": "Mismo mes año anterior", "ventas_ytd": "Acumulado del año",
    "dif_mensual": "Diferencia mensual", "var_mensual": "Var. mensual", "var_anual": "Var. anual",
}
tabla = mensual[list(columnas)]
# Texto ya formateado (espacio de miles, "—" para los meses sin dato), alineado a la derecha
formato = {c: estilo.entero for c in list(columnas)[1:6]} | {"var_mensual": estilo.porcentaje, "var_anual": estilo.porcentaje}
vista = tabla.copy()
for columna, funcion in formato.items():
    vista[columna] = tabla[columna].map(lambda v, f=funcion: "—" if pd.isna(v) else f(v))
st.dataframe(
    vista,
    hide_index=True,
    column_config={c: st.column_config.TextColumn(n, alignment="right" if c in formato else None)
                   for c, n in columnas.items()},
    alt="Tabla de medidas de tiempo por mes",
)
st.download_button(
    "Descargar medidas (CSV)", tabla.to_csv(index=False).encode("utf-8"),
    file_name="medidas-de-tiempo.csv", mime="text/csv", icon=":material/download:",
)

"""Dashboard de ventas: app final de la sección S08 (Módulos 44 a 50).

Ejecutar desde la raíz del repositorio:

    uv run streamlit run s08-dashboards/practica-ventas/app.py

Este archivo es el punto de entrada: configura la página, dibuja lo que comparten
todas las páginas (logotipo, acceso y filtros de la barra lateral) y delega el
contenido en las páginas de `paginas/` con `st.navigation`.
"""

from pathlib import Path

import streamlit as st

import comun
import estilo  # noqa: F401  (registra la plantilla de Plotly)
import seguridad

RUTA = Path(__file__).resolve().parent

st.set_page_config(page_title="Ventas", page_icon=":material/storefront:", layout="wide")
st.logo(str(RUTA / "icono-inicio.jpg"), size="large")

inicio = st.Page("paginas/inicio.py", title="Inicio", icon=":material/home:", default=True)
paginas = {
    "": [inicio],
    "Tablero": [
        st.Page("paginas/resumen.py", title="Resumen", icon=":material/dashboard:"),
        st.Page("paginas/medidas.py", title="Medidas de tiempo", icon=":material/calendar_month:"),
        st.Page("paginas/analisis.py", title="Análisis por país", icon=":material/travel_explore:"),
    ],
    "Información": [
        st.Page("paginas/acerca.py", title="Acerca de", icon=":material/info:"),
    ],
}
pagina = st.navigation(paginas, position="sidebar")

with st.sidebar:
    seguridad.panel_acceso()
    comun.barra_lateral()

# Botón de inicio en el mismo lugar de todas las páginas, salvo en la propia portada
if pagina.url_path != inicio.url_path:
    st.page_link(inicio, label="Inicio", icon=":material/home:")

pagina.run()

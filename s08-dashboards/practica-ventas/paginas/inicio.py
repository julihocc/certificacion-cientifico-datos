"""Página de inicio: presentación y menú de navegación (Módulo 49)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import streamlit as st

import comun
import estilo
import seguridad

comun.iniciar_estado()

st.title("Dashboard de ventas")
st.markdown(
    "Ventas de una cadena de tiendas en diez países de América y Europa, de 2019 a 2021. "
    "Usa el menú para elegir una página; los filtros de la barra lateral se conservan al cambiar de página."
)

# Menú: una tarjeta por página, en una cuadrícula que se apila en pantallas estrechas
MENU = [
    ("paginas/resumen.py", "Resumen", ":material/dashboard:",
     "KPIs, mapa, reparto por categoría, tendencia mensual y tabla por país."),
    ("paginas/medidas.py", "Medidas de tiempo", ":material/calendar_month:",
     "Mes anterior, mismo mes del año anterior, acumulado del año y variaciones."),
    ("paginas/analisis.py", "Análisis por país", ":material/travel_explore:",
     "Filtro cruzado entre gráficos, mapa de árbol y detalle de productos por país."),
    ("paginas/acerca.py", "Acerca de", ":material/info:",
     "Fuentes de datos, autor y cómo se construyó la app."),
]
columnas = st.columns(2)
for i, (ruta, titulo, icono, texto) in enumerate(MENU):
    with columnas[i % 2].container(border=True, height="stretch"):
        st.page_link(ruta, label=titulo, icon=icono)
        st.caption(texto)


st.subheader("Accesos rápidos")
with st.container(horizontal=True):
    for clave in ("2019-s1", "2019-s2"):
        # El callback fija el marcador antes de la nueva ejecución; después se cambia de página
        if st.button(
            f"Resumen de {comun.MARCADORES[clave]['nombre']}",
            key=f"inicio_{clave}",
            icon=":material/bookmark:",
            on_click=comun.aplicar_marcador,
            args=(clave,),
        ):
            st.switch_page("paginas/resumen.py", query_params={"marcador": clave})

# Incluso este resumen respeta la seguridad por filas: solo cuenta los países permitidos
permitidos = seguridad.paises_permitidos()
if permitidos is None or permitidos:
    k = comun.kpis(paises=tuple(permitidos) if permitidos is not None else None)
    st.caption(
        f"Datos visibles para ti: {estilo.entero(k['transacciones'])} ventas entre el "
        f"{comun.INICIO:%d/%m/%Y} y el {comun.FIN:%d/%m/%Y}, por un total de {estilo.millones(k['ventas_total'])}. "
        "Las cifras de las demás páginas respetan además los filtros de la barra lateral."
    )

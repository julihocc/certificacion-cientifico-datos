"""Acerca de: fuentes, autor y cómo se construyó la app."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import duckdb
import plotly
import streamlit as st

import comun
import seguridad

comun.iniciar_estado()

st.title("Acerca de este dashboard")

st.subheader("Datos")
st.markdown(
    "Extracto de ventas de una cadena de tiendas con presencia en diez países (2019–2021): "
    "1 499 000 transacciones, 200 tiendas y un catálogo de clientes y productos. Los archivos "
    "originales (CSV, TXT y Excel) están en `practica-ventas/datos-ventas/`; la app lee el modelo "
    "ya limpio en Parquet de `practica-ventas/datos-modelo/`, que genera `preparar_datos.py`."
)

st.subheader("Cómo se construyó")
st.table(
    {
        "Módulo": ["44", "45", "46", "47", "48", "49", "50"],
        "Tema": ["Preparación de datos", "Modelado de datos", "Formato condicional", "Medidas y KPIs",
                 "Interactividad", "Diseño de dashboards", "Publicación"],
        "Dónde está en la app": [
            "ventas.py: funciones leer_*",
            "ventas.py: conectar() y la vista ventas_detalle",
            "Página Resumen: tarjetas, mapa, anillo y tabla",
            "Página Medidas de tiempo",
            "Página Análisis por país: filtro cruzado y diálogo",
            "app.py, estilo.py, inicio, marcadores y tema",
            "seguridad.py, requirements.txt y secretos",
        ],
    },
    alt="Módulos de la sección y dónde se usa cada uno en la app",
)
st.markdown(
    "La app usa **pandas** para la limpieza, **DuckDB** para el modelo y las consultas, **Plotly** "
    "para los gráficos y **Streamlit** para la interfaz. Las consultas se agregan en DuckDB y solo "
    "llegan a la app las tablas resumidas, nunca los casi 1.5 millones de filas de ventas."
)
st.caption(f"Versiones: Streamlit {st.__version__} · Plotly {plotly.__version__} · DuckDB {duckdb.__version__}")

st.subheader("Acceso a los datos")
permitidos = seguridad.paises_permitidos()
if seguridad.auth_configurada():
    modo = "producción (inicio de sesión con un proveedor OIDC)"
else:
    modo = "demostración (selector «Ver como» en la barra lateral)"
visibles = "todos los países" if permitidos is None else (", ".join(permitidos) or "ningún país")
st.markdown(f"Modo de seguridad: **{modo}**. Países visibles en esta sesión: **{visibles}**.")

st.subheader("Autor")
st.markdown(
    "Juliho Castillo Colmenares. Proyecto de la sección de dashboards de la certificación de ciencia de datos; "
    "la versión original se hizo en Power BI y se rehízo en Python para no depender de software de pago."
)

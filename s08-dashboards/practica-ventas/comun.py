"""Piezas compartidas por las páginas de la app: conexión, consultas en caché y filtros.

- La conexión a DuckDB se abre una vez por servidor (`st.cache_resource`).
- Cada consulta se guarda en caché según sus filtros (`st.cache_data`), con un
  `ttl` para que los datos nuevos aparezcan sin reiniciar la app (Módulo 50).
- Los filtros viven en `st.session_state`: los dibuja `app.py` en la barra lateral
  y las páginas los leen con `filtros()`. Si una página se abre sola (por ejemplo,
  en una prueba), `iniciar_estado()` pone los valores por defecto con `setdefault`.
- La seguridad por filas (`seguridad.py`) se aplica dentro de `filtros()`: el
  argumento `paises` de cada consulta ya viene recortado a los países permitidos.
"""

from __future__ import annotations

import datetime as dt

import pandas as pd
import streamlit as st

import seguridad
import ventas

INICIO = dt.date(2019, 1, 1)
FIN = dt.date(2021, 12, 31)
CATEGORIAS = ["Technology", "Furniture", "Office Supplies"]

# "Marcadores": estados guardados de los filtros, aplicables con un botón y por URL (?marcador=...)
MARCADORES = {
    "2019-s1": {"nombre": "2019, primer semestre", "desde": dt.date(2019, 1, 1), "hasta": dt.date(2019, 6, 30)},
    "2019-s2": {"nombre": "2019, segundo semestre", "desde": dt.date(2019, 7, 1), "hasta": dt.date(2019, 12, 31)},
    "todo": {"nombre": "Todo el periodo", "desde": INICIO, "hasta": FIN},
}

TTL = "1h"  # cuánto tiempo se reutiliza una consulta antes de volver a leer el Parquet


# ---------------------------------------------------------------------------
# Datos
# ---------------------------------------------------------------------------

@st.cache_resource
def conexion():
    """Modelo estrella en DuckDB leído de datos-modelo/*.parquet (una vez por servidor)."""
    return ventas.conectar()


@st.cache_data(ttl=TTL, max_entries=500, show_spinner=False)
def kpis(**filtros) -> dict:
    return ventas.kpis(conexion(), **filtros)


@st.cache_data(ttl=TTL, max_entries=500, show_spinner=False)
def ventas_por(columnas, **filtros) -> pd.DataFrame:
    return ventas.ventas_por(conexion(), list(columnas) if not isinstance(columnas, str) else columnas, **filtros)


@st.cache_data(ttl=TTL, max_entries=500, show_spinner=False)
def tabla_por_pais(**filtros) -> pd.DataFrame:
    return ventas.tabla_por_pais(conexion(), **filtros)


@st.cache_data(ttl=TTL, max_entries=500, show_spinner=False)
def serie_temporal(nivel: str = "month", **filtros) -> pd.DataFrame:
    return ventas.serie_temporal(conexion(), nivel, **filtros)


@st.cache_data(ttl=TTL, max_entries=500, show_spinner=False)
def ventas_mensuales(**filtros) -> pd.DataFrame:
    return ventas.ventas_mensuales(conexion(), **filtros)


# ---------------------------------------------------------------------------
# Estado compartido y marcadores
# ---------------------------------------------------------------------------

def iniciar_estado() -> None:
    """Valores por defecto de los filtros; un ?marcador= en la URL fija el periodo inicial."""
    if "desde" not in st.session_state or "hasta" not in st.session_state:
        marcador = MARCADORES.get(st.query_params.get("marcador"), MARCADORES["todo"])
        st.session_state.setdefault("desde", marcador["desde"])
        st.session_state.setdefault("hasta", marcador["hasta"])
    st.session_state.setdefault("paises_sel", [])
    st.session_state.setdefault("categorias_sel", [])


def aplicar_marcador(clave: str) -> None:
    """Callback de los botones de marcador: fija el periodo y lo deja en la URL."""
    marcador = MARCADORES[clave]
    st.session_state["desde"] = marcador["desde"]
    st.session_state["hasta"] = marcador["hasta"]
    if clave == "todo":
        st.query_params.pop("marcador", None)
    else:
        st.query_params["marcador"] = clave


def restablecer_filtros() -> None:
    """Callback del botón "Restablecer filtros": vuelve al estado inicial."""
    aplicar_marcador("todo")
    st.session_state["paises_sel"] = []
    st.session_state["categorias_sel"] = []


def _fecha_cambiada() -> None:
    # Al mover las fechas a mano, la URL deja de corresponder a un marcador
    st.query_params.pop("marcador", None)


def marcador_activo() -> str | None:
    for clave, marcador in MARCADORES.items():
        if (st.session_state.get("desde"), st.session_state.get("hasta")) == (marcador["desde"], marcador["hasta"]):
            return clave
    return None


def botones_marcadores(ancho: str = "stretch") -> None:
    """Un botón por marcador; el activo se resalta (como un navegador de marcadores)."""
    activo = marcador_activo()
    for clave, marcador in MARCADORES.items():
        st.button(
            marcador["nombre"],
            key=f"marcador_{clave}",
            on_click=aplicar_marcador,
            args=(clave,),
            type="primary" if clave == activo else "secondary",
            icon=":material/bookmark:",
            width=ancho,
        )


# ---------------------------------------------------------------------------
# Filtros
# ---------------------------------------------------------------------------

def barra_lateral() -> None:
    """Filtros compartidos por todas las páginas; app.py los dibuja antes de cada página."""
    iniciar_estado()
    permitidos = seguridad.paises_permitidos()
    opciones = list(ventas.ISO3) if permitidos is None else permitidos
    # Quitar países que ya no están permitidos (por ejemplo, tras cambiar de rol)
    st.session_state["paises_sel"] = [p for p in st.session_state["paises_sel"] if p in opciones]

    st.subheader("Filtros")
    columnas = st.columns(2)
    columnas[0].date_input("Desde", min_value=INICIO, max_value=FIN, key="desde", on_change=_fecha_cambiada,
                           format="DD/MM/YYYY")
    columnas[1].date_input("Hasta", min_value=INICIO, max_value=FIN, key="hasta", on_change=_fecha_cambiada,
                           format="DD/MM/YYYY")
    st.multiselect("Países", opciones, key="paises_sel", placeholder="Todos los permitidos")
    st.pills("Categorías", CATEGORIAS, selection_mode="multi", key="categorias_sel",
             help="Sin selección se incluyen las tres categorías.")
    st.caption("Marcadores")
    botones_marcadores()
    st.button("Restablecer filtros", icon=":material/restart_alt:", on_click=restablecer_filtros, width="stretch")


def filtros() -> dict:
    """Filtros activos, con la seguridad por filas ya aplicada a `paises`.

    Devuelve tuplas (hashables, para la caché) o None cuando no hay filtro.
    """
    iniciar_estado()
    permitidos = seguridad.paises_permitidos()
    elegidos = st.session_state["paises_sel"] or None
    if permitidos is None:
        paises = elegidos
    else:
        paises = [p for p in permitidos if elegidos is None or p in elegidos]
    desde, hasta = st.session_state["desde"], st.session_state["hasta"]
    if desde > hasta:
        desde, hasta = hasta, desde
    return {
        "paises": tuple(paises) if paises is not None else None,
        "categorias": tuple(st.session_state["categorias_sel"]) or None,
        "desde": desde,
        "hasta": hasta,
    }


def detener_si_vacio(filtro: dict) -> None:
    """Si la seguridad por filas no deja ningún país, avisa y detiene la página."""
    if filtro["paises"] is not None and len(filtro["paises"]) == 0:
        if seguridad.auth_configurada() and not st.user.get("is_logged_in", False):
            st.info("Inicia sesión desde la barra lateral para ver los datos.", icon=":material/lock:")
        else:
            st.warning("Tu usuario no tiene países asignados, o ninguno coincide con el filtro.",
                       icon=":material/block:")
        st.stop()


def descripcion(filtro: dict) -> str:
    """Resumen legible de los filtros activos, para el pie de cada página."""
    paises = "todos los países" if filtro["paises"] is None else ", ".join(filtro["paises"])
    categorias = "todas las categorías" if filtro["categorias"] is None else ", ".join(filtro["categorias"])
    return f"{filtro['desde']:%d/%m/%Y} – {filtro['hasta']:%d/%m/%Y} · {paises} · {categorias}"

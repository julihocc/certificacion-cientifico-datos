"""Seguridad por filas de la app de ventas (Módulo 50).

Decide qué países puede ver quien abre la app. El resultado se pasa como
argumento `paises` a las consultas de `ventas.py`, así que el filtro se aplica en
DuckDB, antes de calcular o dibujar nada:

- None: sin restricción (todos los países).
- Lista de países: solo esas filas.
- Lista vacía: ninguna fila (usuario sin países asignados).

Las reglas se leen de los secretos (`.streamlit/secrets.toml` en local, o el
campo Secrets de Streamlit Community Cloud). Ver `.streamlit/secrets.example.toml`
en la raíz del repositorio:

    [roles]                      # seguridad estática: rol -> países
    NAFTA = ["US", "CANADA", "MEXICO"]

    [miembros]                   # qué correos pertenecen a cada rol
    NAFTA = ["ana@empresa.com"]

    [usuarios]                   # seguridad dinámica: correo -> países
    "jorge@empresa.com" = ["US", "MEXICO"]

    [acceso]
    administradores = ["direccion@empresa.com"]   # ven todo

Modo producción: si los secretos tienen una sección [auth] (proveedor OIDC), la
identidad sale de `st.user.email` después de `st.login()`; es el equivalente de
USERPRINCIPALNAME() en una herramienta de BI.

Modo demostración: sin [auth], la barra lateral muestra un selector "Ver como
(solo demo)" para simular un rol o un usuario. Cualquiera puede elegir "Todos",
así que este modo no protege nada: sirve para probar las reglas.
"""

from __future__ import annotations

import streamlit as st

TODOS = "todos"

# Reglas de ejemplo para el modo demostración cuando no hay secretos
DEMO = {
    "roles": {
        "NAFTA": ["US", "CANADA", "MEXICO"],
        "SUDAMERICA": ["BRAZIL", "COLOMBIA", "CHILE", "PERU"],
        "EUROPA": ["SPAIN", "PORTUGAL", "FRANCE"],
    },
    "usuarios": {
        "marta@empresa.com": ["SPAIN", "PORTUGAL", "FRANCE"],
        "jorge@empresa.com": ["US", "MEXICO"],
    },
}


# ---------------------------------------------------------------------------
# Reglas (funciones puras, sin Streamlit: se prueban con un diccionario)
# ---------------------------------------------------------------------------

def paises_de_correo(correo: str | None, reglas: dict) -> list[str] | None:
    """Países que puede ver un correo: unión de sus roles y de su fila en [usuarios].

    Los administradores ven todo (None). Un correo sin rol ni fila no ve nada ([]).
    """
    if not correo:
        return []
    correo = correo.strip().lower()
    administradores = {c.lower() for c in reglas.get("acceso", {}).get("administradores", [])}
    if correo in administradores:
        return None
    paises: set[str] = set()
    for rol, correos in reglas.get("miembros", {}).items():
        if correo in {c.lower() for c in correos}:
            paises |= set(reglas.get("roles", {}).get(rol, []))
    usuarios = {c.lower(): lista for c, lista in reglas.get("usuarios", {}).items()}
    paises |= set(usuarios.get(correo, []))
    return sorted(paises)


def paises_de_opcion(opcion: str, reglas: dict) -> list[str] | None:
    """Países para una opción del selector "Ver como": 'todos', 'rol:X' o 'usuario:correo'."""
    if opcion == TODOS:
        return None
    tipo, _, nombre = opcion.partition(":")
    if tipo == "rol":
        return list(reglas.get("roles", {}).get(nombre, []))
    if tipo == "usuario":
        return list(reglas.get("usuarios", {}).get(nombre, []))
    return []  # opción desconocida: nada


def opciones_demo(reglas: dict) -> list[str]:
    return (
        [TODOS]
        + [f"rol:{rol}" for rol in reglas.get("roles", {})]
        + [f"usuario:{correo}" for correo in reglas.get("usuarios", {})]
    )


def etiqueta(opcion: str) -> str:
    if opcion == TODOS:
        return "Todos los países (sin restricción)"
    tipo, _, nombre = opcion.partition(":")
    return f"Rol {nombre}" if tipo == "rol" else f"Usuario {nombre}"


# ---------------------------------------------------------------------------
# Lectura de secretos e identidad
# ---------------------------------------------------------------------------

def secretos() -> dict:
    """Secretos como diccionario; vacío si no hay archivo de secretos."""
    try:
        return st.secrets.to_dict()
    except Exception:  # sin secrets.toml, st.secrets lanza un error al leerse
        return {}


def auth_configurada() -> bool:
    return "auth" in secretos()


def reglas() -> dict:
    """Reglas de los secretos; en modo demostración, las de ejemplo si faltan."""
    datos = secretos()
    if any(seccion in datos for seccion in ("roles", "usuarios", "miembros", "acceso")):
        return datos
    return {} if auth_configurada() else DEMO


def paises_permitidos() -> list[str] | None:
    """Países visibles para la sesión actual (y los deja en st.session_state)."""
    if auth_configurada():
        # Producción: solo st.user, que viene firmado por el proveedor de identidad
        permitidos = paises_de_correo(st.user.get("email"), reglas()) if st.user.get("is_logged_in", False) else []
    else:
        opcion = st.session_state.setdefault("ver_como", TODOS)
        if opcion not in opciones_demo(reglas()):  # no confiar en el valor del navegador
            opcion = TODOS
        permitidos = paises_de_opcion(opcion, reglas())
    st.session_state["paises_permitidos"] = permitidos
    return permitidos


def _al_cambiar_rol() -> None:
    # Los países elegidos antes pueden no estar permitidos con el nuevo rol
    st.session_state["paises_sel"] = []


def panel_acceso() -> None:
    """Controles de acceso para la barra lateral (los dibuja app.py)."""
    if auth_configurada():
        if st.user.get("is_logged_in", False):
            st.caption(f"Sesión iniciada como **{st.user.get('email')}**")
            if st.button("Cerrar sesión", icon=":material/logout:"):
                st.logout()
        else:
            st.caption("Inicia sesión para ver los datos que te corresponden.")
            if st.button("Iniciar sesión", icon=":material/login:", type="primary"):
                st.login()
        return
    st.session_state.setdefault("ver_como", TODOS)
    st.selectbox(
        "Ver como (solo demo)",
        opciones_demo(reglas()),
        format_func=etiqueta,
        key="ver_como",
        on_change=_al_cambiar_rol,
        help="Simula la seguridad por filas de un rol o un usuario. En producción, la identidad "
             "sale de st.login() y este selector no aparece.",
    )

"""Estilo común de la app de ventas: paleta, plantilla de Plotly y formatos (Módulo 49).

Los colores deben coincidir con el tema de Streamlit de `.streamlit/config.toml`
(en la raíz del repositorio). Si cambias uno, cambia el otro.

La paleta categórica es apta para daltonismo: el orden de los colores está
elegido para que los vecinos se distingan también con deuteranopía y protanopía.
Las tres categorías de producto usan siempre los tres primeros colores, en todas
las páginas y gráficos (el color sigue a la categoría, no a su posición).
"""

from __future__ import annotations

import plotly.graph_objects as go
import plotly.io as pio

# Superficies y texto (iguales que [theme] en config.toml)
FONDO = "#fcfcfb"
FONDO_SECUNDARIO = "#f1f0ed"
TEXTO = "#0b0b0b"
TEXTO_SECUNDARIO = "#52514e"
REJILLA = "#e4e3df"
PRIMARIO = "#2a78d6"

# Paleta categórica en orden fijo (azul, naranja, aguamarina, amarillo...)
PALETA = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]

# Escala secuencial de un solo tono (azul claro -> oscuro) para magnitudes
SECUENCIAL = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]

# Cada categoría conserva su color en todos los gráficos
COLORES_CATEGORIA = {
    "Technology": PALETA[0],
    "Furniture": PALETA[1],
    "Office Supplies": PALETA[2],
}

FUENTE = '"Source Sans 3", "Source Sans Pro", Helvetica, Arial, sans-serif'

PLANTILLA = go.layout.Template(
    layout=dict(
        font=dict(family=FUENTE, size=14, color=TEXTO),
        title=dict(font=dict(size=18, color=TEXTO), x=0, xanchor="left"),
        colorway=PALETA,
        colorscale=dict(sequential=SECUENCIAL),
        paper_bgcolor=FONDO,
        plot_bgcolor=FONDO,
        separators=". ",  # punto decimal y espacio como separador de miles
        margin=dict(l=10, r=10, t=50, b=10),
        hoverlabel=dict(font=dict(family=FUENTE, size=13)),
        legend=dict(orientation="h", y=-0.15, title_text=""),
        xaxis=dict(showgrid=False, linecolor=REJILLA, ticks="", title_font=dict(color=TEXTO_SECUNDARIO)),
        yaxis=dict(gridcolor=REJILLA, zeroline=False, title_font=dict(color=TEXTO_SECUNDARIO)),
        geo=dict(bgcolor=FONDO, landcolor=FONDO_SECUNDARIO, showcountries=True,
                 countrycolor="#ffffff", showframe=False, coastlinecolor=REJILLA),
    )
)
pio.templates["ventas"] = PLANTILLA


def usar_plantilla() -> None:
    """Hace de "plotly_white+ventas" la plantilla por defecto de Plotly Express."""
    pio.templates.default = "plotly_white+ventas"


usar_plantilla()


def ajustar(fig: go.Figure) -> go.Figure:
    """Fija los fondos en el propio gráfico.

    Streamlit pinta el área de trazado con su color secundario cuando el fondo
    solo viene de la plantilla; repetirlo en el layout del gráfico lo evita.
    """
    return fig.update_layout(plot_bgcolor=FONDO, paper_bgcolor=FONDO)


# ---------------------------------------------------------------------------
# Formatos de número (espacio como separador de miles, como en el resto de la sección)
# ---------------------------------------------------------------------------

def entero(valor) -> str:
    """1499000 -> '1 499 000'."""
    return f"{valor:,.0f}".replace(",", " ")


def millones(valor, decimales: int = 2) -> str:
    """41940958825 -> '41 940.96 M'."""
    return f"{valor / 1e6:,.{decimales}f} M".replace(",", " ")


def porcentaje(valor, decimales: int = 1) -> str:
    """0.2735 -> '27.4 %'."""
    return f"{valor * 100:.{decimales}f} %"


# ---------------------------------------------------------------------------
# Formato condicional para tablas (pandas Styler, sin depender de matplotlib)
# ---------------------------------------------------------------------------

def _hex_a_rgb(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))


def color_en_escala(fraccion: float, escala: list[str] = SECUENCIAL) -> str:
    """Interpola un color de la escala para una fracción entre 0 y 1."""
    fraccion = min(max(float(fraccion), 0.0), 1.0)
    posicion = fraccion * (len(escala) - 1)
    i = min(int(posicion), len(escala) - 2)
    t = posicion - i
    a, b = _hex_a_rgb(escala[i]), _hex_a_rgb(escala[i + 1])
    r, g, bl = (round(x + (y - x) * t) for x, y in zip(a, b))
    return f"#{r:02x}{g:02x}{bl:02x}"


def _luminancia(color: str) -> float:
    canales = []
    for c in _hex_a_rgb(color):
        c = c / 255
        canales.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = canales
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def fondo_degradado(columna, escala: list[str] = SECUENCIAL) -> list[str]:
    """Color de fondo según el valor, con texto blanco o negro según el contraste."""
    minimo, maximo = columna.min(), columna.max()
    rango = (maximo - minimo) or 1
    estilos = []
    for valor in columna:
        fondo = color_en_escala((valor - minimo) / rango, escala)
        texto = "#ffffff" if _luminancia(fondo) < 0.35 else TEXTO
        estilos.append(f"background-color: {fondo}; color: {texto}")
    return estilos


def texto_degradado(columna, escala: list[str] = SECUENCIAL[2:]) -> list[str]:
    """Color de fuente según el valor (desde la mitad de la escala, para que se lea)."""
    minimo, maximo = columna.min(), columna.max()
    rango = (maximo - minimo) or 1
    return [f"color: {color_en_escala((v - minimo) / rango, escala)}; font-weight: 600" for v in columna]

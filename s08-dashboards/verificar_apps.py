"""Prueba de humo de todas las apps de Streamlit del repositorio (S08 y P05).

Ejecuta cada app sin navegador con AppTest y comprueba que no lanza excepciones
y que dibuja sus métricas. En la app final recorre las cinco páginas y prueba la
seguridad por filas con "Ver como" el rol NAFTA.

    uv run python s08-dashboards/verificar_apps.py
"""

from pathlib import Path

from streamlit.testing.v1 import AppTest

RAIZ = Path(__file__).resolve().parents[1]
SECCION = RAIZ / "s08-dashboards"
TIEMPO = 120

APPS = [
    SECCION / "m46-formato-condicional" / "m46-formato-condicional-app.py",
    SECCION / "m47-medidas-y-kpis" / "m47-medidas-y-kpis-app.py",
    SECCION / "m48-interactividad" / "m48-interactividad-app.py",
    RAIZ / "proyectos" / "p05-dashboard-covid" / "p05-dashboard-covid-app.py",
]
APP_FINAL = SECCION / "practica-ventas" / "app.py"
PAGINAS = ["paginas/inicio.py", "paginas/resumen.py", "paginas/medidas.py", "paginas/analisis.py", "paginas/acerca.py"]
NAFTA = ["CANADA", "MEXICO", "US"]


def revisar(at: AppTest, nombre: str) -> None:
    assert not at.exception, f"{nombre}: {at.exception}"
    print(f"ok  {nombre}: {len(at.metric)} métricas, {len(at.dataframe)} tablas")


def main() -> None:
    for app in APPS:
        at = AppTest.from_file(str(app), default_timeout=TIEMPO).run()
        revisar(at, app.relative_to(RAIZ).as_posix())
        assert at.metric, f"{app.name}: no dibujó métricas"

    at = AppTest.from_file(str(APP_FINAL), default_timeout=TIEMPO).run()
    revisar(at, "practica-ventas/app.py")
    for pagina in PAGINAS:
        at.switch_page(pagina).run()
        revisar(at, f"practica-ventas/{pagina}")

    # Seguridad por filas en modo demostración: el rol NAFTA solo ve tres países
    at.switch_page("paginas/resumen.py").run()
    at.selectbox(key="ver_como").select("rol:NAFTA").run()
    revisar(at, "practica-ventas/paginas/resumen.py como NAFTA")
    permitidos = sorted(at.session_state["paises_permitidos"])
    assert permitidos == NAFTA, permitidos
    print("ok  Ver como NAFTA:", ", ".join(permitidos))
    print("Todas las apps funcionan.")


if __name__ == "__main__":
    main()

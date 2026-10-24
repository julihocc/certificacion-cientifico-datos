"""Genera datos-modelo/*.parquet a partir de los archivos originales de datos-ventas/.

Las apps de Streamlit y los notebooks leen el modelo desde Parquet: es más rápido
que repetir la limpieza y los archivos son lo bastante pequeños para no necesitar
Git LFS. Hay que volver a ejecutarlo si cambia la limpieza en ventas.py.

    uv run python s08-dashboards/practica-ventas/preparar_datos.py
"""

from ventas import FILAS_VENTAS, MODELO, VENTAS_TOTALES, conectar, guardar_modelo

if __name__ == "__main__":
    rutas = guardar_modelo()
    for nombre, ruta in rutas.items():
        print(f"{ruta.relative_to(MODELO.parent)}: {ruta.stat().st_size / 1e6:.2f} MB")

    filas, total = conectar("parquet").execute(
        "SELECT count(*), CAST(sum(importe) AS BIGINT) FROM ventas_detalle"
    ).fetchone()
    assert (filas, total) == (FILAS_VENTAS, VENTAS_TOTALES), (filas, total)
    print(f"Comprobado: {filas:,} ventas por {total:,}".replace(",", " "))

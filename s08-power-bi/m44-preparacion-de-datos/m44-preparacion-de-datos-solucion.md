# Módulo 44: Preparación de datos — Solución

- Author: Juliho David Castillo Colmenares

Enunciado para estudiantes: [m44-preparacion-de-datos-guia.ipynb](m44-preparacion-de-datos-guia.ipynb) · Lección: [m44-preparacion-de-datos-leccion.md](m44-preparacion-de-datos-leccion.md)

*Título original del ejercicio en el curso: `# Module 45: Prepare your data` (la numeración del curso iba una unidad por delante de la del repositorio).*

## Contexto

Una cadena de tiendas con presencia en diez países quiere un tablero de ventas en Power BI. El extracto que entrega sistemas trae las ventas de 2019 en un CSV, las de 2020 y 2021 en una carpeta con un archivo por año, los países en un TXT sin encabezado y los catálogos de clientes, tiendas y productos en un libro de Excel, con encabezados ausentes, duplicados, filas basura y campos empaquetados. Toda la limpieza se hace en Power Query, para que se repita sola al actualizar.

## Datos

Archivos en `../practica-ventas/datos-ventas/`: `ventas-2019.csv`, `ventas-por-anio/ventas-2020.csv` y `ventas-por-anio/ventas-2021.csv` (columnas `ID_T`, `ID_Country`, `Date`, `ID_Store`, `ID_Client`, `ID_Product`, `Quantity`, `Price`); `paises.txt` (separado por `|`, sin encabezado y con duplicados), y `catalogo.xlsx`, con las hojas `t_customer`, `t_store` y `t_product`.

## Instrucciones

1. **Países.** Importar `paises.txt` con delimitador `|`, nombrar las columnas `ID_Country` y `Country` y quitar duplicados.
2. **Clientes.** Dividir el campo empaquetado `ID_Client` de `t_customer`, quitar las filas vacías y el pie, y las columnas sin información.
3. **Productos.** Extraer la clave numérica `ID_Product` de `Product ID` y conservar solo los productos activos.
4. **Tiendas.** Quitar las filas previas al encabezado de `t_store`, dejar una fila por tienda (la versión `Open`) y normalizar `Format`.
5. **Ventas de 2019.** Importar el CSV, asignar tipos y quitar `ID_T`.
6. **Ventas de 2020 y 2021 desde una carpeta.** Importar `ventas-por-anio/` con el conector Carpeta, leer solo las ocho columnas reales y aplicar los mismos tipos.
7. **Tabla de ventas única.** Anexar las dos consultas de ventas en `Sales` y agregar la columna `Sales` = `Quantity` × `Price`.

*El enunciado original del curso no se conserva; estas instrucciones se reconstruyeron a partir de la solución.*

### Tarea 1. Países

![t_countries](captura-01.png)

### Tarea 2. Clientes

![t_costumer](captura-02.png)

### Tarea 3. Productos

![t_product](captura-03.png)

### Tarea 4. Tiendas

![t_store](captura-04.png)

### Tarea 5. Ventas de 2019

![Sales 2019](captura-05.png)

### Tarea 6. Ventas de 2020 y 2021 desde una carpeta

![Sales 2020-2021](captura-06.png)

### Tarea 7. Tabla de ventas única

![Sales](captura-07.png)
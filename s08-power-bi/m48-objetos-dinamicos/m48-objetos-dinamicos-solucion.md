# Módulo 48: Objetos dinámicos — Solución

Author: Juliho Castillo Colmenares

Enunciado para estudiantes: [m48-objetos-dinamicos-guia.ipynb](m48-objetos-dinamicos-guia.ipynb) · Lección: [m48-objetos-dinamicos-leccion.md](m48-objetos-dinamicos-leccion.md)

*Título original del ejercicio en el curso: `# Module 49: Dynamic Objects` (la numeración del curso iba una unidad por delante de la del repositorio).*

## Contexto

Los gerentes de la cadena de tiendas quieren hacer sus propias preguntas sobre el informe de ventas: acotar el análisis a un periodo, ver la evolución de un país al pasar el cursor por el mapa y abrir el detalle de los productos vendidos en ese país. Para eso se añade una página de análisis con un segmentador de fechas, una página de información sobre herramientas y una página de obtención de detalles.

## Instrucciones

1. **Página de análisis** con un mapa de `SalesAvg` por `Country` y un mapa de árbol de `SalesValue` por `Sub-Category`.
2. **Segmentador de fechas** sobre `Sales[Date]` en estilo Entre.
3. **Información sobre herramientas:** página `mini-viz` de tipo información sobre herramientas, asignada al mapa.
4. **Obtención de detalles:** página `drill-through` con una tabla por país, categoría, subcategoría y producto con `SalesAvg`, y `Country` como campo de obtención de detalles.

*El enunciado original del curso no se conserva; estas instrucciones se reconstruyeron a partir de la solución.*

### Tarea 3. Información sobre herramientas

La captura muestra la página de análisis (Tarea 1) con el segmentador de fechas (Tarea 2) y la mini visualización que aparece al pasar el cursor por un país del mapa.

![mini-viz](captura-01.png) 

### Tarea 4. Obtención de detalles

![drill-through](captura-02.png)
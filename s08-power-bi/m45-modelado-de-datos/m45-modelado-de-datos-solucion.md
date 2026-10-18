# Módulo 45: Modelado de datos — Solución

Author: Juliho Castillo Colmenares

Enunciado para estudiantes: [m45-modelado-de-datos-guia.ipynb](m45-modelado-de-datos-guia.ipynb) · Lección: [m45-modelado-de-datos-leccion.md](m45-modelado-de-datos-leccion.md)

*Título original del ejercicio en el curso: `# Module 46: Data Modelling` (la numeración del curso iba una unidad por delante de la del repositorio).*

## Contexto

Una cadena de tiendas con presencia en diez países tiene sus ventas de 2019 a 2021 (`Sales`) y sus catálogos de países, clientes, productos y tiendas cargados y limpios en Power BI (Módulo 44). Para que un filtro sobre cualquiera de esos catálogos llegue a las ventas en un solo salto, hay que relacionar las tablas en un **modelo estrella**.

## Instrucciones

1. **Crear las relaciones del modelo estrella.** Comprobar que las claves de las dimensiones son únicas y del mismo tipo que en `Sales`, y relacionar `Sales` con `t_countries`, `t_customer`, `t_product` y `t_store` por `ID_Country`, `ID_Client`, `ID_Product` e `ID_Store`: varios a uno, activas y con filtro en una sola dirección.
2. **Documentar el modelo** con una captura de la vista de modelo que muestre la estrella completa.

*El enunciado original del curso no se conserva; estas instrucciones se reconstruyeron a partir de la solución.*

### Tarea 2. Documentar el modelo

La vista de modelo muestra `Sales_jcc` en el centro, relacionada con las cuatro dimensiones (Tarea 1).

![data-model](captura-01.png)
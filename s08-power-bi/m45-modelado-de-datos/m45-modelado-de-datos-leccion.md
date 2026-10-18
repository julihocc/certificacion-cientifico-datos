# Módulo 45: Modelado de datos

Autor: Juliho Castillo Colmenares

> Lección complementaria del ejercicio [m45-modelado-de-datos.md](m45-modelado-de-datos.md). No es una tarea entregada del programa.

En el Módulo 44 dejamos limpias cinco tablas: las ventas y cuatro catálogos. Por separado no responden preguntas como "¿cuánto vendió cada categoría en Canadá?". Para eso hay que **relacionarlas**, y la forma de hacerlo determina si los totales salen bien, si los filtros se propagan como esperamos y si el informe es rápido. Esta lección explica cómo diseñar ese modelo.

1. Tablas de hechos y dimensiones
2. Esquema estrella y copo de nieve
3. Claves y cardinalidad
4. Dirección del filtro cruzado
5. Relaciones activas e inactivas
6. Tabla de medidas y campos ocultos
7. Errores frecuentes
8. Ejercicio

## 1. Tablas de hechos y dimensiones

Un modelo analítico distingue dos tipos de tabla:

| Tipo | Qué guarda | Forma | En los datos de ventas |
| --- | --- | --- | --- |
| **Hechos** (fact) | Eventos medibles: cada venta, cada visita | Muchas filas, columnas numéricas y claves | `Sales`: 1 499 000 filas con `Quantity`, `Price`, `Sales` y cinco claves |
| **Dimensión** (dimension) | Descripciones de las entidades | Pocas filas, columnas de texto | `t_countries` (10), `t_store` (200), `t_customer` (950), `t_product` (1000) |

Las dimensiones responden al "por qué" de un análisis (por país, por categoría, por tienda) y la tabla de hechos aporta el "cuánto". En un visual, las columnas de las dimensiones van a los ejes y a los segmentadores; las columnas numéricas de la tabla de hechos se agregan.

## 2. Esquema estrella y copo de nieve

En un **esquema estrella** (star schema) la tabla de hechos está en el centro y cada dimensión se relaciona directamente con ella. Es el diseño que Power BI maneja mejor: las relaciones son cortas y los filtros llegan a los hechos en un solo salto.

```text
              t_countries
                   │ 1
                   │
 t_customer 1 ── * Sales * ── 1 t_product
                   │ *
                   │
                   │ 1
                t_store
```

En un **copo de nieve** (snowflake) las dimensiones se normalizan en varias tablas encadenadas. Por ejemplo, separar las categorías de los productos:

```text
Sales * ── 1 t_product * ── 1 t_subcategory * ── 1 t_category
```

| | Estrella | Copo de nieve |
| --- | --- | --- |
| Número de tablas | Menos | Más |
| Repetición de texto | Algo en las dimensiones | Mínima |
| Saltos para filtrar los hechos | Uno | Varios |
| Facilidad para quien crea informes | Alta | Menor (más tablas en el panel Datos) |
| Recomendación en Power BI | Preferido | Aplanar en Power Query cuando se pueda |

En `t_product` las columnas `Category` y `Sub-Category` ya vienen dentro de la tabla de productos: es una dimensión estrella. Repetir "Furniture" en cientos de filas cuesta muy poco frente a la simplicidad que se gana.

![Vista de modelo con las relaciones de la tabla de ventas](captura-01.png)

## 3. Claves y cardinalidad

Una relación une una columna de una tabla con una columna de otra, en la **Vista de modelo** arrastrando un campo sobre otro o desde **Inicio → Administrar relaciones** (Manage relationships). La **cardinalidad** describe cuántas filas de cada lado pueden coincidir:

| Cardinalidad | Significado | Ejemplo | Uso |
| --- | --- | --- | --- |
| **Uno a varios** (1:\*) | Cada valor aparece una vez en un lado y muchas en el otro | `t_countries[ID_Country]` → `Sales[ID_Country]` | La relación normal entre dimensión y hechos |
| **Uno a uno** (1:1) | Cada valor aparece una vez en ambos lados | `t_customer` y una tabla de datos fiscales por cliente | Suele indicar que las dos tablas deberían ser una |
| **Varios a varios** (\*:\*) | Los valores se repiten en ambos lados | Una tabla de presupuesto por categoría y mes frente a `t_product` | Casos especiales; con cuidado |

Para que Power BI acepte el lado "uno", la columna debe tener **valores únicos y sin vacíos**. Por eso en el Módulo 44 fue necesario dejar una sola fila por tienda en `t_store` y un solo producto activo en `t_product`: con duplicados, el lado "uno" no existe.

En el diagrama, el lado uno se marca con `1` y el lado varios con `*`. El sentido de la flecha en el centro de la línea indica hacia dónde fluyen los filtros.

## 4. Dirección del filtro cruzado

Cada relación tiene una **dirección de filtro cruzado** (cross filter direction):

- **Única** (Single): el filtro viaja de la dimensión a los hechos. Al elegir "CANADA" en un segmentador de `t_countries`, `Sales` se reduce a las ventas de Canadá.
- **Ambas** (Both): el filtro también vuelve de los hechos a la dimensión. Al filtrar `t_product` por "Furniture", `t_countries` se reduce a los países que vendieron muebles.

La dirección única es la opción por defecto y la recomendada. "Ambas" parece cómoda porque un segmentador de países "sabe" qué países tienen ventas, pero tiene costos:

| Riesgo | Por qué ocurre |
| --- | --- |
| **Ambigüedad** | Con varias relaciones bidireccionales puede haber dos caminos entre dos tablas, y Power BI no sabe cuál usar (o desactiva una relación) |
| **Resultados inesperados** | Un filtro sobre clientes se propaga a productos a través de las ventas, y los totales de una dimensión cambian sin que el usuario lo note |
| **Rendimiento** | Cada filtro tiene que recorrer más tablas |

Si un caso concreto necesita el filtro en ambos sentidos, es preferible activarlo solo dentro de una medida con `CROSSFILTER`, en lugar de dejarlo fijo en el modelo:

```dax
Productos con ventas =
CALCULATE (
    DISTINCTCOUNT ( t_product[ID_Product] ),
    CROSSFILTER ( Sales[ID_Product], t_product[ID_Product], BOTH )
)
```

## 5. Relaciones activas e inactivas

Entre dos tablas solo puede haber **una relación activa** (línea continua). Si se crea una segunda, queda **inactiva** (línea discontinua) y no filtra nada por sí sola.

El caso típico son dos fechas. La tabla de ventas de la práctica tiene una sola fecha (`Date`), pero supongamos que se añadiera una fecha de envío `ShipDate`. Ambas columnas se relacionarían con la misma tabla de calendario (Módulo 47): `Date` de forma activa y `ShipDate` de forma inactiva. Una medida activa la segunda relación solo durante su cálculo con `USERELATIONSHIP`:

```dax
Ventas por fecha de envío =
CALCULATE (
    SUM ( Sales[Sales] ),
    USERELATIONSHIP ( Sales[ShipDate], Calendario[Date] )
)
```

| Mes (Calendario) | Ventas (por fecha de pedido) | Ventas por fecha de envío |
| --- | --- | --- |
| Enero | Pedidos hechos en enero | Pedidos enviados en enero |
| Febrero | Pedidos hechos en febrero | Pedidos enviados en febrero |

Así un mismo eje de calendario sirve para las dos preguntas sin duplicar la tabla de fechas.

## 6. Tabla de medidas y campos ocultos

Cuando un modelo crece, las medidas quedan dispersas entre las tablas. Una práctica común es crear una **tabla de medidas**: una tabla vacía que solo sirve de carpeta.

1. **Inicio → Especificar datos** (Enter data), sin escribir filas, con un nombre como `_Medidas`.
2. Crear las medidas en ella, o mover las existentes cambiando su **Tabla principal** (Home table) en el panel de propiedades.
3. Ocultar la columna vacía que crea la tabla. Power BI muestra entonces la tabla con un icono de calculadora y la coloca arriba en el panel **Datos**.

El otro hábito es **ocultar las claves técnicas**. A quien construye un visual no le sirve `Sales[ID_Product]`: debe usar `t_product[Product Name]`. Clic derecho → **Ocultar en la vista de informe** (Hide in report view) sobre:

| Tabla | Campos que conviene ocultar |
| --- | --- |
| `Sales` | `ID_T`, `ID_Country`, `ID_Store`, `ID_Client`, `ID_Product`, y las columnas numéricas que solo se usan a través de medidas |
| Dimensiones | Las claves `ID_*` cuando ya hay un nombre descriptivo |

Ocultar no borra: el campo sigue disponible para relaciones y fórmulas DAX.

## 7. Errores frecuentes

**Claves duplicadas en la dimensión.** Si `t_store` conserva las dos filas de la tienda 17 (una `Open` y otra `Closed`), la relación con `Sales[ID_Store]` no puede ser uno a varios. Power BI propone varios a varios, y cada venta de la tienda 17 se asocia a dos filas de tienda. La forma correcta es arreglar la clave en Power Query, no cambiar la cardinalidad:

| ID_Store | Name_Store | Status |
| --- | --- | --- |
| 17 | Rippin LLC | Open |
| ~~17~~ | ~~Rippin LLC~~ | ~~Closed~~ |

**Relacionar columnas de distinto tipo.** Si `t_product[ID_Product]` quedó como texto (`"1000"`) y `Sales[ID_Product]` como entero, Power BI no permite crear la relación o no encuentra coincidencias. Ambas claves deben tener el mismo tipo desde Power Query.

**Valores de la tabla de hechos sin pareja en la dimensión.** Si una venta tiene un `ID_Client` que no existe en `t_customer`, sus importes aparecen bajo una categoría **(En blanco)** (Blank) en cualquier visual por cliente. No es un error del visual: es un problema de integridad referencial que se resuelve completando la dimensión.

**Relacionar dos tablas de hechos entre sí.** Si el modelo tuviera una tabla de devoluciones, unirla con `Sales` por `ID_Product` crearía una relación varios a varios que no tiene sentido analítico: un producto aparece en miles de ventas y en decenas de devoluciones. Las dos tablas de hechos se conectan a través de las dimensiones comunes (`t_product`, `Calendario`), y cada una se relaciona con ellas por separado.

**Activar "Ambas" para que un segmentador muestre solo valores con datos.** Es más seguro dejar la relación en una dirección y filtrar el segmentador con un filtro de nivel de objeto visual (por ejemplo, `Sales` no está en blanco).

## 8. Ejercicio

Una cadena de librerías entrega estas tablas:

| Tabla | Columnas | Filas |
| --- | --- | --- |
| `Pedidos` | `ID_Pedido`, `FechaPedido`, `FechaEntrega`, `ID_Libro`, `ID_Sucursal`, `Unidades`, `Importe` | 250 000 |
| `Libros` | `ID_Libro`, `Titulo`, `ID_Genero` | 4 000 |
| `Generos` | `ID_Genero`, `Genero` | 25 |
| `Sucursales` | `ID_Sucursal`, `Ciudad`, `Region` | 40 (dos sucursales aparecen dos veces por un cambio de dirección) |
| `Calendario` | `Date`, `Año`, `Mes` | 1 096 |

1. Clasifica cada tabla como hechos o dimensión.
2. El modelo propuesto es un copo de nieve. Indica qué cambiarías para convertirlo en estrella.
3. Escribe cada relación con su cardinalidad y su dirección de filtro.
4. ¿Qué problema impide crear la relación con `Sucursales` y cómo se resuelve?
5. Escribe una medida que sume `Importe` por fecha de entrega.
6. Lista los campos que ocultarías en la vista de informe.

### Solución

1. `Pedidos` es la tabla de hechos. `Libros`, `Generos`, `Sucursales` y `Calendario` son dimensiones.
2. `Generos` cuelga de `Libros`: es un copo de nieve. En Power Query se combina `Generos` dentro de `Libros` (combinar consultas por `ID_Genero`, expandir `Genero`) y se deshabilita la carga de `Generos`.
3. Relaciones del modelo estrella:

| Desde (lado varios) | Hacia (lado uno) | Cardinalidad | Filtro | Estado |
| --- | --- | --- | --- | --- |
| `Pedidos[ID_Libro]` | `Libros[ID_Libro]` | \*:1 | Única | Activa |
| `Pedidos[ID_Sucursal]` | `Sucursales[ID_Sucursal]` | \*:1 | Única | Activa |
| `Pedidos[FechaPedido]` | `Calendario[Date]` | \*:1 | Única | Activa |
| `Pedidos[FechaEntrega]` | `Calendario[Date]` | \*:1 | Única | Inactiva |

4. `Sucursales[ID_Sucursal]` no es única. Hay que decidir qué fila representa a cada sucursal (por ejemplo, la dirección vigente) y dejar una sola en Power Query, con `Table.Distinct` sobre la clave después de ordenar o con un filtro por la fila vigente.
5. Medida con la relación inactiva:

```dax
Importe por fecha de entrega =
CALCULATE (
    SUM ( Pedidos[Importe] ),
    USERELATIONSHIP ( Pedidos[FechaEntrega], Calendario[Date] )
)
```

6. Se ocultan `Pedidos[ID_Pedido]`, `Pedidos[ID_Libro]`, `Pedidos[ID_Sucursal]`, `Pedidos[FechaPedido]`, `Pedidos[FechaEntrega]` (las fechas se usan desde `Calendario`), `Libros[ID_Libro]`, `Libros[ID_Genero]` y `Sucursales[ID_Sucursal]`. `Unidades` e `Importe` también pueden ocultarse si existen medidas que las sumen.

## Resumen

- La tabla de hechos guarda eventos medibles y las dimensiones los describen; los visuales agrupan por dimensiones y agregan hechos.
- El esquema estrella, con cada dimensión unida directamente a los hechos, es el diseño preferido en Power BI.
- La relación habitual es uno a varios, y exige claves únicas y del mismo tipo en el lado uno.
- La dirección de filtro única evita ambigüedades; "Ambas" se reserva para casos concretos, mejor dentro de una medida con `CROSSFILTER`.
- Solo una relación entre dos tablas puede estar activa; `USERELATIONSHIP` activa otra durante un cálculo.
- Una tabla de medidas y las claves ocultas hacen el modelo más fácil de usar.

En el **Módulo 46** se construyen los primeros visuales sobre este modelo y se resalta la información con formato condicional.

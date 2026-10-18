# Módulo 47: DAX

Autor: Juliho Castillo Colmenares

> Lección complementaria del ejercicio de este módulo: [enunciado](m47-dax-guia.ipynb) y [solución](m47-dax-solucion.pdf). No es una tarea entregada del programa.

Arrastrar un campo numérico a un visual produce una suma automática. Pero las preguntas de negocio rara vez son una suma: "¿cuánto crecimos frente al mismo mes del año pasado?", "¿qué parte del total aporta cada país?", "¿cuánto llevamos vendido en el año?". Para responderlas Power BI usa **DAX** (Data Analysis Expressions), un lenguaje de fórmulas que trabaja sobre el modelo. Esta lección presenta las ideas que hacen falta para escribir DAX correcto, con resultados calculados sobre las ventas reales de la práctica (`Sales`, 1 499 000 filas de 2019 a 2021).

1. Medidas y columnas calculadas
2. Contexto de fila y contexto de filtro
3. `SUM` frente a `SUMX`
4. `CALCULATE`
5. `DIVIDE` y variables
6. La tabla de calendario
7. Inteligencia de tiempo
8. Variación mensual y anual
9. Errores frecuentes
10. Ejercicio

## 1. Medidas y columnas calculadas

DAX se escribe en dos lugares distintos, y la diferencia importa:

| | Columna calculada | Medida |
| --- | --- | --- |
| Se crea con | **Herramientas de tabla → Nueva columna** | **Inicio → Nueva medida** |
| Se calcula | Al cargar o actualizar los datos, una vez por fila | Al mostrar un visual, una vez por celda |
| Se guarda | En el modelo, ocupando memoria | No se guarda: solo la fórmula |
| Contexto | De fila | De filtro |
| Uso típico | Ejes, segmentadores, filtros, claves | Valores agregados: totales, promedios, variaciones |

Una columna calculada que clasifica cada venta por su tamaño:

```dax
Tamaño de venta =
IF ( Sales[Sales] >= 100000, "Grande", "Normal" )
```

La columna aparece en la tabla `Sales` con un valor por fila y puede usarse en un segmentador. Una medida que suma las ventas:

```dax
Ventas = SUM ( Sales[Sales] )
```

La medida no tiene valor propio: en una tarjeta da el total; en una tabla por año da un número distinto en cada fila.

| Año | Ventas |
| --- | --- |
| 2019 | 14 028 184 223 |
| 2020 | 4 574 028 172 |
| 2021 | 23 338 746 430 |
| **Total** | **41 940 958 825** |

La regla práctica: si el resultado tiene que **filtrar o agrupar**, es una columna; si tiene que **agregarse** y responder a los filtros del informe, es una medida. Ante la duda, medida: no ocupa memoria y se adapta a cualquier visual.

## 2. Contexto de fila y contexto de filtro

Toda fórmula DAX se evalúa dentro de un **contexto**:

- El **contexto de fila** (row context) existe cuando DAX recorre una tabla fila a fila. En una columna calculada, `Sales[Sales]` significa "el valor de esta fila".
- El **contexto de filtro** (filter context) es el conjunto de filtros activos al evaluar una medida: la fila de la tabla del visual, los segmentadores, los filtros de página y los de las relaciones.

Cuando la tabla del visual muestra la fila "2020", la medida `Ventas` se evalúa con el filtro `Año = 2020`. Ese filtro viaja por la relación de `Calendario` a `Sales` y `SUM` solo ve las 499 000 ventas de 2020. Si además un segmentador selecciona "CANADA", el contexto tiene dos filtros y el resultado es 856 197 372.

Una medida **no tiene contexto de fila** por sí sola. Por eso esta medida falla:

```dax
-- Error: no se puede determinar un único valor para la columna Quantity
Importe mal = Sales[Quantity] * Sales[Price]
```

Dentro de una medida, una columna solo puede aparecer dentro de una función que la agregue (`SUM`, `MAX`...) o dentro de un iterador que cree el contexto de fila.

## 3. `SUM` frente a `SUMX`

`SUM` suma una columna. `SUMX` es un **iterador**: recorre una tabla, evalúa una expresión en cada fila (con contexto de fila) y suma los resultados.

```dax
Ventas SUM = SUM ( Sales[Sales] )

Ventas SUMX = SUMX ( Sales, Sales[Quantity] * Sales[Price] )
```

Las dos dan 41 940 958 825, porque la columna `Sales` es justamente `Quantity * Price`. Con `SUMX` la columna intermedia no hace falta: el producto se calcula al vuelo. Cada función de agregación tiene su versión iteradora: `AVERAGEX`, `MINX`, `MAXX`, `COUNTX`.

La diferencia aparece cuando se intenta multiplicar agregados:

| Medida | Fórmula | Resultado |
| --- | --- | --- |
| Correcta | `SUMX ( Sales, Sales[Quantity] * Sales[Price] )` | 41 940 958 825 |
| Incorrecta | `SUM ( Sales[Quantity] ) * AVERAGE ( Sales[Price] )` | 39 157 948 916 |

La segunda subestima las ventas en un 6.6 %: el precio promedio de todas las filas no pondera por cantidad. La suma de productos no es el producto de sumas.

Lo mismo pasa con los promedios. `AVERAGE ( Sales[Sales] )` da el importe medio por venta (27 979.29), mientras que `AVERAGE ( Sales[Quantity] ) * AVERAGE ( Sales[Price] )` da 26 122.71. Solo la primera responde a "¿cuánto vale una venta típica?".

## 4. `CALCULATE`

`CALCULATE` es la función central de DAX: evalúa una expresión en un **contexto de filtro modificado**.

```dax
CALCULATE ( <expresión>, <filtro1>, <filtro2>, ... )
```

Cada argumento de filtro **reemplaza** el filtro existente sobre esa columna. Por ejemplo:

```dax
Ventas Furniture =
CALCULATE ( [Ventas], t_product[Category] = "Furniture" )

Ventas todos los países =
CALCULATE ( [Ventas], ALL ( t_countries ) )

Participación país =
DIVIDE ( [Ventas], [Ventas todos los países] )
```

En una tabla por categoría, `Ventas Furniture` repite el mismo número en todas las filas, porque su filtro sustituye al de la fila:

| Category | Ventas | Ventas Furniture |
| --- | --- | --- |
| Furniture | 15 750 407 426 | 15 750 407 426 |
| Office Supplies | 8 553 767 974 | 15 750 407 426 |
| Technology | 17 636 783 425 | 15 750 407 426 |

Si se quiere **añadir** el filtro en lugar de reemplazarlo, se envuelve en `KEEPFILTERS`: `CALCULATE ( [Ventas], KEEPFILTERS ( t_product[Category] = "Furniture" ) )` devuelve 15 750 407 426 en la fila Furniture y nada en las otras dos.

`ALL ( t_countries )` quita todos los filtros de la tabla de países. Así el denominador de `Participación país` es siempre el total y cada país muestra su parte:

| Country | Ventas | Ventas todos los países | Participación país |
| --- | --- | --- | --- |
| FRANCE | 6 709 452 115 | 41 940 958 825 | 16.00 % |
| CANADA | 6 683 524 091 | 41 940 958 825 | 15.94 % |
| PERU | 2 348 842 532 | 41 940 958 825 | 5.60 % |

## 5. `DIVIDE` y variables

`DIVIDE ( numerador, denominador, alternativo )` divide y, si el denominador es cero o está en blanco, devuelve el valor alternativo (en blanco si se omite). El operador `/` en cambio devuelve infinito o un error, que en un visual aparece como `Infinity` o `NaN`.

Las **variables** (`VAR ... RETURN`) guardan un resultado intermedio con nombre. Hacen la fórmula más legible, evitan calcular dos veces lo mismo y facilitan depurar: basta con devolver una variable para ver su valor.

```dax
Ticket promedio =
VAR Importe = [Ventas]
VAR Transacciones = COUNTROWS ( Sales )
RETURN
    DIVIDE ( Importe, Transacciones )
```

| Año | Ventas | Transacciones | Ticket promedio |
| --- | --- | --- | --- |
| 2019 | 14 028 184 223 | 300 000 | 46 760.61 |
| 2020 | 4 574 028 172 | 499 000 | 9 166.39 |
| 2021 | 23 338 746 430 | 700 000 | 33 341.07 |
| **Total** | **41 940 958 825** | **1 499 000** | **27 979.29** |

Una variable se evalúa **una sola vez, en el contexto donde se define**. Si se define fuera de un `CALCULATE`, el `CALCULATE` posterior no la modifica.

## 6. La tabla de calendario

Las funciones de inteligencia de tiempo (`DATEADD`, `SAMEPERIODLASTYEAR`, `TOTALYTD`...) necesitan una columna de fechas **continua**: todos los días, sin huecos, desde el inicio del primer año hasta el final del último. La columna `Sales[Date]` no lo garantiza: un día sin ventas simplemente no aparece.

Power BI crea por defecto una tabla de fechas oculta para cada columna de fecha (la opción **Fecha y hora automáticas**, Auto date/time). Sirve para empezar, pero tiene límites: hay una tabla oculta por columna, no se puede compartir entre varias tablas de hechos y no admite columnas propias como el trimestre fiscal. Lo recomendable es crear una **tabla de calendario** propia con **Modelado → Nueva tabla**:

```dax
Calendario =
ADDCOLUMNS (
    CALENDAR ( DATE ( 2019, 1, 1 ), DATE ( 2021, 12, 31 ) ),
    "Año", YEAR ( [Date] ),
    "Mes", MONTH ( [Date] ),
    "Nombre del mes", FORMAT ( [Date], "mmm" ),
    "Año-Mes", FORMAT ( [Date], "yyyy-mm" ),
    "Trimestre", "T" & ROUNDUP ( MONTH ( [Date] ) / 3, 0 )
)
```

`CALENDAR` genera una tabla con una sola columna `Date`, un día por fila (1 096 filas: 2020 es bisiesto). `ADDCOLUMNS` le agrega columnas calculadas. `CALENDARAUTO ()` es la alternativa automática: busca la fecha mínima y máxima en todas las columnas de fecha del modelo y genera años completos.

| Date | Año | Mes | Nombre del mes | Año-Mes | Trimestre |
| --- | --- | --- | --- | --- | --- |
| 2019-01-01 | 2019 | 1 | ene | 2019-01 | T1 |
| 2019-01-02 | 2019 | 1 | ene | 2019-01 | T1 |
| ... | ... | ... | ... | ... | ... |
| 2021-12-31 | 2021 | 12 | dic | 2021-12 | T4 |

Después hay tres pasos:

1. **Marcar como tabla de fechas** (Mark as date table) en **Herramientas de tabla**, eligiendo la columna `Date`. Power BI comprueba que sea única, sin vacíos y continua.
2. Crear la relación `Calendario[Date]` (1) → `Sales[Date]` (\*), con filtro en una dirección.
3. Usar en los visuales las columnas de `Calendario` (Año, Mes...), no las de `Sales[Date]`.

## 7. Inteligencia de tiempo

Con el calendario marcado, las funciones de inteligencia de tiempo **desplazan** el contexto de fechas dentro de `CALCULATE`:

| Función | Qué devuelve | Ejemplo de uso |
| --- | --- | --- |
| `DATEADD ( fechas, n, intervalo )` | Las fechas desplazadas *n* días, meses, trimestres o años | Mes anterior: `-1, MONTH` |
| `SAMEPERIODLASTYEAR ( fechas )` | El mismo periodo un año antes | Comparación anual |
| `DATESYTD ( fechas )` | Del 1 de enero hasta la última fecha del contexto | Acumulado del año |
| `TOTALYTD ( expresión, fechas )` | Atajo de `CALCULATE ( expresión, DATESYTD ( fechas ) )` | Acumulado del año |

```dax
Ventas mes anterior =
CALCULATE ( [Ventas], DATEADD ( Calendario[Date], -1, MONTH ) )

Ventas año anterior =
CALCULATE ( [Ventas], SAMEPERIODLASTYEAR ( Calendario[Date] ) )

Ventas acumuladas del año =
TOTALYTD ( [Ventas], Calendario[Date] )

-- Equivalente con CALCULATE
Ventas acumuladas del año (2) =
CALCULATE ( [Ventas], DATESYTD ( Calendario[Date] ) )
```

Si el año fiscal no coincide con el natural, `TOTALYTD` y `DATESYTD` aceptan la fecha de cierre como argumento opcional, por ejemplo `TOTALYTD ( [Ventas], Calendario[Date], "6/30" )` para un año que termina el 30 de junio.

## 8. Variación mensual y anual

Las variaciones combinan lo anterior: el valor actual, el valor del periodo de referencia y `DIVIDE`.

```dax
Variación mensual =
VAR Actual = [Ventas]
VAR Anterior = [Ventas mes anterior]
RETURN
    DIVIDE ( Actual - Anterior, Anterior )

Variación anual =
VAR Actual = [Ventas]
VAR Anterior = [Ventas año anterior]
RETURN
    DIVIDE ( Actual - Anterior, Anterior )
```

Resultado en una tabla por `Calendario[Año-Mes]`, con las ventas reales:

| Año-Mes | Ventas | Mes anterior | Variación mensual | Año anterior | Variación anual | Acumulado del año |
| --- | --- | --- | --- | --- | --- | --- |
| 2019-01 | 1 055 072 666 | | | | | 1 055 072 666 |
| 2019-12 | 1 958 766 078 | 1 851 126 376 | 5.81 % | | | 14 028 184 223 |
| 2020-01 | 726 241 507 | 1 958 766 078 | −62.92 % | 1 055 072 666 | −31.17 % | 726 241 507 |
| 2020-02 | 666 901 056 | 726 241 507 | −8.17 % | 952 801 751 | −30.01 % | 1 393 142 563 |
| 2020-03 | 434 689 279 | 666 901 056 | −34.82 % | 1 931 341 497 | −77.49 % | 1 827 831 842 |
| 2021-01 | 4 368 191 234 | 438 915 318 | 895.22 % | 726 241 507 | 501.48 % | 4 368 191 234 |

Tres detalles a observar:

- En 2019-01 no hay mes anterior ni año anterior dentro del calendario. `DIVIDE` devuelve un blanco en lugar de un error.
- El acumulado del año se reinicia en enero: 2020-01 vuelve a empezar desde 726 241 507.
- `DATEADD` cruza el cambio de año sin problemas: el mes anterior a 2020-01 es 2019-12.

Las mismas medidas funcionan a nivel de año sin cambiar una línea. En una tabla por `Calendario[Año]`:

| Año | Ventas | Año anterior | Variación anual |
| --- | --- | --- | --- |
| 2019 | 14 028 184 223 | | |
| 2020 | 4 574 028 172 | 14 028 184 223 | −67.39 % |
| 2021 | 23 338 746 430 | 4 574 028 172 | 410.24 % |

Esa es la ventaja de las medidas: el contexto de filtro decide el periodo y la fórmula no necesita saber si está en un mes o en un año.

## 9. Errores frecuentes

**Usar una columna calculada para lo que debe ser una medida.** Una columna `Participación = Sales[Sales] / SUM ( Sales[Sales] )` calcula la participación de cada fila sobre el total general y queda fija: al filtrar por país no se recalcula. La participación debe ser una medida con `DIVIDE` y `ALL`, como en la sección 4.

**Dividir con `/` cuando el denominador puede estar vacío.** En el primer mes del calendario no hay mes anterior:

```dax
-- Incorrecto: en 2019-01 devuelve Infinity
Variación mensual mal = ( [Ventas] - [Ventas mes anterior] ) / [Ventas mes anterior]

-- Correcto: en 2019-01 devuelve un blanco
Variación mensual = DIVIDE ( [Ventas] - [Ventas mes anterior], [Ventas mes anterior] )
```

**Usar la fecha de la tabla de hechos en las funciones de tiempo.** `SAMEPERIODLASTYEAR ( Sales[Date] )` depende de que haya ventas todos los días. Si falta un día, el periodo comparable se recorta en silencio. Las funciones de tiempo deben recibir `Calendario[Date]`, y los visuales deben usar las columnas del calendario.

**Olvidar marcar la tabla de fechas o crear la relación.** Sin relación entre `Calendario` y `Sales`, todas las filas del visual muestran el total general. Sin marcarla, algunas funciones de tiempo dan resultados incorrectos cuando la relación usa una columna que no es de tipo fecha.

**Meses ordenados alfabéticamente.** La columna `Nombre del mes` es texto y se ordena "abr, ago, dic, ene...". Se corrige seleccionando la columna y usando **Ordenar por columna** (Sort by column) con `Mes`.

**Esperar que `CALCULATE` respete el filtro de la fila.** Un filtro dentro de `CALCULATE` sobre la misma columna que la fila del visual la **reemplaza**. Si se quiere la intersección, se usa `KEEPFILTERS`.

## 10. Ejercicio

Con el modelo de ventas y la tabla `Calendario` de la sección 6:

1. Crea la medida `Ventas trimestre anterior` con `DATEADD`.
2. Crea `Variación trimestral` con variables y `DIVIDE`.
3. Crea `Participación en el año`, que diga qué parte de las ventas del año aporta cada trimestre.
4. Crea `Ventas acumuladas del trimestre` con la función de acumulado trimestral de DAX.
5. Construye una tabla por `Año` y `Trimestre` y comprueba los resultados de 2020.

### Solución

```dax
Ventas trimestre anterior =
CALCULATE ( [Ventas], DATEADD ( Calendario[Date], -1, QUARTER ) )

Variación trimestral =
VAR Actual = [Ventas]
VAR Anterior = [Ventas trimestre anterior]
RETURN
    DIVIDE ( Actual - Anterior, Anterior )

Participación en el año =
VAR VentasAño =
    CALCULATE ( [Ventas], ALLEXCEPT ( Calendario, Calendario[Año] ) )
RETURN
    DIVIDE ( [Ventas], VentasAño )

Ventas acumuladas del trimestre =
TOTALQTD ( [Ventas], Calendario[Date] )
```

`ALLEXCEPT ( Calendario, Calendario[Año] )` quita los filtros de todas las columnas del calendario salvo el año: el denominador es el total del año de esa fila. `TOTALQTD` es el equivalente trimestral de `TOTALYTD`; en una fila de trimestre completo coincide con `Ventas`, y se diferencia en una tabla por mes.

Resultado esperado para 2020:

| Año | Trimestre | Ventas | Trimestre anterior | Variación trimestral | Participación en el año |
| --- | --- | --- | --- | --- | --- |
| 2020 | T1 | 1 827 831 842 | 5 747 580 818 | −68.20 % | 39.96 % |
| 2020 | T2 | 827 844 344 | 1 827 831 842 | −54.71 % | 18.10 % |
| 2020 | T3 | 608 272 193 | 827 844 344 | −26.52 % | 13.30 % |
| 2020 | T4 | 1 310 079 793 | 608 272 193 | 115.38 % | 28.64 % |
| **2020** | | **4 574 028 172** | | | **100.00 %** |

El trimestre anterior a 2020-T1 es 2019-T4 (5 747 580 818), y las cuatro participaciones suman 100 %. En 2021-T1 la variación trimestral es 682.32 % (10 248 999 518 frente a 1 310 079 793).

## Resumen

- Las columnas calculadas se evalúan por fila y se guardan; las medidas se evalúan en el contexto de filtro de cada celda y se adaptan a cualquier visual.
- Los iteradores como `SUMX` evalúan una expresión fila a fila; multiplicar agregados no equivale a agregar productos.
- `CALCULATE` modifica el contexto de filtro: sus filtros reemplazan los existentes, `ALL` los quita y `KEEPFILTERS` los combina.
- `DIVIDE` evita errores de división y las variables hacen las fórmulas legibles y eficientes.
- La inteligencia de tiempo requiere una tabla de calendario continua, relacionada y marcada como tabla de fechas; sobre ella, `DATEADD`, `SAMEPERIODLASTYEAR` y `TOTALYTD` resuelven comparaciones y acumulados.

En el **Módulo 48** se hacen los informes interactivos con segmentadores, obtención de detalles e información sobre herramientas.

# Módulo 46: Formato condicional

Autor: Juliho Castillo Colmenares

> Lección complementaria del ejercicio de este módulo: [enunciado](m46-formato-condicional-guia.ipynb) y [solución](m46-formato-condicional-solucion.pdf). No es una tarea entregada del programa.

Una tabla con diez países y cuatro métricas tiene cuarenta números. Nadie los lee todos: el lector busca el más alto, el más bajo o el que se sale de lo normal. El **formato condicional** (conditional formatting) colorea las celdas según su valor para que esa búsqueda la haga el ojo, no la cabeza. Bien usado, ahorra segundos en cada lectura; mal usado, convierte la tabla en un mosaico que distrae. Esta lección muestra las opciones de Power BI con los datos de ventas por país.

1. Para qué sirve: la atención preatentiva
2. Dónde se configura
3. Escalas de color
4. Reglas
5. Valor del campo: el color desde una medida DAX
6. Barras de datos e iconos
7. Accesibilidad
8. Errores frecuentes
9. Ejercicio

## 1. Para qué sirve: la atención preatentiva

El sistema visual detecta ciertos atributos **antes** de que pongamos atención consciente: el color, la intensidad, el tamaño, la posición o la orientación. Se llaman atributos **preatentivos**. Si en una columna de números grises uno es rojo, lo vemos en menos de un cuarto de segundo, sin recorrer la lista.

El formato condicional aprovecha ese mecanismo. Su objetivo no es decorar, sino responder una pregunta concreta:

| Pregunta del lector | Técnica adecuada |
| --- | --- |
| ¿Qué valores son altos y cuáles bajos? | Escala de color (degradado) |
| ¿Qué valores superan un umbral? | Reglas |
| ¿Cuál es la proporción entre valores? | Barras de datos |
| ¿Mejoró o empeoró? | Iconos o colores divergentes alrededor de cero |

Los datos de esta lección son las ventas totales por país de 2019 a 2021 (en millones):

| Country | Ventas (M) | % del total |
| --- | --- | --- |
| FRANCE | 6 709.5 | 16.00 % |
| CANADA | 6 683.5 | 15.94 % |
| US | 5 025.3 | 11.98 % |
| BRAZIL | 4 708.0 | 11.23 % |
| CHILE | 4 690.6 | 11.18 % |
| MEXICO | 4 655.6 | 11.10 % |
| PORTUGAL | 2 401.5 | 5.73 % |
| SPAIN | 2 360.7 | 5.63 % |
| COLOMBIA | 2 357.4 | 5.62 % |
| PERU | 2 348.8 | 5.60 % |

Sin color hay que leer las diez cifras para ver que forman tres grupos: dos países cerca de 6 700 M, cuatro entre 4 600 y 5 100 M, y cuatro cerca de 2 400 M. Con color, los grupos saltan a la vista.

## 2. Dónde se configura

El formato condicional se aplica sobre todo en los objetos visuales **Tabla** y **Matriz**, aunque varios gráficos admiten color condicional en barras o columnas. Hay dos caminos:

- En el panel **Visualizaciones → Formato del objeto visual → Elementos de celda** (Cell elements), elegir la serie y activar color de fondo, color de fuente, barras de datos o iconos.
- En el panel de campos del visual, clic derecho sobre un campo numérico → **Formato condicional**.

Cada opción abre un cuadro de diálogo con un **estilo de formato** (Format style) que puede ser **Degradado** (Gradient), **Reglas** (Rules) o **Valor del campo** (Field value), y con el campo en el que se basa el formato. Ese campo no tiene que ser el que se muestra: se puede colorear la columna de ventas según el margen, por ejemplo.

![Tabla por país con degradado y barras de datos](../practica-ventas/dashboard-ventas.png)

## 3. Escalas de color

Un **degradado de dos colores** asigna un color al mínimo y otro al máximo, e interpola entre ambos. Sirve para magnitudes que van de "poco" a "mucho", como las ventas: todos los valores son positivos y el interés está en el extremo alto.

Un **degradado de tres colores** añade un color central. Es la escala **divergente**, adecuada cuando hay un punto de referencia con significado: cero en una variación, la meta en un cumplimiento, el promedio en una comparación.

| Escala | Mínimo | Centro | Máximo | Ejemplo |
| --- | --- | --- | --- | --- |
| Secuencial (2 colores) | Azul muy claro | — | Azul oscuro | Ventas por país |
| Divergente (3 colores) | Naranja | Blanco en 0 | Azul | Variación anual de ventas |

En la escala secuencial aplicada a la tabla anterior, FRANCE y CANADA quedan en el tono más oscuro, PERU en el más claro, y los cuatro países del grupo intermedio en un tono medio. El ojo agrupa sin leer.

El mínimo y el máximo pueden ser los valores más bajo y más alto de la columna (opción por defecto) o **números fijos**. Con números fijos el color significa lo mismo aunque cambie el filtro del informe: si un segmentador deja solo tres países, el degradado automático vuelve a estirarse entre esos tres y un país mediocre parecerá el mejor.

## 4. Reglas

Con **Reglas** se definen intervalos y un color por intervalo: "si el valor es mayor o igual que *a* y menor que *b*, entonces este color". Es la opción adecuada cuando existen umbrales de negocio.

Para la tabla de países se pueden fijar tres niveles por participación en el total:

| Regla | Condición sobre `% del total` | Color | Países |
| --- | --- | --- | --- |
| Alto | ≥ 15 % | Azul oscuro | FRANCE, CANADA |
| Medio | ≥ 10 % y < 15 % | Azul claro | US, BRAZIL, CHILE, MEXICO |
| Bajo | < 10 % | Gris | PORTUGAL, SPAIN, COLOMBIA, PERU |

Las reglas pueden expresarse como **número** o como **porcentaje** del rango de valores. Conviene usar números: "15 %" del rango no es lo mismo que "15 % del total", y la diferencia confunde a quien mantiene el informe.

Los intervalos deben cubrir todos los valores sin huecos ni solapes. Si una regla termina en "< 10" y la siguiente empieza en "> 10", el valor 10 exacto se queda sin color.

## 5. Valor del campo: el color desde una medida DAX

El estilo **Valor del campo** toma el color de una columna o medida que devuelve un código de color como texto (`"#1F77B4"`) o un nombre de color. Es la opción más flexible: la lógica vive en DAX, se puede reutilizar en varios visuales y puede depender de otras medidas.

```dax
Ventas = SUM ( Sales[Sales] )

Participación =
DIVIDE ( [Ventas], CALCULATE ( [Ventas], ALL ( t_countries ) ) )

Color participación =
VAR p = [Participación]
RETURN
    SWITCH (
        TRUE (),
        ISBLANK ( p ), BLANK (),
        p >= 0.15, "#08519C",    -- azul oscuro
        p >= 0.10, "#6BAED6",    -- azul claro
        "#BDBDBD"                -- gris
    )
```

`SWITCH ( TRUE (), ... )` evalúa las condiciones en orden y devuelve el resultado de la primera verdadera: es la forma legible de escribir varios `IF` anidados. En el cuadro de formato condicional se elige **Valor del campo** y se selecciona la medida `Color participación`.

| Country | Participación | Color participación |
| --- | --- | --- |
| FRANCE | 16.00 % | #08519C |
| US | 11.98 % | #6BAED6 |
| PERU | 5.60 % | #BDBDBD |

La ventaja frente a las reglas del cuadro de diálogo es que los umbrales se cambian en un solo lugar y pueden venir de otra tabla, por ejemplo de una tabla de metas.

## 6. Barras de datos e iconos

Las **barras de datos** (data bars) dibujan dentro de la celda una barra proporcional al valor. Convierten la tabla en un pequeño gráfico de barras sin perder el número exacto. Se configuran el color de las barras positivas y negativas, la dirección y si se muestra solo la barra.

Las barras funcionan bien para comparar magnitudes de la misma columna. En la tabla de países se ve de inmediato que FRANCE vende casi tres veces lo que PERU (6 709.5 frente a 2 348.8 M).

Los **iconos** (flechas, semáforos, símbolos) se asignan con reglas, como en la sección 4. Son útiles para estados discretos: subió, bajó o se mantuvo.

| Icono | Regla sobre la variación anual |
| --- | --- |
| ▲ | > 0 |
| ▬ | = 0 |
| ▼ | < 0 |

Un icono no depende solo del color: la forma de la flecha comunica lo mismo a quien no distingue los colores.

## 7. Accesibilidad

Alrededor del 8 % de los hombres tiene algún tipo de daltonismo, el más común con dificultad para distinguir rojo y verde. Un semáforo rojo–verde, la elección más habitual, es justo la que más falla.

| Recomendación | Cómo aplicarla |
| --- | --- |
| Evitar el par rojo–verde | Usar azul–naranja para escalas divergentes |
| No depender solo del color | Añadir iconos, etiquetas o el propio número |
| Cuidar el contraste del texto | Con fondos oscuros, fuente blanca; WCAG recomienda un contraste mínimo de 4.5:1 para texto normal |
| Pocos colores con significado | Tres niveles se distinguen; siete no |

La regla del contraste también aplica al degradado: si el fondo pasa de blanco a azul muy oscuro, el texto negro se vuelve ilegible en las celdas más oscuras. Se puede combinar con un formato condicional del **color de fuente** que cambie a blanco cuando el fondo es oscuro.

## 8. Errores frecuentes

**Colorear todo.** Si las cuatro columnas de una tabla tienen degradado, ninguna destaca. El formato condicional funciona por contraste con lo que no tiene formato. Lo correcto es colorear la columna que responde a la pregunta principal y dejar las demás neutras.

**Usar un degradado secuencial para una variación.** Con una escala de blanco a azul, una variación de −30 % y una de +5 % pueden verse ambas claras, y el lector no distingue si el país creció o decreció. Para valores con signo, la escala debe ser divergente con el centro fijado en 0:

| Configuración | Mínimo | Centro | Máximo |
| --- | --- | --- | --- |
| Incorrecta | Valor más bajo: blanco | — | Valor más alto: azul |
| Correcta | Número −1: naranja | Número 0: blanco | Número 1: azul |

**Dejar el degradado automático cuando el informe tiene filtros.** Con mínimo y máximo automáticos, el color se recalcula con cada filtro, y el mismo valor cambia de color según lo que se haya seleccionado. Si el color tiene que significar algo estable, se fijan valores numéricos.

**Reglas con huecos.** Escribir "> 10 %" en una regla y "< 10 %" en la otra deja sin color al 10 % exacto. Un límite debe ser inclusivo (≥) y el otro exclusivo (<).

**Medida de color que devuelve texto inválido.** Si la medida devuelve `"azul oscuro"` o un código mal escrito (`"#08519"`), Power BI no aplica el color y no muestra error. Conviene usar códigos hexadecimales de seis dígitos y probar la medida en una tabla antes de usarla como formato.

**Elegir colores con el significado contrario.** En finanzas, el rojo significa pérdida; si la escala pinta de rojo los países con más ventas, el lector entenderá lo opuesto. El color debe respetar las convenciones del público.

## 9. Ejercicio

Se quiere una matriz con la variación de ventas de 2021 frente a 2020 por país. Los datos son:

| Country | Ventas 2020 (M) | Ventas 2021 (M) |
| --- | --- | --- |
| FRANCE | 866.4 | 3 453.6 |
| CANADA | 856.2 | 3 450.5 |
| US | 869.1 | 3 429.8 |
| BRAZIL | 495.6 | 2 311.9 |
| CHILE | 493.9 | 2 303.8 |
| MEXICO | 488.6 | 2 276.5 |
| PORTUGAL | 125.0 | 1 554.1 |
| SPAIN | 126.9 | 1 524.9 |
| COLOMBIA | 125.9 | 1 516.8 |
| PERU | 126.4 | 1 516.8 |

1. Calcula la variación anual de cada país.
2. Elige la escala de color adecuada para esa variación y justifica la elección.
3. Escribe una medida DAX que devuelva un color con tres niveles: crecimiento superior a 1000 %, entre 300 % y 1000 %, e inferior a 300 %. Usa colores aptos para daltonismo.
4. Indica qué agregarías para que la información no dependa solo del color.

### Solución

1. Variación = Ventas 2021 / Ventas 2020 − 1:

| Country | Variación 2021 vs 2020 | Nivel |
| --- | --- | --- |
| PORTUGAL | 1 142.8 % | Alto |
| COLOMBIA | 1 105.1 % | Alto |
| SPAIN | 1 101.7 % | Alto |
| PERU | 1 100.4 % | Alto |
| BRAZIL | 366.5 % | Medio |
| CHILE | 366.4 % | Medio |
| MEXICO | 365.9 % | Medio |
| CANADA | 303.0 % | Medio |
| FRANCE | 298.6 % | Bajo |
| US | 294.6 % | Bajo |

2. Todos los valores son positivos y no hay un cero que separe crecimiento de caída, así que basta una **escala secuencial** o, mejor, **reglas**, porque el enunciado define umbrales. Una escala divergente centrada en 0 no aportaría nada: todos los países quedarían del mismo lado.
3. La medida, suponiendo una tabla de calendario con la columna `Año` (Módulo 47):

```dax
Ventas 2020 = CALCULATE ( [Ventas], Calendario[Año] = 2020 )

Ventas 2021 = CALCULATE ( [Ventas], Calendario[Año] = 2021 )

Variación 2021 = DIVIDE ( [Ventas 2021] - [Ventas 2020], [Ventas 2020] )

Color variación =
VAR v = [Variación 2021]
RETURN
    SWITCH (
        TRUE (),
        ISBLANK ( v ), BLANK (),
        v > 10, "#08519C",      -- más de 1000 %: azul oscuro
        v >= 3, "#6BAED6",      -- de 300 % a 1000 %: azul claro
        "#FD8D3C"               -- menos de 300 %: naranja
    )
```

Una variación de 1000 % equivale a 10 en DAX, porque el porcentaje es solo el formato de la medida. El par azul–naranja se distingue con los tipos de daltonismo más comunes.

4. Se agrega la variación como número con formato de porcentaje junto al color y un icono por regla (por ejemplo, ▲ doble para el nivel alto). Así el color refuerza el mensaje pero no lo carga solo.

## Resumen

- El formato condicional usa atributos preatentivos, sobre todo el color, para que los valores importantes se vean sin leer toda la tabla.
- El degradado de dos colores sirve para magnitudes; el de tres colores, para valores con un punto de referencia, como el cero de una variación.
- Las reglas expresan umbrales de negocio; deben cubrir todos los valores sin huecos.
- Con **Valor del campo**, una medida DAX con `SWITCH ( TRUE (), ... )` decide el color y centraliza la lógica.
- Barras de datos e iconos complementan al color; la accesibilidad pide evitar rojo–verde, cuidar el contraste y no depender solo del color.
- Menos es más: el formato funciona por contraste con lo que no tiene formato.

En el **Módulo 47** se estudia DAX a fondo: medidas, contextos de evaluación e inteligencia de tiempo.

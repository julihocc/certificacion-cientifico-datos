# Módulo 44: Preparación de datos

Autor: Juliho Castillo Colmenares

> Lección complementaria del ejercicio de este módulo: [enunciado](m44-preparacion-de-datos-guia.ipynb) y [solución](m44-preparacion-de-datos-solucion.md). No es una tarea entregada del programa.

Un informe de Power BI solo es tan bueno como los datos que lo alimentan. Antes de dibujar un solo gráfico hay que importar los archivos, darles la forma correcta y limpiar lo que viene mal. En Power BI esa tarea la hace **Power Query**, y en esta lección la recorremos con los datos de ventas de la práctica de la sección (`../practica-ventas/datos-ventas/`), que traen casi todos los problemas típicos de un extracto real.

1. El flujo de trabajo de Power BI
2. Conectores: CSV, TXT, carpeta y Excel
3. Pasos aplicados y el lenguaje M
4. Perfilado de columnas
5. Limpieza de los casos reales
6. Anexar frente a combinar
7. Columnas personalizadas
8. Consultas intermedias y carga
9. Errores frecuentes
10. Ejercicio

## 1. El flujo de trabajo de Power BI

Power BI tiene dos piezas principales. **Power BI Desktop** es la aplicación de escritorio donde se construye todo, y **Power BI Service** es el servicio web donde se publica y se comparte (lo veremos en el Módulo 50). Dentro de Desktop el trabajo avanza en tres etapas:

| Etapa | Herramienta | Pregunta que responde |
| --- | --- | --- |
| Preparación | Power Query (Transformar datos) | ¿Los datos están limpios y con la forma correcta? |
| Modelado | Vista de modelo y DAX | ¿Cómo se relacionan las tablas y qué se calcula? |
| Visualización | Vista de informe | ¿Cómo se comunica el resultado? |

Power Query no modifica los archivos de origen. Guarda una **receta** de transformaciones que se vuelve a ejecutar cada vez que se pulsa **Actualizar** (Refresh). Si el mes que viene llega un CSV nuevo con el mismo formato, la limpieza se repite sola.

## 2. Conectores: CSV, TXT, carpeta y Excel

Desde **Inicio → Obtener datos** (Get data) se elige el conector según el tipo de origen. Los datos de la práctica usan cuatro:

| Archivo | Conector | Particularidad |
| --- | --- | --- |
| `ventas-2019.csv` | Texto/CSV | Encabezado en la primera fila; fechas en formato `M/D/YYYY` |
| `ventas-por-anio/` (2020 y 2021) | Carpeta | Dos CSV con la misma estructura; el de 2021 termina cada línea en coma |
| `paises.txt` | Texto/CSV con delimitador `\|` | Sin encabezado y con filas duplicadas |
| `catalogo.xlsx` | Libro de Excel | Tres hojas: `t_customer`, `t_store` y `t_product` |

Las primeras líneas de `ventas-2019.csv` muestran las columnas de la tabla de ventas:

| ID_T | ID_Country | Date | ID_Store | ID_Client | ID_Product | Quantity | Price |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 9 | 10/24/2019 | 1 | 551 | 291 | 155 | 233 |
| 2 | 2 | 6/17/2019 | 153 | 774 | 710 | 25 | 415 |
| 3 | 10 | 3/4/2019 | 159 | 356 | 962 | 445 | 58 |

Y así se ve `paises.txt`, sin fila de encabezado:

```text
1|US
1|US
2|CANADA
3|MEXICO
...
```

El conector **Carpeta** (Folder) es el más útil cuando los datos llegan en varios archivos con la misma estructura: lee todos los archivos de la carpeta y los apila. Al pulsar **Combinar y transformar datos**, Power Query crea consultas auxiliares (un archivo de ejemplo y una función) que aplican la misma transformación a cada archivo.

![Ventas 2020-2021 importadas desde una carpeta](captura-06.png)

## 3. Pasos aplicados y el lenguaje M

Cada acción en el Editor de Power Query se registra como un paso en el panel **Pasos aplicados** (Applied steps). Detrás de cada paso hay una línea del lenguaje **M**, que se ve en la barra de fórmulas o completa en **Inicio → Editor avanzado** (Advanced Editor).

Una consulta M es una expresión `let ... in`: cada paso tiene un nombre y recibe como entrada el paso anterior. Esta es la importación de `ventas-2019.csv`:

```powerquery
let
    // 1. Leer el archivo como texto delimitado por comas
    Origen = Csv.Document(
        File.Contents("C:\datos-ventas\ventas-2019.csv"),
        [Delimiter = ",", Columns = 8, Encoding = 65001, QuoteStyle = QuoteStyle.None]
    ),
    // 2. La primera fila contiene los nombres de columna
    Encabezados = Table.PromoteHeaders(Origen, [PromoteAllScalars = true]),
    // 3. Asignar tipos; "en-US" interpreta 10/24/2019 como mes/día/año
    Tipos = Table.TransformColumnTypes(
        Encabezados,
        {
            {"ID_T", Int64.Type}, {"ID_Country", Int64.Type}, {"Date", type date},
            {"ID_Store", Int64.Type}, {"ID_Client", Int64.Type}, {"ID_Product", Int64.Type},
            {"Quantity", Int64.Type}, {"Price", Currency.Type}
        },
        "en-US"
    )
in
    Tipos
```

Las funciones más usadas en la preparación son pocas:

| Función M | Botón equivalente | Qué hace |
| --- | --- | --- |
| `Table.PromoteHeaders` | Usar la primera fila como encabezado | Convierte la primera fila en nombres de columna |
| `Table.TransformColumnTypes` | Tipo de datos | Asigna tipos (entero, decimal, fecha, texto, moneda) |
| `Table.SplitColumn` | Dividir columna → Por delimitador | Separa un texto en varias columnas |
| `Table.Skip` | Quitar filas → Quitar filas superiores | Descarta las primeras *n* filas |
| `Table.Distinct` | Quitar filas → Quitar duplicados | Elimina filas repetidas |
| `Table.Combine` | Anexar consultas | Apila tablas con las mismas columnas |

No hace falta escribir M a mano: la interfaz lo genera. Pero leerlo permite revisar qué hace cada paso, corregirlo y copiarlo entre consultas.

## 4. Perfilado de columnas

En la pestaña **Vista** se activan tres ayudas que conviene dejar siempre encendidas al limpiar:

- **Calidad de columnas** (Column quality): porcentaje de valores válidos, con error y vacíos.
- **Distribución de columnas** (Column distribution): número de valores distintos y únicos.
- **Perfil de columnas** (Column profile): estadísticas y un histograma de la columna seleccionada.

Por defecto el perfil se calcula sobre las **primeras 1000 filas**. En la barra de estado se puede cambiar a "todo el conjunto de datos" cuando hace falta una respuesta exacta.

![Perfilado de la hoja t_store](captura-04.png)

La distribución delata problemas de un vistazo. En la hoja `t_store`, la columna `ID_Store` tiene 204 filas pero solo 200 valores distintos: hay tiendas repetidas. En `Format` aparecen más categorías de las esperadas porque el mismo formato está escrito de varias maneras.

## 5. Limpieza de los casos reales

Los archivos de `datos-ventas` traen cinco problemas distintos. Esta tabla los resume con su diagnóstico y su solución en Power Query:

| Origen | Problema | Solución |
| --- | --- | --- |
| `paises.txt` | Sin encabezado; `1\|US`, `4\|BRAZIL` y `5\|SPAIN` aparecen dos veces (12 filas, 10 países) | Renombrar columnas y `Table.Distinct` |
| `ventas-2021.csv` | Cada línea termina en coma, lo que crea una novena columna vacía | Leer solo 8 columnas o quitar la columna sobrante |
| `t_store` | Dos filas basura (`As of Date:2020` y una vacía) antes del encabezado; `Format` escrito como `"aa"`, `"AAA"` y `"   A"`; las tiendas 17, 167, 188 y 197 aparecen como `Open` y como `Closed` | `Table.Skip`, `Text.Trim` + `Text.Upper` y filtrar `Status = "Open"` |
| `t_customer` | `ID_Client` empaqueta cinco datos: `ID\|658\|Hamlin/Zohrer\|mail:hzohrerih@over-blog.com\|+55-890-712-8982`; al final hay filas vacías y un pie `CRM Extract by Data team 862992`; `zone` vale `?` en todas las filas | Filtrar filas válidas, `Table.SplitColumn` y quitar columnas sin información |
| `t_product` | `Product ID` tiene la forma `ID-1000\|Product`; 17 productos aparecen dos veces, una con `Active = 1` y otra con `Active = 0` | Extraer el número y filtrar `Active = 1` |

**Países.** Al leer un TXT con delimitador se indica el separador y luego se nombran las columnas, porque el archivo no trae encabezado:

```powerquery
let
    Origen = Csv.Document(
        File.Contents("C:\datos-ventas\paises.txt"),
        [Delimiter = "|", Columns = 2, Encoding = 65001, QuoteStyle = QuoteStyle.None]
    ),
    Renombradas = Table.RenameColumns(Origen, {{"Column1", "ID_Country"}, {"Column2", "Country"}}),
    Tipos = Table.TransformColumnTypes(Renombradas, {{"ID_Country", Int64.Type}, {"Country", type text}}),
    SinDuplicados = Table.Distinct(Tipos)
in
    SinDuplicados
```

| ID_Country | Country |
| --- | --- |
| 1 | US |
| 2 | CANADA |
| 3 | MEXICO |
| 4 | BRAZIL |
| ... | ... |
| 10 | FRANCE |

**Clientes.** El campo empaquetado se divide por el delimitador `|` en cinco columnas. Antes se filtran las filas que no empiezan por `ID|`, lo que elimina de una vez las filas vacías y el pie del extracto:

```powerquery
let
    Origen = Excel.Workbook(File.Contents("C:\datos-ventas\catalogo.xlsx"), null, true),
    Hoja = Origen{[Item = "t_customer", Kind = "Sheet"]}[Data],
    Encabezados = Table.PromoteHeaders(Hoja, [PromoteAllScalars = true]),
    // Solo las filas con un cliente real
    Validas = Table.SelectRows(
        Encabezados,
        each [ID_Client] <> null and Text.StartsWith([ID_Client], "ID|")
    ),
    // ID|658|Hamlin/Zohrer|mail:...|+55-... -> cinco columnas
    Divididas = Table.SplitColumn(
        Validas,
        "ID_Client",
        Splitter.SplitTextByDelimiter("|", QuoteStyle.None),
        {"Prefijo", "ID_Client", "Nombre completo", "mail", "tel"}
    ),
    SinSobrantes = Table.RemoveColumns(Divididas, {"Prefijo", "Nombre completo", "zone"}),
    SinEtiqueta = Table.TransformColumns(SinSobrantes, {{"mail", each Text.AfterDelimiter(_, "mail:"), type text}}),
    Tipos = Table.TransformColumnTypes(SinEtiqueta, {{"ID_Client", Int64.Type}})
in
    Tipos
```

Resultado esperado (950 clientes, uno por fila):

| ID_Client | first_name | last_name | mail | tel |
| --- | --- | --- | --- | --- |
| 658 | HAMLIN | Zohrer | hzohrerih@over-blog.com | +55-890-712-8982 |
| 261 | KARIE | Zellmer | kzellmer7g@gov.uk | +55-119-801-5241 |

![Hoja t_customer tras dividir columnas](captura-02.png)

**Productos.** La clave numérica está entre `ID-` y `|`. `Text.BetweenDelimiters` la extrae sin necesidad de dividir en columnas:

```powerquery
let
    Origen = Excel.Workbook(File.Contents("C:\datos-ventas\catalogo.xlsx"), null, true),
    Hoja = Origen{[Item = "t_product", Kind = "Sheet"]}[Data],
    Encabezados = Table.PromoteHeaders(Hoja, [PromoteAllScalars = true]),
    SoloActivos = Table.SelectRows(Encabezados, each [Active] = 1),
    ClaveNumerica = Table.TransformColumns(
        SoloActivos,
        {{"Product ID", each Number.FromText(Text.BetweenDelimiters(_, "ID-", "|")), Int64.Type}}
    ),
    Renombrada = Table.RenameColumns(ClaveNumerica, {{"Product ID", "ID_Product"}})
in
    Renombrada
```

Tras el filtro quedan 1000 productos con `ID_Product` del 1 al 1000, sin repetidos, que es justo el rango de `ID_Product` en las ventas.

## 6. Anexar frente a combinar

Power Query ofrece dos formas de juntar consultas, y es fácil confundirlas por el nombre:

| Operación | Botón | Dirección | Equivalente SQL | Uso típico |
| --- | --- | --- | --- | --- |
| **Anexar** (append) | Anexar consultas | Apila filas | `UNION ALL` | Ventas de 2019 + ventas de 2020–2021 |
| **Combinar** (merge) | Combinar consultas | Agrega columnas por una clave | `JOIN` | Agregar el nombre del país a cada venta |

Anexar exige que las tablas tengan las **mismas columnas con los mismos nombres**; si una columna falta en una tabla, se rellena con `null`. Las tres tablas de ventas juntas suman 300 000 + 499 000 + 700 000 = 1 499 000 filas, del 1 de enero de 2019 al 31 de diciembre de 2021.

```powerquery
let
    // Ventas2019 y Ventas2020_2021 son consultas ya limpias y con los mismos tipos
    Sales = Table.Combine({Ventas2019, Ventas2020_2021})
in
    Sales
```

Combinar, en cambio, usa `Table.NestedJoin` y después expande la columna de tabla resultante:

```powerquery
let
    Unidas = Table.NestedJoin(Sales, {"ID_Country"}, t_countries, {"ID_Country"}, "Pais", JoinKind.LeftOuter),
    ConPais = Table.ExpandTableColumn(Unidas, "Pais", {"Country"}, {"Country"})
in
    ConPais
```

En Power BI casi nunca hace falta combinar las dimensiones con la tabla de hechos: es mejor cargarlas por separado y **relacionarlas** en el modelo (Módulo 45). Combinar duplica el texto del país en 1,5 millones de filas; una relación lo guarda una sola vez.

## 7. Columnas personalizadas

Desde **Agregar columna → Columna personalizada** (Custom column) se escribe una expresión M que se evalúa fila a fila. El importe de cada venta es cantidad por precio:

```powerquery
let
    ConImporte = Table.AddColumn(Sales, "Sales", each [Quantity] * [Price], Currency.Type)
in
    ConImporte
```

| Date | Quantity | Price | Sales |
| --- | --- | --- | --- |
| 2019-01-01 | 28 | 257.00 | 7 196.00 |
| 2019-01-01 | 97 | 138.00 | 13 386.00 |
| 2019-01-01 | 142 | 983.00 | 139 586.00 |

El cuarto argumento de `Table.AddColumn` fija el tipo de la columna nueva. Sin él la columna queda como "cualquiera" (`any`) y el modelo no sabrá sumarla.

![Tabla de ventas con la columna Sales](captura-07.png)

## 8. Consultas intermedias y carga

Al importar por partes quedan consultas que solo sirven de paso: las ventas de 2019 por un lado, las de la carpeta por otro, y la consulta anexada que las junta. Si todas se cargan, el modelo guarda las mismas filas dos veces.

La solución es hacer clic derecho sobre cada consulta intermedia en el panel **Consultas** y desmarcar **Habilitar carga** (Enable load). La consulta sigue existiendo y alimenta a las demás, pero no se carga al modelo. En el panel aparece en cursiva.

| Consulta | ¿Cargar? |
| --- | --- |
| `Ventas2019` | No |
| `Ventas2020_2021` | No |
| `Sales` (anexada, con la columna `Sales`) | Sí |
| `t_countries`, `t_customer`, `t_product`, `t_store` | Sí |

Al terminar se pulsa **Inicio → Cerrar y aplicar** (Close & Apply) para cargar los datos al modelo.

## 9. Errores frecuentes

**Tipos de fecha con la configuración regional equivocada.** Si el equipo está en español, Power Query interpreta `10/24/2019` como día 10 del mes 24 y produce un error. La forma correcta es cambiar el tipo **usando la configuración regional** (clic derecho en la columna → Cambiar tipo → Usar configuración regional) o pasar la cultura en M:

```powerquery
// Incorrecto en un equipo con configuración es-MX: "10/24/2019" da Error
Tipos = Table.TransformColumnTypes(Encabezados, {{"Date", type date}})

// Correcto: se indica que el texto viene en formato de Estados Unidos
Tipos = Table.TransformColumnTypes(Encabezados, {{"Date", type date}}, "en-US")
```

**Cambiar el tipo antes de promover encabezados.** Power Query suele añadir un paso automático de tipos justo después de leer el archivo. Si la primera fila todavía es el encabezado, convierte `ID_Store` a texto para que quepa la palabra "ID_Store". Conviene borrar ese paso automático y fijar los tipos al final.

**La columna fantasma de la coma final.** `ventas-2021.csv` termina cada línea en coma, así que el archivo tiene nueve columnas. Al anexarlo con 2019 aparece una columna `Column9` (o vacía) llena de `null`. Se evita leyendo `Columns = 8` en `Csv.Document` o quitando esa columna antes de anexar.

**Tratar `ID_T` como clave única.** Cada archivo numera sus transacciones desde 1, así que después de anexar el número `1` aparece tres veces. Si se necesita un identificador único se puede agregar con **Agregar columna → Columna de índice** (`Table.AddIndexColumn`) después de anexar.

**Quitar filas por posición cuando el número cambia.** `Table.RemoveLastN(tabla, 5)` funciona hoy en `t_customer`, pero si el próximo extracto trae una fila vacía menos, borrará un cliente. Filtrar por contenido (`Text.StartsWith([ID_Client], "ID|")`) es más robusto.

**Normalizar texto sin quitar espacios.** `Text.Upper("   A")` sigue siendo `"   A"`, distinto de `"A"`. Primero se recortan los espacios y luego se cambian las mayúsculas:

```powerquery
Formato = Table.TransformColumns(Tabla, {{"Format", each Text.Upper(Text.Trim(_)), type text}})
```

## 10. Ejercicio

La hoja `t_store` de `catalogo.xlsx` empieza así:

| Column1 | Column2 | Column3 | Column4 | Column5 |
| --- | --- | --- | --- | --- |
| As of Date:2020 | null | null | null | null |
| null | null | null | null | null |
| ID_Store | Name_Store | Addres | Format | Status |
| 2 | Huels-Robel | 1029 Petterle Trail | AAA | Open |
| 17 | Rippin LLC | 30 Badeau Parkway | AAA | Open |
| 17 | Rippin LLC | 30 Badeau Parkway | AAA | Closed |

1. Quita las dos filas basura y promueve el encabezado.
2. Renombra `Addres` a `Address` y asigna los tipos: `ID_Store` entero y el resto texto.
3. Normaliza `Format` para que solo existan los valores `A`, `AA` y `AAA`.
4. Deja una sola fila por tienda, quedándote con la versión `Open`.
5. Agrega una columna `Formato orden` con 1 para `A`, 2 para `AA` y 3 para `AAA`, útil para ordenar visuales.
6. Comprueba con la distribución de columnas que `ID_Store` tiene tantos valores distintos como filas.

### Solución

```powerquery
let
    Origen = Excel.Workbook(File.Contents("C:\datos-ventas\catalogo.xlsx"), null, true),
    Hoja = Origen{[Item = "t_store", Kind = "Sheet"]}[Data],
    // 1. Fuera las dos filas basura
    SinBasura = Table.Skip(Hoja, 2),
    Encabezados = Table.PromoteHeaders(SinBasura, [PromoteAllScalars = true]),
    // 2. Nombre y tipos
    Renombrada = Table.RenameColumns(Encabezados, {{"Addres", "Address"}}),
    Tipos = Table.TransformColumnTypes(
        Renombrada,
        {{"ID_Store", Int64.Type}, {"Name_Store", type text}, {"Address", type text},
         {"Format", type text}, {"Status", type text}}
    ),
    // 3. "aa", "AAA", "   A" -> "AA", "AAA", "A"
    Formato = Table.TransformColumns(Tipos, {{"Format", each Text.Upper(Text.Trim(_)), type text}}),
    // 4. Una fila por tienda: las duplicadas tienen una versión Open
    Abiertas = Table.SelectRows(Formato, each [Status] = "Open"),
    // 5. Orden numérico del formato
    ConOrden = Table.AddColumn(
        Abiertas,
        "Formato orden",
        each if [Format] = "A" then 1 else if [Format] = "AA" then 2 else 3,
        Int64.Type
    )
in
    ConOrden
```

Resultado esperado: 200 filas, una por tienda, con `ID_Store` del 1 al 200 (200 distintos, 200 únicos) y tres formatos.

| ID_Store | Name_Store | Address | Format | Status | Formato orden |
| --- | --- | --- | --- | --- | --- |
| 2 | Huels-Robel | 1029 Petterle Trail | AAA | Open | 3 |
| 17 | Rippin LLC | 30 Badeau Parkway | AAA | Open | 3 |

Si se quisiera conservar el historial de estados, la alternativa sería no filtrar y crear otra tabla con el estado por fecha; para usar `t_store` como dimensión, la clave debe ser única.

## Resumen

- Power Query prepara los datos con una receta de pasos que se repite en cada actualización, sin tocar los archivos de origen.
- Cada paso es una línea de M: `Table.PromoteHeaders`, `Table.TransformColumnTypes`, `Table.SplitColumn`, `Table.Skip`, `Table.Distinct` y `Table.Combine` cubren la mayor parte de la limpieza.
- El perfilado de columnas (calidad, distribución y perfil) revela duplicados, vacíos y categorías mal escritas antes de que lleguen al informe.
- Anexar apila filas de tablas con las mismas columnas; combinar agrega columnas por una clave, aunque en Power BI suele ser mejor relacionar tablas en el modelo.
- Las consultas intermedias se dejan sin cargar para no duplicar datos en el modelo.

En el **Módulo 45** se organizan estas tablas en un modelo de datos: tabla de hechos, dimensiones y relaciones.

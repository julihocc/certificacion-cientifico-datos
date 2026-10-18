# Módulo 50: Publicación de dashboards

Autor: Juliho Castillo Colmenares

> Lección complementaria del ejercicio [m50-publicacion-de-dashboards.md](m50-publicacion-de-dashboards.md). No es una tarea entregada del programa.

Un informe que solo existe en un archivo `.pbix` en el equipo del autor no lo usa nadie más. Para que llegue a su público hay que publicarlo en **Power BI Service**, mantener sus datos al día y decidir quién ve qué. Esta lección recorre ese último tramo: los elementos del servicio, la publicación, la actualización programada, las formas de compartir y la seguridad de nivel de fila, que permite que un mismo informe muestre a cada usuario solo los datos que le corresponden.

1. Power BI Service y sus elementos
2. Publicar desde Desktop
3. Puerta de enlace y actualización programada
4. Compartir: acceso directo, áreas de trabajo y aplicaciones
5. Seguridad de nivel de fila
6. Seguridad de nivel de fila dinámica
7. Licencias
8. Errores frecuentes
9. Ejercicio

## 1. Power BI Service y sus elementos

Power BI Service (app.powerbi.com) es la parte web de Power BI. Al publicar un archivo de Desktop se crean en él varios elementos distintos:

| Elemento | Qué es | Relación con el `.pbix` |
| --- | --- | --- |
| **Área de trabajo** (workspace) | Contenedor donde viven los elementos y donde se asignan permisos | Destino de la publicación |
| **Modelo semántico** (semantic model, antes "conjunto de datos") | Las tablas, relaciones y medidas | El modelo del `.pbix` |
| **Informe** (report) | Las páginas con sus visuales interactivos | Las páginas del `.pbix` |
| **Panel** (dashboard) | Una sola página donde se **anclan** visuales de uno o varios informes | Se crea en el servicio; no existe en Desktop |

La diferencia entre informe y panel confunde por el nombre. Un **informe** tiene varias páginas, filtros, segmentadores y obtención de detalles; se diseña en Desktop. Un **panel** es una vista de una sola pantalla con mosaicos anclados desde informes (con el icono de la chincheta de cada visual); sirve como portada de monitoreo, y al hacer clic en un mosaico se abre el informe de origen.

Cada usuario tiene **Mi área de trabajo** (My workspace), personal. Para colaborar se crean áreas de trabajo compartidas, con cuatro roles:

| Rol | Puede |
| --- | --- |
| Administrador | Todo, incluido gestionar el área y sus miembros |
| Miembro | Publicar, editar y compartir contenido; agregar colaboradores |
| Colaborador | Publicar y editar contenido |
| Visor | Solo ver e interactuar con el contenido |

## 2. Publicar desde Desktop

Con el informe guardado, en **Inicio → Publicar** (Publish) se inicia sesión con la cuenta de la organización y se elige el área de trabajo de destino. Power BI sube el modelo y el informe; si ya existían con el mismo nombre, pregunta si se reemplazan.

Después de publicar conviene revisar en el servicio:

- Que el informe se vea igual que en Desktop (fuentes, tamaño de página).
- Que la configuración del modelo semántico tenga credenciales válidas para los orígenes de datos.
- Que las páginas auxiliares sigan ocultas y la navegación funcione con un clic.

Publicar copia los datos **tal como estaban** en el último refresco de Desktop. Para que se actualicen solos hace falta el paso siguiente.

## 3. Puerta de enlace y actualización programada

Los datos de la práctica son archivos locales: `ventas-2019.csv`, la carpeta `ventas-por-anio`, `paises.txt` y `catalogo.xlsx`. Power BI Service está en la nube y no puede leer el disco de un equipo. El puente es la **puerta de enlace de datos local** (on-premises data gateway): un programa que se instala en un equipo con acceso a los archivos y que el servicio usa para leerlos.

| Origen | ¿Necesita puerta de enlace? |
| --- | --- |
| Archivos en un disco local o una carpeta de red | Sí |
| Base de datos en un servidor de la empresa | Sí |
| Archivos en OneDrive o SharePoint en línea | No |
| Servicios en la nube (Azure SQL, por ejemplo) | Por lo general, no |

Hay dos modos: el **estándar**, compartido por varios usuarios y administrado de forma central, y el **modo personal**, para un solo usuario. La puerta de enlace solo funciona mientras el equipo donde está instalada está encendido y conectado.

Con la puerta de enlace configurada, en la configuración del modelo semántico se activa la **actualización programada** (scheduled refresh): frecuencia (diaria o semanal), horas y zona horaria, y a quién avisar si falla. El número de actualizaciones al día depende de la licencia: una capacidad compartida con licencia Pro admite hasta 8; las capacidades Premium o Fabric admiten más.

Cuando el modelo se actualiza, Power Query vuelve a ejecutar todos los pasos aplicados del Módulo 44. Por eso importa que la limpieza sea robusta: si un archivo nuevo trae una fila basura más, el paso que la elimina por contenido seguirá funcionando y el que la elimina por posición, no.

## 4. Compartir: acceso directo, áreas de trabajo y aplicaciones

Hay tres formas de dar acceso a un informe publicado:

| Forma | Cómo | Cuándo |
| --- | --- | --- |
| **Compartir** el elemento | Botón **Compartir** en el informe o panel | Pocas personas, acceso puntual |
| **Agregar al área de trabajo** | Asignar un rol en el área | Equipo que construye o mantiene el contenido |
| **Aplicación** (app) | Publicar una aplicación desde el área de trabajo | Distribución a un público amplio de consumidores |

Una **aplicación** empaqueta los informes y paneles de un área de trabajo con una navegación propia. Sus usuarios ven una versión estable: los autores pueden seguir editando en el área de trabajo y solo actualizan la aplicación cuando el contenido está listo. Es la forma recomendada de llegar a muchos usuarios.

## 5. Seguridad de nivel de fila

La **seguridad de nivel de fila** (row-level security, RLS) filtra las filas que puede ver cada usuario. Un solo informe sirve a todos: el gerente de Sudamérica ve solo sus cuatro países y el de Europa solo los suyos, sin crear un informe por región.

En Desktop se definen **roles**, cada uno con una regla de filtro en DAX sobre una tabla. Desde **Modelado → Administrar roles** (Manage roles):

1. Crear un rol, por ejemplo "Sudamérica".
2. Elegir la tabla a filtrar: `t_countries`.
3. Escribir la regla, ya sea con el editor de reglas de la interfaz o con el editor de DAX:

```dax
[Country] IN { "BRAZIL", "COLOMBIA", "CHILE", "PERU" }
```

La regla es una expresión que se evalúa en cada fila de la tabla: las filas donde es verdadera quedan visibles. El filtro viaja por las relaciones como cualquier otro: al reducir `t_countries` a cuatro países, `Sales` se reduce a las ventas de esos países.

Para probarla, **Modelado → Ver como** (View as) permite elegir uno o varios roles y ver el informe con sus restricciones. Una barra en la parte superior indica qué rol se está simulando hasta pulsar **Detener vista**.

![Administrar roles de seguridad y vista como rol en Desktop](assets/captura-01.png)

| Vista | Ventas totales | Países visibles |
| --- | --- | --- |
| Sin rol | 41 940 958 825 | 10 |
| Rol "Sudamérica" | 14 104 866 510 | BRAZIL, COLOMBIA, CHILE, PERU |

Después de publicar, los usuarios se asignan a los roles en el servicio: en el modelo semántico, opción **Seguridad**, se elige el rol y se agregan las personas o los grupos. Desde ahí también se puede **probar como rol** en el navegador.

La seguridad de nivel de fila restringe a los usuarios con rol **Visor** en el área de trabajo y a quienes acceden por compartir o por aplicación. Los administradores, miembros y colaboradores del área de trabajo ven todos los datos.

## 6. Seguridad de nivel de fila dinámica

Con muchos usuarios, un rol por región se vuelve difícil de mantener. La **RLS dinámica** usa un solo rol cuya regla depende de quién está viendo el informe. La función `USERPRINCIPALNAME ()` devuelve el correo (nombre principal) del usuario conectado.

Se agrega al modelo una tabla de seguridad, por ejemplo cargada desde un Excel:

| Email | ID_Country |
| --- | --- |
| ana@empresa.com | 4 |
| ana@empresa.com | 6 |
| luis@empresa.com | 2 |
| luis@empresa.com | 3 |

La tabla `t_usuarios` se deja **sin relación** con el resto del modelo y se oculta. El rol "Por usuario" tiene esta regla sobre `t_countries`:

```dax
[ID_Country]
    IN CALCULATETABLE (
        VALUES ( t_usuarios[ID_Country] ),
        t_usuarios[Email] = USERPRINCIPALNAME ()
    )
```

Para cada fila de `t_countries`, la regla comprueba si su `ID_Country` está entre los países asignados al usuario conectado. Ana ve Brasil (4) y Colombia (6); Luis ve Canadá (2) y México (3). Para dar acceso a una persona nueva basta con añadir filas a la tabla de seguridad y actualizar el modelo: no hay que tocar los roles.

En Desktop, **Ver como** permite combinar el rol con **Otro usuario** para simular el correo de Ana o de Luis.

## 7. Licencias

Las licencias de Power BI cambian con frecuencia en nombre y precio, así que aquí se describen solo en términos generales:

| Licencia | Para qué alcanza |
| --- | --- |
| **Gratuita** (Free) | Usar Desktop y publicar en Mi área de trabajo para uso personal; no permite compartir ni colaborar |
| **Pro** | Publicar en áreas de trabajo compartidas, compartir y consumir contenido compartido; en general, tanto quien comparte como quien consume necesitan Pro |
| **Premium por usuario** (PPU) | Lo de Pro más funciones avanzadas (más actualizaciones al día, modelos más grandes); el contenido en áreas PPU solo lo consumen usuarios con PPU |
| **Capacidad** (Premium o Fabric) | La organización compra capacidad; los usuarios con licencia gratuita pueden consumir el contenido alojado en ella |

Antes de diseñar la distribución de un informe conviene confirmar con el administrador de la organización qué licencias y capacidades están disponibles.

## 8. Errores frecuentes

**Publicar con orígenes en rutas locales y esperar que se actualice.** La actualización programada falla con un error de credenciales u origen inaccesible porque el servicio no ve `C:\`. Se resuelve con una puerta de enlace o moviendo los archivos a OneDrive o SharePoint y conectando desde ahí.

**Escribir la regla RLS sobre una columna que la tabla no tiene.** Una regla `Sales[Country] = "PERU"` no es válida porque `Sales` no tiene esa columna. Las reglas se escriben sobre las dimensiones (`t_countries[Country] = "PERU"`) y el filtro llega a los hechos por la relación.

**Escribir mal los valores de la regla.** `[Country] IN { "Peru", "Chile" }` funciona en los datos de la práctica porque las comparaciones de texto en DAX no distinguen mayúsculas, pero `"Perú"` con tilde no coincide con `"PERU"` y el país desaparece del rol sin ningún error. Se prueba cada rol con **Ver como** y se compara el número de filas visibles con lo esperado.

**Probar la RLS siendo administrador del área de trabajo.** Los administradores, miembros y colaboradores no quedan restringidos, así que el autor ve todo y concluye que la seguridad no funciona (o, peor, que funciona). Se prueba con **Ver como** en Desktop, con **Probar como rol** en el servicio o con un usuario de rol Visor.

**Crear el rol en Desktop y no asignar usuarios en el servicio.** El rol existe, pero nadie pertenece a él. Los visores sin rol asignado en un modelo con RLS no ven datos.

**Usar `USERNAME ()` en lugar de `USERPRINCIPALNAME ()`.** En el servicio ambas suelen devolver el correo, pero en Desktop `USERNAME ()` devuelve el usuario de Windows (`DOMINIO\usuario`), y las pruebas no coinciden con la tabla de seguridad. `USERPRINCIPALNAME ()` es la opción coherente.

## 9. Ejercicio

Una empresa quiere distribuir el informe de ventas a sus gerentes regionales.

1. Crea un rol "Europa" que muestre solo SPAIN, PORTUGAL y FRANCE. Escribe la regla DAX e indica en qué tabla va.
2. Calcula las ventas totales que debería ver este rol, a partir de las ventas por país (SPAIN 2 360 722 916, PORTUGAL 2 401 536 230, FRANCE 6 709 452 115).
3. La empresa prefiere una RLS dinámica. Diseña la tabla de seguridad para que `marta@empresa.com` vea Europa y `jorge@empresa.com` vea US y MEXICO, y escribe la regla del rol.
4. Indica qué pasos hacen falta en el servicio para que Marta vea el informe con su restricción.
5. Los archivos de ventas están en `C:\datos-ventas`. ¿Qué hace falta para actualizar el modelo cada mañana?

### Solución

1. Rol "Europa", regla sobre `t_countries`:

```dax
[Country] IN { "SPAIN", "PORTUGAL", "FRANCE" }
```

2. Ventas del rol = 2 360 722 916 + 2 401 536 230 + 6 709 452 115 = **11 471 711 261**, el 27.35 % del total de 41 940 958 825. Con **Modelado → Ver como → Europa**, una tarjeta con `Ventas` debe mostrar esa cifra.
3. Tabla de seguridad `t_usuarios`, sin relaciones y oculta:

| Email | ID_Country |
| --- | --- |
| marta@empresa.com | 5 |
| marta@empresa.com | 9 |
| marta@empresa.com | 10 |
| jorge@empresa.com | 1 |
| jorge@empresa.com | 3 |

Los identificadores salen de `paises.txt`: 5 SPAIN, 9 PORTUGAL, 10 FRANCE, 1 US y 3 MEXICO. Rol "Por usuario", regla sobre `t_countries`:

```dax
[ID_Country]
    IN CALCULATETABLE (
        VALUES ( t_usuarios[ID_Country] ),
        t_usuarios[Email] = USERPRINCIPALNAME ()
    )
```

Prueba en Desktop con **Ver como**, rol "Por usuario" y otro usuario `jorge@empresa.com`: deben verse 5 025 305 951 + 4 655 551 012 = 9 680 856 963 en ventas.

4. Publicar el informe en un área de trabajo compartida; en el modelo semántico, opción **Seguridad**, agregar a Marta (o a un grupo que la contenga) al rol "Por usuario"; dar acceso a Marta como **Visor** del área o mediante una aplicación. Si Marta fuera miembro del área, vería todos los países.
5. Instalar una puerta de enlace de datos local en un equipo que pueda leer `C:\datos-ventas` y que esté encendido por la mañana, registrar los orígenes en ella y activar la actualización programada diaria en el modelo semántico. La alternativa sin puerta de enlace es mover los archivos a OneDrive o SharePoint y cambiar el origen de las consultas.

## Resumen

- Al publicar se crean en un área de trabajo un modelo semántico y un informe; los paneles se arman en el servicio anclando visuales.
- Los orígenes locales necesitan una puerta de enlace para la actualización programada, que vuelve a ejecutar toda la preparación de Power Query.
- Se comparte directamente, por roles del área de trabajo o, para públicos amplios, con aplicaciones.
- La seguridad de nivel de fila filtra los datos por rol con reglas DAX sobre las dimensiones; se prueba con **Ver como** y se asignan usuarios en el servicio.
- La RLS dinámica con `USERPRINCIPALNAME ()` y una tabla de seguridad evita crear un rol por usuario o región.
- Las licencias determinan quién puede publicar, compartir y consumir; conviene confirmarlas antes de distribuir.

En el **Módulo 51** comienza la sección de modelado estadístico con el análisis de regresión.

-- =============================================================================
-- Módulo 36: Operaciones en tablas — Solución
-- Enunciado para estudiantes: m36-operaciones-en-tablas-guia.ipynb
-- Lección: m36-operaciones-en-tablas-leccion.ipynb
-- =============================================================================
--
-- Contexto:
--   Una tienda en línea quiere registrar sus ventas en una tabla propia de
--   SQL Server (base AdventureWorks2022, esquema dbo). La tabla se crea desde
--   cero y después se renombra, gana columnas y cambia el formato del número de
--   orden para incluir la clave del estado de la sucursal.
--
-- Instrucciones (tareas secuenciales; ver la guía para el detalle):
--   1. Crear la tabla Ventas.
--   2. Insertar órdenes.
--   3. Renombrar la tabla.
--   4. Agregar la fecha de envío.
--   5. Renombrar una columna.
--   6. Actualizar registros.
--   7. Prefijo de estado en el número de orden.
--   8. Crear la tabla Prueba.
--   9. TRUNCATE y DROP.
--   10. Eliminar órdenes canceladas.
--
--   Este archivo reúne una versión resumida: crea la tabla (Tarea 1), inserta
--   dos órdenes y muestra un UPDATE y un DELETE. La solución completa de cada
--   tarea está en script-01.sql a script-10.sql; las capturas de comprobación,
--   en evidencia-NN.png y en m36-operaciones-en-tablas-solucion.pdf/.pptx.
-- =============================================================================

USE AdventureWorks2022;
GO

-- Revisión posterior (2026-10): la clave primaria se declara con nombre explícito
-- (PK_Ventas) para que script-07.sql pueda eliminarla en cualquier instalación;
-- antes SQL Server le asignaba un nombre autogenerado (PK__Ventas__...).

CREATE TABLE dbo.Ventas (
    NumeroOrden INT NOT NULL,
    FechaOrden DATETIME,
    FechaEntrega DATE,
    EstatusOrden VARCHAR(50),
    NombreCliente NVARCHAR(100),
    DomicilioEntrega NVARCHAR(255),
    CompraOnline CHAR(1), -- 'S' para Sí, 'N' para No
    MetodoPago NVARCHAR(50),
    MetodoEnvio NVARCHAR(50),
    Subtotal DECIMAL(10, 2),
    Impuestos DECIMAL(10, 2),
    CostoEnvio DECIMAL(10, 2),
    Total DECIMAL(10, 2),
    Moneda CHAR(3),
    Observaciones NVARCHAR(MAX),
    CONSTRAINT PK_Ventas PRIMARY KEY (NumeroOrden)
);

-- Insertando el primer registro
INSERT INTO dbo.Ventas (
    NumeroOrden, FechaOrden, FechaEntrega, EstatusOrden, NombreCliente, 
    DomicilioEntrega, CompraOnline, MetodoPago, MetodoEnvio, Subtotal, 
    Impuestos, CostoEnvio, Total, Moneda, Observaciones
) VALUES (
    12345, '2022-08-05 18:58:46.867', '2022-08-15', 'Pendiente', 'Juan Pérez', 
    'Avenida Siempre Viva 742 Springfield', 'S', 'Tarjeta de Crédito', 'Express', 
    20565.62, 1971.51, 616.09, 23153.22, 'MXN', 
    'El cliente indica que solo puede recibir el envío entre semana'
);

-- Insertando el segundo registro
INSERT INTO dbo.Ventas (
    NumeroOrden, FechaOrden, FechaEntrega, EstatusOrden, NombreCliente, 
    DomicilioEntrega, CompraOnline, MetodoPago, MetodoEnvio, Subtotal, 
    Impuestos, CostoEnvio, Total, Moneda, Observaciones
) VALUES (
    12346, '2022-08-06 10:24:30.123', '2022-08-16', 'En Proceso', 'Ana López', 
    'Calle de la Rosa 15, Ciudad de México', 'N', 'Efectivo', 'Terrestre', 
    15200.00, 1368.00, 500.00, 17068.00, 'MXN', 
    'Preferible entregar por la mañana'
);

-- Actualizar el estatus de la orden con el Número de Orden 12345
UPDATE dbo.Ventas
SET EstatusOrden = 'Completada'
WHERE NumeroOrden = 12345;

-- Eliminar la orden con el Número de Orden 12346
DELETE FROM dbo.Ventas
WHERE NumeroOrden = 12346;
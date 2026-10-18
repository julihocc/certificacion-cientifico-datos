-- Tarea 1. Crear la tabla Ventas
-- Crea la tabla dbo.Ventas para almacenar las ventas de una tienda: número de
-- orden, fecha de orden, fecha de entrega, estatus, nombre del cliente,
-- domicilio de entrega, compra en línea (S/N), método de pago, método de envío,
-- subtotal, impuestos, costo de envío, total, moneda y observaciones, con el
-- tipo de dato adecuado para cada campo. Define el número de orden como clave
-- primaria con un nombre explícito.
-- Enunciado completo: m36-operaciones-en-tablas-guia.ipynb

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

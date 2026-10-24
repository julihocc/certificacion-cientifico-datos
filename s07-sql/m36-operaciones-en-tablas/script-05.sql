-- Tarea 5. Renombrar una columna
-- Cambia el nombre (no el tipo de dato) de la columna "CompraOnline" a
-- "BanderaCompraOnline" mediante código SQL.
-- Enunciado completo: m36-operaciones-en-tablas-guia.ipynb

USE AdventureWorks2022;
GO

EXEC sp_rename 'dbo.Ordenes.CompraOnline', 'BanderaCompraOnline', 'COLUMN';

SELECT TOP 10 BanderaCompraOnline 
FROM dbo.Ordenes;
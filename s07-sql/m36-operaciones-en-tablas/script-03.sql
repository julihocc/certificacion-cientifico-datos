-- Tarea 3. Renombrar la tabla
-- Cambia el nombre de la tabla de "Ventas" a "Ordenes" mediante código SQL.
-- Enunciado completo: m36-operaciones-en-tablas-guia.ipynb

USE AdventureWorks2022;
GO

EXEC sp_rename 'dbo.Ventas', 'Ordenes';

-- Tarea 4. Agregar la fecha de envío
-- Agrega una columna nueva para almacenar la fecha de envío mediante código SQL.
-- Enunciado completo: m36-operaciones-en-tablas-guia.ipynb

USE AdventureWorks2022;
GO

ALTER TABLE dbo.Ordenes
ADD FechaEnvio DATE;


SELECT TOP 10 FechaEnvio
FROM dbo.Ordenes;
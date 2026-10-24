-- Tarea 10. Eliminar órdenes canceladas
-- Sobre la tabla Ordenes, aplica un DELETE para eliminar solo los registros
-- cuyo estatus sea "Cancelada".
-- Enunciado completo: m36-operaciones-en-tablas-guia.ipynb

USE AdventureWorks2022;
GO

DELETE FROM dbo.Ordenes
WHERE EstatusOrden = 'Cancelada';

SELECT * FROM dbo.Ordenes
WHERE EstatusOrden = 'Cancelada';

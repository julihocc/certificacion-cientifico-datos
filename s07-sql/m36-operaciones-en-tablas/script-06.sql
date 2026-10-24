-- Tarea 6. Actualizar registros
-- Actualiza al menos 5 registros; por ejemplo, el método de pago o el
-- domicilio de entrega de alguna orden en particular.
-- Enunciado completo: m36-operaciones-en-tablas-guia.ipynb

USE AdventureWorks2022;
GO

UPDATE dbo.Ordenes
SET MetodoPago = 'Pago Móvil'
WHERE NumeroOrden = 12347;

UPDATE dbo.Ordenes
SET DomicilioEntrega = 'Calle Roble 25, Barrio Verde'
WHERE NumeroOrden = 12348;

UPDATE dbo.Ordenes
SET EstatusOrden = 'Enviada'
WHERE NumeroOrden = 12349;

UPDATE dbo.Ordenes
SET FechaEntrega = '2022-10-05'
WHERE NumeroOrden = 12350;

UPDATE dbo.Ordenes
SET Total = Total + 500 -- Aumenta el total en 500
WHERE NumeroOrden = 12351;

-- Utiliza la tabla Sales.SalesOrderHeader para crear una consulta que muestre los números de orden y números de compra solo para el año 2011.

SELECT 
    SalesOrderNumber,
    PurchaseOrderNumber
FROM 
    [AdventureWorks2022].[Sales].[SalesOrderHeader]
WHERE 
    YEAR(OrderDate) = 2011;

-- Revisión posterior (2026-10): el número de orden es SalesOrderNumber (por ejemplo 'SO43659'),
-- no SalesOrderID, que es el identificador interno de la tabla.

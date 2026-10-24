-- 6.Utiliza la tabla Sales.SalesOrderHeader para crear una consulta que muestre los números de orden y números de compra sin los 2 primeros caracteres y nombra los campos resultantes como NewSalesOrderNumber y NewPurchaseOrderNumber.

SELECT 
    SUBSTRING(SalesOrderNumber, 3, LEN(SalesOrderNumber)) AS NewSalesOrderNumber,
    SUBSTRING(PurchaseOrderNumber, 3, LEN(PurchaseOrderNumber)) AS NewPurchaseOrderNumber
FROM 
    [AdventureWorks2022].[Sales].[SalesOrderHeader];

-- Revisión posterior (2026-10): el número de orden es SalesOrderNumber (por ejemplo 'SO43659'),
-- no SalesOrderID, que es un entero; la versión entregada quitaba los 2 primeros dígitos del ID.
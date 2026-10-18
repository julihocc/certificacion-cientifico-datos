-- Utiliza las tablas Sales.SalesOrderHeader y Sales.Customer para crear una 
-- consulta que muestre el ID de la orden (SalesOrderID) y el ID del cliente 
-- (CustomerID). Asegúrate de incluir todas las órdenes, incluso si no hay un 
-- cliente asociado usando un RIGHT JOIN.

SELECT 
    soh.SalesOrderID, 
    c.CustomerID
FROM 
    [AdventureWorks2022].[Sales].[Customer] c
RIGHT JOIN 
    [AdventureWorks2022].[Sales].[SalesOrderHeader] soh
ON 
    soh.CustomerID = c.CustomerID;

-- Revisión posterior (2026-10): se invirtió el orden de las tablas. RIGHT JOIN conserva
-- todas las filas de la tabla de la derecha; para incluir todas las órdenes, aunque no
-- tengan un cliente asociado, Sales.SalesOrderHeader debe ir a la derecha del RIGHT JOIN.
-- En la versión entregada estaba a la izquierda, con lo que se conservaban todos los clientes.
-- Tarea 7. Prefijo de estado en el número de orden
-- Antepón al número de orden un código de 2 letras (catálogo RENAPO) del
-- estado de la sucursal: modifica la definición de la columna para admitir
-- letras y guion, y actualiza todos los registros con "XX-" si la compra fue
-- en línea (BanderaCompraOnline = 'S') o con "DF-" (Ciudad de México) si no.
-- Enunciado completo: m36-operaciones-en-tablas-guia.ipynb

USE AdventureWorks2022;
GO

-- Revisión posterior (2026-10): se usa el nombre explícito PK_Ventas definido en
-- script-01.sql en lugar del nombre autogenerado PK__Ventas__9A7552946CD46A71, que solo
-- existía en la instalación original. El sp_rename de la tabla (script-03.sql) no
-- renombra sus restricciones, así que la PK sigue llamándose PK_Ventas.
ALTER TABLE dbo.Ordenes
DROP CONSTRAINT PK_Ventas;

ALTER TABLE dbo.Ordenes
ALTER COLUMN NumeroOrden VARCHAR(10) NOT NULL;

UPDATE dbo.Ordenes
SET NumeroOrden = CASE 
                      WHEN BanderaCompraOnline = 'S' THEN 'XX-' + CAST(NumeroOrden AS VARCHAR)
                      ELSE 'DF-' + CAST(NumeroOrden AS VARCHAR)
                  END;

ALTER TABLE dbo.Ordenes
ADD CONSTRAINT PK_Ordenes_NumeroOrden PRIMARY KEY (NumeroOrden);

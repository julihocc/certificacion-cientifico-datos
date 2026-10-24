-- Tarea 8. Crear la tabla Prueba
-- Crea una tabla llamada Prueba con una sola columna e inserta 5 registros
-- aleatorios.
-- Enunciado completo: m36-operaciones-en-tablas-guia.ipynb

USE AdventureWorks2022;
GO

CREATE TABLE Prueba (
    Id INT
);

INSERT INTO Prueba (Id) VALUES (CAST(RAND()*100 AS INT));
INSERT INTO Prueba (Id) VALUES (CAST(RAND()*100 AS INT));
INSERT INTO Prueba (Id) VALUES (CAST(RAND()*100 AS INT));
INSERT INTO Prueba (Id) VALUES (CAST(RAND()*100 AS INT));
INSERT INTO Prueba (Id) VALUES (CAST(RAND()*100 AS INT));

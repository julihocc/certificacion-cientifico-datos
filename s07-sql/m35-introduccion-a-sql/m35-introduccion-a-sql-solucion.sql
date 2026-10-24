-- =============================================================================
-- Módulo 35: Introducción a SQL — Solución
-- Enunciado para estudiantes: m35-introduccion-a-sql-guia.ipynb
-- Lección: m35-introduccion-a-sql-leccion.ipynb
-- =============================================================================
--
-- Contexto:
--   AdventureWorks es una empresa ficticia que fabrica y vende bicicletas. El
--   área de Recursos Humanos pide unas cifras rápidas sobre su plantilla, que
--   está en la tabla HumanResources.Employee de la base AdventureWorks2022.
--
-- Instrucciones:
--   SQL Server con la base de ejemplo AdventureWorks2022 restaurada (SSMS o
--   Azure Data Studio). Una consulta por tarea:
--   1. Contar empleados: número total de empleados.
--   2. Contar empleados hombres: empleados con Gender = 'M'.
--   3. Horas de baja por enfermedad: LoginID y SickLeaveHours, de más a menos horas.
--   4. Empleados nacidos entre 1980 y 2000: cuántos nacieron entre el
--      1980-01-01 y el 2000-12-31, con BETWEEN sobre BirthDate.
--
--   El enunciado original del curso no se conserva; estas instrucciones se
--   reconstruyeron a partir de la solución.
-- =============================================================================

-- Tarea 1. Contar empleados
SELECT COUNT(*) 
FROM HumanResources.Employee

-- Tarea 2. Contar empleados hombres
SELECT COUNT(*) 
FROM HumanResources.Employee
WHERE Gender = 'M'

-- Tarea 3. Horas de baja por enfermedad
SELECT LoginID, SickLeaveHours 
FROM HumanResources.Employee
ORDER BY SickLeaveHours DESC

-- Tarea 4. Empleados nacidos entre 1980 y 2000
SELECT COUNT(BirthDate) 
FROM HumanResources.Employee
WHERE BirthDate BETWEEN '1980-01-01' AND '2000-12-31'
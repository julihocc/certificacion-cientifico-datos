# Proyecto P04: Análisis de películas con SQL — Solución
Author: Juliho Castillo Colmenares

Enunciado para estudiantes: [p04-analisis-de-peliculas-sql-guia.ipynb](p04-analisis-de-peliculas-sql-guia.ipynb) · Consultas: [p04-analisis-de-peliculas-sql-solucion.sql](p04-analisis-de-peliculas-sql-solucion.sql) · Plantilla original: [p04-avance-parte-4.sql](p04-avance-parte-4.sql)

## Contexto

Una cadena de tiendas de renta de DVD quiere conocer mejor su catálogo, a sus clientes y sus ventas: qué actores participan en más películas, cuánto cuesta rentar cada título, qué películas se rentan más y cuáles nunca, cuántos clientes tiene cada tienda y cuánto vende cada una. Cada pregunta se responde con una consulta de SQL.

## Datos

Base de datos de ejemplo **dvdrental** de PostgreSQL (esquema en [dvdrental/restore.sql](dvdrental/restore.sql); los archivos `.dat` con los datos no están en el repositorio). Tablas usadas: `actor`, `film`, `film_actor`, `inventory`, `rental`, `payment`, `customer` y `store`. Una renta apunta a una copia del inventario, así que para ir de `rental` a `film` hay que pasar por `inventory`.

## Instrucciones

PostgreSQL con la base `dvdrental` restaurada; una consulta por pregunta. Cada ejercicio muestra la consulta y una captura de su resultado (extensión Database Client de VS Code).

1. **Nombre y apellido de los actores.**
2. **Nombre completo en una sola columna.**
3. **Actores cuyo nombre empieza con "D".**
4. **Actores con el mismo nombre.**
5. **Costo máximo de renta.**
6. **Películas con el costo máximo.**
7. **Películas por tipo de audiencia.**
8. **Películas sin clasificación R ni NC-17.**
9. **Clientes por tienda.**
10. **Película más rentada.**
11. **Películas que no se han rentado.**
12. **Clientes sin rentas.**
13. **Actores con más de 30 películas.**
14. **Ventas totales por tienda.**
15. **Clientes que rentaron una película más de una vez.**

## Solución

### Exercise 1

**Tarea 1. Nombre y apellido de los actores.** Selecciona el nombre y el apellido de todos los actores.

```sql
SELECT first_name, last_name FROM actor;
```

![exercise-01](ejercicio-01.png)

### Exercise 2

**Tarea 2. Nombre completo en una sola columna.** Selecciona el nombre completo de cada actor en una sola columna (`full_name`).

```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM actor;
```

![exercise-02](ejercicio-02.png)

### Exercise 3

**Tarea 3. Actores cuyo nombre empieza con "D".** Selecciona los actores cuyo nombre empieza con "D".

```sql
SELECT first_name, last_name FROM actor WHERE first_name LIKE 'D%';
```

![exercise-03](ejercicio-03.png)

### Exercise 4

**Tarea 4. Actores con el mismo nombre.** ¿Hay actores que compartan el mismo nombre?

```sql
SELECT first_name, COUNT(*) FROM actor GROUP BY first_name HAVING COUNT(*) > 1;
```

![exercise-04](ejercicio-04.png)

### Exercise 5

**Tarea 5. Costo máximo de renta.** ¿Cuál es el costo máximo de renta de una película?

```sql
SELECT MAX(rental_rate) FROM film;
```

![alt text](ejercicio-05.png)

### Exercise 6

**Tarea 6. Películas con el costo máximo.** ¿Qué películas tienen ese costo de renta máximo?

```sql
SELECT title FROM film WHERE rental_rate = (SELECT MAX(rental_rate) FROM film);
```

![exercise-06](ejercicio-06.png)

### Exercise 7

**Tarea 7. Películas por tipo de audiencia.** ¿Cuántas películas hay por tipo de audiencia (`rating`)?

```sql
SELECT rating, COUNT(*) FROM film GROUP BY rating;
```

![exercise-07](ejercicio-07.png)

### Exercise 8

**Tarea 8. Películas sin clasificación R ni NC-17.** Selecciona las películas que no tienen un `rating` R o NC-17.

```sql
SELECT title FROM film WHERE rating NOT IN ('R', 'NC-17');
```

![exercise-08](ejercicio-08.png)

### Exercise 9

**Tarea 9. Clientes por tienda.** ¿Cuántos clientes hay en cada tienda?

```sql
SELECT store_id, COUNT(*) FROM customer GROUP BY store_id;
```

![exercise-09](ejercicio-09.png)

### Exercise 10

**Tarea 10. Película más rentada.** ¿Cuál es la película que más veces se rentó?

```sql
SELECT film.title, COUNT(rental.rental_id) AS rental_count
FROM rental
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
GROUP BY film.title
ORDER BY rental_count DESC
LIMIT 1;
```

![exercise-10](ejercicio-10.png)

### Exercise 11

**Tarea 11. Películas que no se han rentado.** ¿Qué películas no se han rentado?

```sql
SELECT title 
FROM film 
WHERE film_id NOT IN (SELECT film_id FROM inventory WHERE inventory_id IN (SELECT inventory_id FROM rental));
```

![exercise-11](ejercicio-11.png)

### Exercise 12

**Tarea 12. Clientes sin rentas.** ¿Qué clientes no han rentado ninguna película?

```sql
SELECT first_name, last_name 
FROM customer 
WHERE customer_id NOT IN (SELECT customer_id FROM rental);
```

![exercise-12](ejercicio-12.png)

### Exercise 13

**Tarea 13. Actores con más de 30 películas.** ¿Qué actores han actuado en más de 30 películas?

```sql
SELECT actor.first_name, actor.last_name, COUNT(film_actor.film_id) AS film_count
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
GROUP BY actor.actor_id
HAVING COUNT(film_actor.film_id) > 30;
```

![exercise-13](ejercicio-13.png)

### Exercise 14

**Tarea 14. Ventas totales por tienda.** Muestra las ventas totales por tienda.

```sql
SELECT store.store_id, SUM(payment.amount) AS total_sales
FROM payment
JOIN rental ON payment.rental_id = rental.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN store ON inventory.store_id = store.store_id
GROUP BY store.store_id;
```

![exercise-14](ejercicio-14.png)

### Exercise 15

**Tarea 15. Clientes que rentaron una película más de una vez.** Muestra los clientes que rentaron una película (la misma copia) más de una vez.

```sql
WITH rental_counts AS (
    SELECT customer_id, inventory_id, COUNT(*) AS rental_count
    FROM rental
    GROUP BY customer_id, inventory_id
)
SELECT customer.first_name, customer.last_name, rental_counts.rental_count
FROM rental_counts
JOIN customer ON rental_counts.customer_id = customer.customer_id
WHERE rental_counts.rental_count > 1;
```

![exercise-15](ejercicio-15.png)
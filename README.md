<div align="center">

# **📊🗃️Proyecto Nro 2 - Building mySQL Data-base** </div>
![Proyecto Nro 2 - Building mySQL Data-base](https://i.postimg.cc/JnxfCpBM/image-87.webp)


---
</div>

## Introducción
Este proyecto tiene como objetivo principal la creación de una base de datos utilizando SQL (Structured Query Language). 

La base de datos servirá como un almacén centralizado de información, permitiendo el acceso, búsqueda y análisis de datos de manera eficaz. 

Este proyecto abordará la definición de tablas, relaciones, índices y consultas SQL que cumplirán con las necesidades específicas de la organización. La creación de esta base de datos contribuirá a la toma de decisiones informadas y mejorará la eficiencia de la organización en la gestión de sus activos de datos."

## Contenido
- [data](https://github.com/Christelllameda/Proyecto-Nro-2/tree/main/data)
    - [cvs_originales](https://github.com/Christelllameda/Proyecto-Nro-2/tree/main/data/csv_originales)
    - [cvs_limpios](https://github.com/Christelllameda/Proyecto-Nro-2/tree/main/data/csv_limpios)
- [src](https://github.com/Christelllameda/Proyecto-Nro-2/tree/main/src)
    - [jupyter](https://github.com/Christelllameda/Proyecto-Nro-2/tree/main/src/jupyter)
        - [Limpieza de datos](https://github.com/Christelllameda/Proyecto-Nro-2/tree/main/src/jupyter/Limpieza%20de%20datos)
        - [Creación base de datos](https://github.com/Christelllameda/Proyecto-Nro-2/blob/main/src/jupyter/Base%20de%20datos.ipynb)
        - [Querys](https://github.com/Christelllameda/Proyecto-Nro-2/blob/main/src/jupyter/Querys.ipynb)
- [imagen](https://github.com/Christelllameda/Proyecto-Nro-2/tree/main/imagen)


## Objetivos
El objetivo principal de la creación de esta base de datos y su posterior análisis, es demostrar si es rentable reabrir un videoclub. Para ello necesitaremos:

Determinar el día que mas se alquilan películas.

Localizar cuál es la película mas alquilada.

Definir cuál es la categoría de películas que mas se suelen alquilar.

Determinar el total de dinero obtenido por rentas de películas en un día.

## Exploración y análisis de datos
En esta fase realizamos la detección y corrección de errores, así como la eliminación de valores nulos o duplicadoss que pueden tener un impacto negativo en la precisión y fiabilidad del análisis.

Observé que la columna 'last_update' estaba presente en varias tablas, pero la información que contenía no era relevante así que la eliminé.

En el archivo de 'rental' convertimos los valores de las columnas 'rental_date' y 'return_date' a un formato datetime para poder restarlos y conocer la cantidad de días que alquiló el cliente esa película, este valor lo guardamos en una nueva columna llamada 'rental_duration'

Además, añadí otra columna llamada 'day_of_week' que contiene el día de la semana que se alquiló la película (según la fecha almacenada en 'rental_date').

En el archivo 'old_hdd' observé que tenía una columna 'category_id', decidí crear un diccionario para agregar una nueva columna llamada 'category' que según el id, asignaría la categoría correspondiente a la película. Todo esto basado según la información obtenida en el csv 'category'.

En el archivo 'film', eliminé la columna 'original_language' ya que era una columna con valores nulos, al igual que la columna 'release_year' que mostraba que todas las películas habían sido estrenadas en el 2006, por lo que procedí a eliminarla ya que no me aportaía información relevante para poder filtrar datos.
Añadí una nueva columna 'total_rate', en ella almacené el resultado de la multiplicación de la columna 'rental_duration' con la columna 'rental_rate', para así obtener el costo total de ese alquiler.

## Creación de base de datos
Realicé la creación de la base de datos en sql desde python, para ello efectué la conexión al servidor para crear una nueva base de datos vacía a la que llamé 'movies'.

Posteriormente ejecutamos la string de conexión para ir cargando los diferentes cvs, convertidos en dataframe, como tablas en mi base de datos 'movies'. Todo los códigos se encuentran descritos en el jupyter notebook 'base de datos'

[![Captura-de-pantalla-2023-10-30-a-la-s-6-03-35-p-m.png](https://i.postimg.cc/SxhVWN2F/Captura-de-pantalla-2023-10-30-a-la-s-6-03-35-p-m.png)](https://postimg.cc/zVxnNNF0)

## Conclusión
Una vez realizadas las querys (descritas en el jupyter notebook 'querys') podemos concluir que:

- El día que mas se rentan películas es el sábado.
- La película mas rentada según los registros, es BOOGIE AMELIE
- La clasificación de películas mas rentada es PG-13, con supervisión de los padres para menores de 13 años.
- La categoría de películas que mas registros de alquileres tiene, es la de Documentary con 28 registros, seguida de Drama con 23 registros.
- El total de dinero obtenido por rentas de películas los sábados, fue de 458,28$.
<div align="center">

# **🚧🏗️Proyecto Nro 3 - Obras públicas inconclusas en Venezuela🏗️🚧** </div>
[Proyecto Nro 3 - ETL][![2-Metro-guarenas-Creditos-Sergio-Gonzalez-2.jpg](https://i.postimg.cc/vB7mLWxV/2-Metro-guarenas-Creditos-Sergio-Gonzalez-2.jpg)](https://postimg.cc/DJZF74gv)


---
</div>

## Introducción
El presente proyecto de Extracción, Transformación y Carga (ETL) sobre obras públicas inconclusas en Venezuela es una iniciativa crucial para abordar la problemática de las obras de infraestructura en el país. Venezuela, al igual que muchos otros lugares en el mundo, enfrenta desafíos en la ejecución y seguimiento de obras públicas, lo que puede tener un impacto significativo en el desarrollo y el bienestar de sus habitantes.

Este proyecto tiene como objetivo principal la recopilación, limpieza, transformación y análisis de datos relacionados con obras públicas que se encuentran inconclusas en diferentes regiones de Venezuela. La ejecución de obras inconclusas puede generar una serie de problemas, como el desperdicio de recursos públicos, la falta de acceso a servicios esenciales para la población y un impacto negativo en la calidad de vida de las comunidades afectadas.


## Contenido
- [data](https://github.com/Christelllameda/Proyecto-Nro-3/tree/main/data)
    - [Poblacion_estado_venezuela](https://github.com/Christelllameda/Proyecto-Nro-3/blob/main/data/Poblacion_estado_venezuela.csv)
    - [latitudes_longitudes](https://github.com/Christelllameda/Proyecto-Nro-3/blob/main/data/latitudes_longitudes.csv)
    - [obras_transporte](https://github.com/Christelllameda/Proyecto-Nro-3/blob/main/data/obras_transporte.csv)
    - [obras_vialidad](https://github.com/Christelllameda/Proyecto-Nro-3/blob/main/data/obras_vialidad.csv)
- [src](https://github.com/Christelllameda/Proyecto-Nro-3/tree/main/src)
    - [procesos](https://github.com/Christelllameda/Proyecto-Nro-3/blob/main/src/procesos.py)
- [jupyter_notebook](https://github.com/Christelllameda/Proyecto-Nro-3/tree/main/jupyter_notebook)
    - [Base_datos](https://github.com/Christelllameda/Proyecto-Nro-3/blob/main/jupyter_notebook/Base_datos.ipynb)
    - [Estados_Vzla](https://github.com/Christelllameda/Proyecto-Nro-3/blob/main/jupyter_notebook/Estados_Vzla.ipynb)
    - [Obras_transporte](https://github.com/Christelllameda/Proyecto-Nro-3/blob/main/jupyter_notebook/Obras_transporte.ipynb)
    - [Obras_vialidad](https://github.com/Christelllameda/Proyecto-Nro-3/blob/main/jupyter_notebook/Obras_vialidad.ipynb)
- [imagen](https://github.com/Christelllameda/Proyecto-Nro-3/tree/main/imagen)
- [html] (https://github.com/Christelllameda/Proyecto-Nro-3/tree/main/html)


## Objetivos
El propósito final de este proyecto es proporcionar a los ciudadanos, funcionarios gubernamentales y la sociedad civil una herramienta valiosa para el monitoreo y la toma de decisiones informadas en relación con las obras públicas en Venezuela. Al aumentar la transparencia y visibilidad de estas obras, se busca contribuir a la mejora de la gestión de proyectos de infraestructura y, en última instancia, al desarrollo sostenible del país.
Para ello necesitaremos:

Identificar las obras públicas inconclusas en los sectores de transporte y vialidad.

Definir el valor total de las obras públicas inconclusas.

## Extracción y limpieza de datos
Para el proceso de ETL nos basamos en la extracción de datos de tres fuentes distintas, en este caso fueron dos páginas webs y una Api que nos proporcionó las coordenadas de las diferentes direcciones de las obras.

Los métodos de extracción fueron: web scraping (selenium) donde obtuvimos todos los datos de las obras (status, dirección, el valor total de la obra, fecha de inicio, etc). Además utilizamos una base de datos que contenía todos lo estados de Venezuela junto con su población y densidad.

Los procesos anteriores se realizaron para crear un conjunto de datos completos y actualizados sobre estas obras. Luego, se llevó a cabo una transformación de los datos para estandarizar la información y hacerla más accesible y comprensible. 

## Creación de base de datos
Para la creación de nuestra base de datos utilizamos Mongo DB desde python, para ello efectuamos la conexión al servidor para crear una nueva base de datos vacía a la que llamamos 'obras_inconclusas'.

Posteriormente ejecutamos la string de conexión para ir cargando los diferentes cvs como colecciones en mi base de datos 'obras_inconclusas'. Todo los códigos se encuentran descritos en el jupyter notebook 'Base_datos'


## Conclusión
El proyecto de Extracción, Transformación y Carga (ETL) sobre obras públicas inconclusas en Venezuela es una iniciativa crucial para abordar la problemática de las obras de infraestructura en el país. A través de la recopilación, limpieza y análisis de datos, este proyecto busca aumentar la transparencia y la toma de decisiones informadas en relación con las obras públicas inconclusas. Al hacerlo, contribuye al mejoramiento de la gestión de proyectos de infraestructura y, en última instancia, al desarrollo sostenible de Venezuela. La identificación de obras inconclusas y su análisis detallado son pasos fundamentales hacia un futuro en el que los recursos públicos se utilicen eficaz y eficientemente para el beneficio de la sociedad.

## Links & Recursos
- https://pandas.pydata.org/
- https://docs.python.org/3/library/functions.html
- https://geopy.readthedocs.io/en/latest/
- https://selenium-python.readthedocs.io/
- https://docs.kepler.gl/docs/user-guides
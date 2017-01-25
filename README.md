#django-tweepy 

Este módulo es un Web Service tipo REST que realiza la búsqueda de un texto por medio de la API de twitter.
Despues de buscar el texto, guarda los resultados de la busqueda en una base de datos.

Metodos Soportados:
 * **POST**/**PUT** para realizar la busqueda del texto en twitter.
 * **GET**  Lista la base de datos.


Dependencias: 
 * [Tweepy] (http://www.tweepy.org/) para acceder a la API de twitter.
 * [Django REST framework] (http://www.django-rest-framework.org/)

Requerimientos:
 * [Docker] (https://github.com/docker/docker)
 * [Docker Compose] (https://docs.docker.com/compose/install/)
 
#Instalación

Para configurar los contenedores por primera vez
```bash
#Crea contenedores
docker-compose up --build

#Configuración inicial:
# - Instala las dependencias necesarias.
# - Cambia permisos a los archivos.
# - Crea tablas en Base de Datos (migrate).
# - Crear Usuario administrador.

./src/config.sh

```

#Uso 
Con esto ya se podrá navegar en: http://0.0.0.0:8000

Para usar el Web Service usar la siguiente URL:
http://0.0.0.0:8000/tweepy/



```bash
#Crear arcvivo de migraciones.
docker-compose run web python manage.py makemigrations nombre_app

#Actualizar migración
docker-compose run web python manage.py migrate
```

En caso de agregar dependencias

```bash
docker-compose run web pip install -r requirements/requirements.txt --upgrade
docker-compose run web pip install -r requirements/modules.txt
```


#Ayuda Docker

```bash
#Para saber la IP de los contenedores
docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)

#To list all running and stopped containers
docker ps -a

#To list all running containers (just stating the obvious and also example use of -f filtering option)
docker ps -a -f status=running

#To list all running and stopped containers, showing only their container id
docker ps -aq

#To remove all containers that are NOT running
docker rm `docker ps -aq -f status=exited`
docker rmi $(docker images -q)

docker-compose exec web bash

```

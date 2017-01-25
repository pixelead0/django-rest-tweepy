 #!/bin/bash

echo ============= Instalando dependencias =============
docker-compose run web pip install -r requirements/requirements.txt --upgrade
docker-compose run web pip install -r requirements/modules.txt

echo ============= Cambia permisos a los archivos =============
sudo chown -R $USER:$USER .

echo ============= Crea tablas en Base de Datos =============
docker-compose run web python manage.py migrate

echo ============= Crear Usuario administrador =============
docker-compose run web python manage.py createsuperuser
# Proyecto-final-info
Proyecto ONU 

Comitteen aca chicos no usen master  :D, uwu

# configuracion del proyecto
## ejecutar: 
* 1- pip install -r requirements.txt
* 2- python manage.py makemigrations
* 3- python manage.py migrate

## crear un super usuario:

* 1- python manage.py createsuperuser

## En etapa de deploy ejecutar lo siguientes comandos
* `python manage.py makemigrations`
* `python manage.py migrate --run-syncdb`

_Acto seguido eliminar 'migrations' del .gitignore para el posterior deploy_
## Tutorial de Django

1. Creamos el entorno virtual

 ```python -m venv nombre-entorno```

2. Instalamos Django

```pip install django```

3. Crear nuestro Proyecto

```django-admin startproject mysite```

4. Explicamos todo lo que creo el comando anterior
5. Creamos nuestra app

```python manage.py startapp polls```

6. Explicamos todo lo que creo el app anterior
7. Creamos nuestra primera views
8. Creamos nuestra primera urls ademas configuramos la del root
9. Creamos el modelo
10. Creamos las migraciones con estos comandos
```
python manage.py makemigrations nombre_bd
python manage.py migrate
```
11. Explicacion de la famosa api shell

```python manage.py shell```

````
 from polls.models import Choice, Question
 Question.objects.all()
````
12. Creamos el usuario administrador
```python manage.py createsuperuser```
13. Configurar el admin.py para mostrar el modelo


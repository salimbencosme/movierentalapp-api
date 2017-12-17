#First be in the python environment
workon myproject

#Update the structure of the database
python manage.py makemigrations

#Confirm changes to the database
python manage.py migrate

#Create a superuser
python manage.py createsuperuser

#run the server
python manage.py runserver

Note: in case of not having django-cors-headers
pip install django-cors-headers


#Create movies by the Admin de Django
#Create two users of different types (1-Admin 2-Client)

#Use the application
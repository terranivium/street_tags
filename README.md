### Street Tags
## Street Photography Location Tagging WebAPP

Technologies Used:

 - Anaconda (Virtual Environment)
 - Django (Web Framework)
 - Python
 - HTML/CSS
 - SQLite (DB)
 - JavaScript
 - Mapbox API

For an online demo see:
http://terranivium.pythonanywhere.com/
How to use this repo:

NOTE: localhost(127.) must be added to ALLOWED_HOSTS in settings.py

 - $ mkvirtualenv -p python3.7 geo-photo
 - $ pip install django==2.1.5
   $ pip install pillow==5.4.1
   $ pip install django-registration-redux==2.2
   $ pip install requests
   $ pip install coverage
 - clone repo
 - $ python manage.py makemigrations street_tag
   $ python manage.py migrate
   $ python manage.py createsuperuser
 - $ python manage.py runserver

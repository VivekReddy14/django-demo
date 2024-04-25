1. Created demo project

        django-admin startproject demo

2. Created myapp inside demo project - contains all my APIs

        python manage.py createapp myapp

    - Updated INSTALLED_APPS array with 'myapp' in demo/settings.py

3. Installed django rest framework

        pip install djangorestframework

    - Updated INSTALLED_APPS array with 'rest_framework' in demo/settings.py

4. Created APIs in myapp/views.py and registered the respective endpoints in myapp/urls.py 

    - Also added below code in demo/urls.py to reroute all enpoints to myapp 
        
        path("", include("myapp.urls"))

5. - Created a database model 'Catalog' in myapp/models.py 

    - Created a serializer 'CatalogSerializer' in myapp/serializers.py to convert Catalog model instance into python data types
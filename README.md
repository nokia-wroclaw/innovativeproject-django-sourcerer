# innovativeproject-django-sourcerer

## Links

 - Pypi https://pypi.org/project/django-sourcerer/
 - Source code https://github.com/nokia-wroclaw/innovativeproject-django-sourcerer

## Install
```pip install django-sourcerer```

## Usage
Add `django_sourcerer` and `rest_framework` texts to `settings.py` under `INSTALLED_APPS` list.
```
INSTALLED_APPS=[
    ... 
    'django_sourcerer',
    'rest_framework'
]
```
Add also to `settings.py` information that where the config file is located.
```
SOURCERER_CONFIG_FILES = [
    "project_path/example.yaml"
]
```
Then run following commands:
```
./manage.py makemigrations django_sourcerer
```
```
./manage.py migrate
```
For update objects from source type following command:
```
./manage.py update_objects
```
For view in API Framework add following lines of code to your `urls.py` :
```
from django.urls import path, include
from django_sourcerer.urls import django_sourcerer_urls

urlpatterns = [
    path('', include(django_sourcerer_urls().urls))
]
```
Then just start the API `./manage.py runserver` .

Library works with `csv` datas now. It will be updated for json&xls formats.

## Example .yaml File
```
name: <name of data source>
source: <endpoint of data source>
format: csv
columns:
  - external_name: <column name>
    type: <column type e.g : int>
  - external_name: <column name>
    type: <column type e.g : str>
```

### Requires

- Python 3

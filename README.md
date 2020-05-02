# innovativeproject-django-sourcerer

## Links

 - Pypi https://pypi.org/project/django-sourcerer/
 - Source code https://github.com/nokia-wroclaw/innovativeproject-django-sourcerer

## Install
```pip install django-sourcerer```

## Usage
Add `django_sourcerer` text to `settings.py` under `INSTALLED_APPS` list.
```
INSTALLED_APPS=[
    ... 
    'django_sourcerer'
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
After those commands you can query to shell as following script:
```
from django_sourcerer.models import Models
Models.objects.values()
```

Library works with 'csv' datas now. It will be updated for json&xls formats.

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

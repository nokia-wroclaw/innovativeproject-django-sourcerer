# innovativeproject-django-sourcerer

## Links

 - Pypi https://pypi.org/project/django-sourcerer/
 - Source code https://github.com/nokia-wroclaw/innovativeproject-django-sourcerer

## Install
```pip install django-sourcerer```

Then add `django_sourcerer` to your project.

## Usage
```
from django_sourcerer.domain.import_datas.intermediate_layer import Adapter
```
Then `Adapter("yaml_file").get_data_type_columns()`
It works with 'csv' datas now. It will be updated for json&xls formats.

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

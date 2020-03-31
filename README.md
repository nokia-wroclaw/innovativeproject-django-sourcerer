# innovativeproject-django-sourcerer

## Links

 - Pypi https://pypi.org/project/django-sourcerer/
 - Source code https://github.com/nokia-wroclaw/innovativeproject-django-sourcerer

##Install
```pip install django-sourcerer```

Then add `django_sourcerer` to your project.

##Usage
```
from django_sourcerer.domain.import_datas.intermediate_layer import Adapter
```
Then `Adapter("yaml_file").get_data_type_columns()`
### Requires

- Python 3
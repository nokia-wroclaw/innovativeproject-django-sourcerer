#!/usr/bin/env python
from django_sourcerer.import_datas.intermediate_layer import Adapter

from django_sourcerer.models import AutoModels

instance = AutoModels().ModelsFromConfFile
records = Adapter().get_df()

for i in records:
    to_db = [instance(**i)]
    instance.objects.bulk_create(to_db)

# python manage.py shell <django_sourcerer/update_objects.py

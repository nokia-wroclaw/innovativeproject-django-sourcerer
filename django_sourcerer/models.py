from django.db import models

from django_sourcerer.import_datas.intermediate_layer import Adapter


class CreateModelBasedOnYamlFile(models.Model):
    pass


class HandleModels:

    dic = Adapter().parse_models_values()

    for k, v in dic.items():

        if v == 'str':
            CreateModelBasedOnYamlFile.add_to_class(k, models.CharField(max_length=255))
        elif v == 'int':
            CreateModelBasedOnYamlFile.add_to_class(k, models.IntegerField(max_length=255))


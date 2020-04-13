from django.db import models

from django_sourcerer.import_datas.intermediate_layer import Adapter

ModelNameFromConfigFile = type(Adapter().parse_models_name(), (models.Model,), {
    '__module__': __name__,
})


class HandleModels:
    dic = Adapter().parse_models_values()

    for k, v in dic.items():

        if v == 'str':
            ModelNameFromConfigFile.add_to_class(k, models.CharField(max_length=255))
        elif v == 'int':
            ModelNameFromConfigFile.add_to_class(k, models.IntegerField(max_length=255))

from django.db import models

from django_sourcerer.import_datas.intermediate_layer import Adapter


class AutoModels:
    ModelsFromConfFile = type(Adapter().parse_models_name(), (models.Model,), {
        '__module__': __name__,
    })


class HandleModel:

    def parse_models(self):
        dic = Adapter().parse_models_values()

        for k, v in dic.items():

            if v == 'str':
                AutoModels.ModelsFromConfFile.add_to_class(k, models.CharField(max_length=255, null=True))
            elif v == 'int':
                AutoModels.ModelsFromConfFile.add_to_class(k, models.IntegerField(null=True))
            elif v == 'text':
                AutoModels.ModelsFromConfFile.add_to_class(k, models.TextField(max_length=255, null=True))


HandleModel().parse_models()

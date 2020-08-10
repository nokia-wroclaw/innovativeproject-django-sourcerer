from django.db import models

from django_sourcerer.import_datas.intermediate_layer import Adapter


class AutoModels:
    ModelsFromConfFile = type(Adapter().model_name(), (models.Model,), {
        '__module__': __name__,
    })

    def use_model(self):
        return self.ModelsFromConfFile


class HandleModel:

    def parse_models(self):
        dic = Adapter().parse_models_values()
        model = AutoModels().use_model()
        for k, v in dic.items():
            if v == 'str':
                model.add_to_class(k, models.CharField(max_length=255, null=True))
            elif v == 'int':
                model.add_to_class(k, models.IntegerField(null=True))
            elif v == 'text':
                model.add_to_class(k, models.TextField(max_length=255, null=True))


HandleModel().parse_models()

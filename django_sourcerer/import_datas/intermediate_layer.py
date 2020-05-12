import os

from django.conf import settings

from django_sourcerer.import_datas import parsing_config_file
from django_sourcerer.import_datas.import_csv_data import HandleCsvData


class Adapter(object):
    _importers = {
        'csv': HandleCsvData
    }

    def __init__(self):
        yaml_file = os.path.join(settings.BASE_DIR, settings.SOURCERER_CONFIG_FILES[0])
        self.yaml_data = parsing_config_file.ReadConfigFile(yaml_file).import_yaml_file()
        self.source = self.yaml_data['source']
        self.type = self.yaml_data['format']
        self.get_columns = self.yaml_data['columns']
        self.columns = []
        for i in self.get_columns:
            self.columns.append(i['external_name'])
        self.fields = []
        for i in self.get_columns:
            self.fields.append(i['type'])
        self.name = self.yaml_data['name']

    def get_df(self):
        importer = self._importers[self.type]
        call_function = importer(self.source, self.columns)
        call_function.import_()
        get_data = call_function.parse_data()
        return get_data.to_dict('records')

    def parse_models_values(self):
        dict_of_columns_fields = dict(zip(self.columns, self.fields))
        return dict_of_columns_fields

    def model_name(self):
        return self.name

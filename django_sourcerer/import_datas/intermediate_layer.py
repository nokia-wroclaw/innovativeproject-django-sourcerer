from django_sourcerer.import_datas import parsing_config_file
from django_sourcerer.import_datas.import_csv_data import HandleCsvData
from django_sourcerer.models import Sth

class Adapter(object):
    _importers = {
        'csv': HandleCsvData
    }

    def __init__(self, yaml_file):
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

    def get_data_type_columns(self):
        # importer = self._importers[self.type]
        # importer(self.source, self.columns).import_()
        pass

    def models_parameters(self):
        models_parameters_key = self.columns
        models_parameters_value = self.fields
        Sth(models_parameters_key, models_parameters_value).call()


Adapter('csv_config_file.yaml').models_parameters()
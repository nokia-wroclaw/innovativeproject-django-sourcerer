from django_sourcerer.import_datas import parsing_config_file
from django_sourcerer.import_datas.import_csv_data import HandleCsvData


class Adapter(object):
    _importers = {
        'csv': HandleCsvData
    }

    def __init__(self):
        yaml_file = '/Users/cemarslan/Desktop/innovativeproject-django-sourcerer/django_sourcerer/import_datas/csv_config_file.yaml'
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
        importer = self._importers[self.type]
        importer(self.source, self.columns).import_()

    def parse_models_values(self):
        dict_of_columns_fields = dict(zip(self.columns, self.fields))
        return dict_of_columns_fields

# Adapter().get_data_type_columns()

from django_sourcerer.domain.import_datas import parsing_config_file
from django_sourcerer.domain.import_datas.import_csv_data import HandleCsvData


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

    def get_data_type_columns(self):
        importer = self._importers[self.type]
        importer(self.source, self.columns).import_data()

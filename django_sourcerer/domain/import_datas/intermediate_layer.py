from django_sourcerer.domain.import_datas import parsing_config_file
from django_sourcerer.domain.import_datas.jsonHandler import JsonHandler
from django_sourcerer.domain.import_datas.csvHandler import CsvHandler
from django_sourcerer.domain.import_datas.importer import Importer


class Adapter(object):
    _handler = {
        'csv': CsvHandler,
        'json': JsonHandler,
    }

    def __init__(self, yaml_file):
        self.yaml_data = parsing_config_file.ReadConfigFile(yaml_file).import_yaml_file()
        self.source = self.yaml_data['source']
        self.type = self.yaml_data['format']
        self.get_columns = self.yaml_data['columns']
        self.columns = []
        for i in self.get_columns:
            self.columns.append(i['external_name'])

    def importer(self):
        return Importer(self.source)._get_response()

    def get_data(self):
        types = self._handler[self.type]
        data = types(self.columns, self.importer())._parse_data()
        return data


Adapter('csv_config_file.yaml').get_data()

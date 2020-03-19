from source.django_sourcerer.domain.import_datas import parsing_config_file
from source.django_sourcerer.domain.import_datas.import_csv import import_csv_data


class Adapter(object):
    _importers = {
        'csv': import_csv_data
    }

    def __init__(self):
        self.yaml_data = parsing_config_file.ReadConfigFile().import_yaml_file()
        self.source = self.yaml_data['source']
        self.type = self.yaml_data['format']
        self.get_columns = self.yaml_data['columns']
        self.columns = []
        for i in self.get_columns:
            self.columns.append(i['external_name'])

    def get_data_type_columns(self):
        importer = self._importers[self.type]
        importer.HandleCsvData(self.source, self.columns).import_data()


if __name__ == '__main__':
    Adapter().get_data_type_columns()

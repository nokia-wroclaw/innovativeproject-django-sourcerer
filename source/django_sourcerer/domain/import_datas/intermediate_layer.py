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

    def get_data_type(self):
        importer = self._importers[self.type]
        importer.get_data(self.source)


if __name__ == '__main__':
    Adapter().get_data_type()

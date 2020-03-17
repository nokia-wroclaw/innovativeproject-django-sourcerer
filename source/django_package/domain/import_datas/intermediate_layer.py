from source.django_package.domain.import_datas import parsing_config_file
from source.django_package.domain.import_datas.import_csv import import_csv_data


class Adapter:
    data_type = parsing_config_file.ReadConfigFile.data_type[0]

    def get_data_type(self):
        if self.data_type == 'csv':
            import_csv_data.get_data()
        elif self.data_type == 'json':
            pass
        elif self.data_type == 'xls':
            pass


a = Adapter()
a.get_data_type()

import requests

from source.django_package.domain.import_datas import parsing_config_file


def get_data():
    r = requests.get(parsing_config_file.ReadConfigFile.data_source[0])
    print(r.text)

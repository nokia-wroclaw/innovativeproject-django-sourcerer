import yaml


class ReadConfigFile:
    def import_yaml_file(self):
        with open("csv_config_file.yaml", 'r') as stream:
            docs = yaml.safe_load(stream)
        return docs

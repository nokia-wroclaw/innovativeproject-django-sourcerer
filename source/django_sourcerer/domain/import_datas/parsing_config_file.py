import yaml


class ReadConfigFile:

    def __init__(self, file):
        self.parse = file

    def import_yaml_file(self):
        with open(self.parse, 'r') as stream:
            docs = yaml.safe_load(stream)
        return docs

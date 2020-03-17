import yaml


class ReadConfigFile:
    config_file_keys = []
    config_file_values = []
    data_source = []
    data_type = []

    def parse_file(self):
        with open('csv_config_file.yaml') as f:
            docs = yaml.load_all(f, Loader=yaml.FullLoader)

            for doc in docs:
                for k, v in doc.items():
                    self.config_file_keys.append(k)
                    self.config_file_values.append(v)
        self.data_source.append(self.config_file_values[1])
        self.data_type.append(self.config_file_values[2])


run = ReadConfigFile()
run.parse_file()

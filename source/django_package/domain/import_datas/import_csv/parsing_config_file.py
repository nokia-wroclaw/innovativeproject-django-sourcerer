import yaml


class ReadConfigFile:
    config_file_keys = []
    config_file_values = []
    csv_data_source = []

    def parse_file(self):
        with open('csv_data_source.yaml') as f:
            docs = yaml.load_all(f, Loader=yaml.FullLoader)

            for doc in docs:
                for k, v in doc.items():
                    self.config_file_keys.append(k)
                    self.config_file_values.append(v)
        self.csv_data_source.append(self.config_file_values[1])


# a = ReadConfigFile()
# a.parse_file()
#
# print(a.csv_data_source)

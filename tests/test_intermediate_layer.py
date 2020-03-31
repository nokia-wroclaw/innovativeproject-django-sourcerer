import unittest
from unittest.mock import MagicMock, Mock

from django_sourcerer.domain.import_datas import intermediate_layer, parsing_config_file

test_csv_yaml = {'format': 'csv',
                 'source': 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv',
                 'columns': [{
                     'external_name': 'State'
                 }]}


class TestIntermediateLayer(unittest.TestCase):
    def test_csv_yaml_file_for_intermediate_layer(self):
        parsing_config_file.ReadConfigFile.import_yaml_file = Mock(return_value=test_csv_yaml)
        mocking_importers = intermediate_layer.Adapter._importers["csv"]
        mocking_importers.import_data = MagicMock()
        mocking_importers.handle_data = MagicMock()
        intermediate_layer.Adapter(test_csv_yaml).get_data_type_columns()

        mocking_importers.import_data.assert_called()

    def test_yaml_file_for_xls(self):
        pass

    def test_yaml_file_for_json(self):
        pass

    def test_column_len(self):
        parsing_config_file.ReadConfigFile.import_yaml_file = Mock(return_value=test_csv_yaml)
        get_len_of_column = intermediate_layer.Adapter(test_csv_yaml)

        assert len(get_len_of_column.columns) == 1


if __name__ == "__main__":
    unittest.main()

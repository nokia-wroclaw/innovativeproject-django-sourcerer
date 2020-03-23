import unittest
from unittest.mock import MagicMock, Mock
import requests
import requests_testing

from source.django_sourcerer.domain.import_datas import intermediate_layer
from source.django_sourcerer.domain.import_datas import parsing_config_file

test_csv_yaml = {'format': 'csv',
                 'source': 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv',
                 'columns': [{
                     'external_name': 'State'
                 }]}


class TestIntermediateLayer(unittest.TestCase):

    def test_yaml_file_for_csv(self):
        parsing_config_file.ReadConfigFile.import_yaml_file = Mock(return_value=test_csv_yaml)
        mocking_importers = intermediate_layer.Adapter._importers["csv"]
        mocking_importers.import_data = MagicMock()
        mocking_importers.handle_data = MagicMock()
        intermediate_layer.Adapter().get_data_type_columns()

        mocking_importers.import_data.assert_called()

    def test_yaml_file_for_xls(self):
        pass

    def test_yaml_file_for_json(self):
        pass

    @requests_testing.activate
    def test_requests(self):
        requests_testing.add(
            request={'url': 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'},
            response={'body': 'ok'})
        resp = requests.get('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

        assert resp.status_code == 200
        assert len(requests_testing.calls) == 1
        assert requests_testing.calls[
                   0].request.url == 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'


if __name__ == "__main__":
    unittest.main()

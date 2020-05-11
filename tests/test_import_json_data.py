import unittest
import pandas as pd
import requests_mock
from django_sourcerer.domain.import_datas.import_json_data import HandleJsonData

endpoint = 'https://raw.githubusercontent.com/plotly/datasets/master/PK_subban_shots.json'
key = ['shotType']
response_request = 'django_sourcerer'


class TestJsonData(unittest.TestCase):

    def test_parse_data_return(self):
        main_call = HandleJsonData(endpoint, key)
        self.assertIsInstance(main_call._parse_data(main_call._get_response()), pd.DataFrame)

    def test_get_response(self):
        main_call = HandleJsonData(endpoint, key)
        return_value = main_call._get_response()
        self.assertIsNotNone(return_value)

    @requests_mock.mock()
    def test_requests_response(self, mock_response):
        mock_response.get(endpoint, text=response_request)
        call_function = HandleJsonData(endpoint, key)._get_response().decode()

        self.assertEquals(call_function, response_request)


if __name__ == "__main__":
    unittest.main()

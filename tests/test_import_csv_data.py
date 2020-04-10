import unittest
import pandas as pd
import requests_mock

from django_sourcerer.import_datas.import_csv_data import HandleCsvData

endpoint = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
column = ['Rank']
test_response_example = 'Test Requests'


class TestImportCsvData(unittest.TestCase):

    def test_parse_data_return_data_frame(self):
        call_function = HandleCsvData(endpoint, column)

        self.assertTrue(isinstance(call_function._parse_data(call_function._get_response()), pd.DataFrame))

    def test_get_response_method_return_not_none(self):
        call_function = HandleCsvData(endpoint, column)
        test_return_value = call_function._get_response()

        self.assertTrue(test_return_value is not None)

    @requests_mock.mock()
    def test_requests_response(self, mock_response):
        mock_response.get(endpoint, text=test_response_example)
        call_function = HandleCsvData(endpoint, column)._get_response().decode()

        self.assertEqual(call_function, test_response_example)


if __name__ == "__main__":
    unittest.main()

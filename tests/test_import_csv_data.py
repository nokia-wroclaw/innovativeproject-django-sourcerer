import unittest
from unittest.mock import MagicMock, Mock
import requests
import pandas as pd

from django_sourcerer.domain.import_datas.import_csv_data import HandleCsvData

endpoint = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
column = ['Rank']


class TestImportCsvData(unittest.TestCase):

    def test_parse_data_return_data_frame(self):
        call_function = HandleCsvData(endpoint, column)

        self.assertTrue(isinstance(call_function._parse_data(call_function._get_response()), pd.DataFrame))

    def test_get_response_method_return_not_none(self):
        call_function = HandleCsvData(endpoint, column)
        test_return_value = call_function._get_response()

        self.assertTrue(test_return_value is not None)

    def test_get_response_raise_error_condition(self):
        HandleCsvData(endpoint, column).import_()
        checking_call_error = requests.exceptions.ConnectionError()
        checking_call_error = MagicMock()

        checking_call_error.assert_not_called()


if __name__ == "__main__":
    unittest.main()

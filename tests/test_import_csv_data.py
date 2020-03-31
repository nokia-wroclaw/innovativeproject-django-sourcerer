import unittest
from unittest.mock import MagicMock
import requests
import requests_mock

from django_sourcerer.domain import HandleCsvData

endpoint = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
column = ['Rank']


class TestImportCsvData(unittest.TestCase):
    def test_requests(self):
        session = requests.Session()
        adapter = requests_mock.Adapter()
        session.mount('mock', adapter)
        adapter.register_uri('GET', endpoint)
        resp = session.get(endpoint)

        assert resp.status_code == 200

    def test_raise_error_condition(self):
        HandleCsvData(endpoint, column).import_data()
        checking_call_error = requests.exceptions.ConnectionError()
        checking_call_error = MagicMock()

        checking_call_error.assert_not_called()

    def test_import_data_method_return(self):
        return_value = HandleCsvData(endpoint, column).import_data()
        self.assertFalse(return_value is None)


if __name__ == "__main__":
    unittest.main()

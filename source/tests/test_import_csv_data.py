import unittest
from unittest.mock import MagicMock, Mock
import requests
import requests_mock


class TestIntermediateLayer(unittest.TestCase):
    def test_requests(self):
        session = requests.Session()
        adapter = requests_mock.Adapter()
        session.mount('mock', adapter)

        adapter.register_uri('GET', 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
        resp = session.get('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
        assert resp.status_code == 200

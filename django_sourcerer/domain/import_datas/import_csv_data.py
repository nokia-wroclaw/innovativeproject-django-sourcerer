import requests
import time
import pandas as pd
import io


class HandleCsvData:

    def __init__(self, endpoint, columns):
        self.endpoint = endpoint
        self.columns = columns

    def import_(self):
        response = self._get_response()
        return self._parse_data(response)

    def _get_response(self):
        max_attempts = 3
        for trial in range(max_attempts):
            try:
                response = requests.get(self.endpoint, timeout=2)
            except requests.exceptions.ConnectionError:
                time.sleep(2)
            else:
                break
        return response.content

    def _parse_data(self, response):
        df = pd.read_csv(io.StringIO(response.decode('utf-8')), usecols=self.columns)
        return df

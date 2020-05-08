import requests
import time
import pandas as pd
import io


class HandleCsvData:

    def __init__(self, endpoint, columns):
        self.endpoint = endpoint
        self.columns = columns

    def import_(self):
        return self._get_response()

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

    def parse_data(self):
        df = pd.read_csv(io.StringIO(self.import_().decode('utf-8')), usecols=self.columns)
        return df

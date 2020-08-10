import pandas as pd
import io


class CsvHandler:
    def __init__(self, columns, response):
        self.columns = columns
        self.response = response

    def _parse_data(self):
        df = pd.read_csv(io.StringIO(self.response.decode('utf-8')), usecols=self.columns)
        return df

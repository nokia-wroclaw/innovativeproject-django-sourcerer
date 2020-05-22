import io
import pandas as pd


class JsonHandler:
    def __init__(self, columns, response):
        self.columns = columns
        self.response = response

    def _parse_data(self):
        df = pd.read_json(io.StringIO(self.response.decode('utf-8')))
        data = df.loc[0::, self.columns]
        return data

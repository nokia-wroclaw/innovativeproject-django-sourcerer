import requests
import time
import pandas as pd
import io


class HandleCsvData:
    def __init__(self, endpoint, columns):
        self.endpoint = endpoint
        self.columns = columns
        self.import_data()
        self.handle_data()

    def import_data(self):
        try:
            csv_data = requests.get(self.endpoint, timeout=2)
        except requests.exceptions.ConnectionError:
            time.sleep(2)
            csv_data = requests.get(self.endpoint, timeout=2)
        except requests.exceptions.RequestException as e:
            raise e
        return csv_data.content

    def handle_data(self):
        df = pd.read_csv(io.StringIO(self.import_data().decode('utf-8')), usecols=self.columns)
        print(df)

import requests
import time
import csv


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
        return csv_data

    def handle_data(self):
        text = self.import_data().iter_lines(decode_unicode='utf-8')
        reader = csv.DictReader(text, delimiter=',')
        a=len(self.columns)
        for i in range(0,a):
            for x in reader:
                print(x[self.columns[0]],x[self.columns[1]],x[self.columns[2]])




import requests


def get_data(endpoint):
    response_csv_data = requests.get(endpoint)
    print(response_csv_data.text)

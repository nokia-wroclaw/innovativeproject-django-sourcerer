import requests


def get_data(endpoint):
    csv_data = requests.get(endpoint)
    print(csv_data.text)

import requests
import time


class Importer:

    def __init__(self, endpoint):
        self.endpoint = endpoint

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

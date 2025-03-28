import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

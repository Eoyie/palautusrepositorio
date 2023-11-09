import requests

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url).json()
        return response

import requests
from urllib.parse import urljoin

class Facebook:
    def __init__(self, token):
        self._token = token
        self._url = 'https://graph.facebook.com'
        self._api_version = '/v2.5/'

    def api(self, method, path, data = {}):

        data['access_token'] = self._token

        commands = {
            'get': self.get_api,
            'post': self.post_api
        }

        return commands[method.lower()](self.get_url(path), data)

    def next(self, path):
        return requests.get(path).json()

    def get_api(self, path, data):
        return requests.get(path, data).json()

    def post_api(self, path, data):
        return requests.post(path, data).json()

    def get_url(self, path):
        return urljoin(self._url, self._api_version + path)
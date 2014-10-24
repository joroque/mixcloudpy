import requests

class Mixcloud(object):
    api_url = 'http://api.mixcloud.com/'
    
    def _request(self, resource):
        r  = requests.get(self.api_url + resource)
        if r.status_code == 200:
            return r.json()

    def get_user(self, username):
        return self._request(username)

    def get_tag(self, name):
        pass

    def get_artist(self, slug=None, name=None):
        pass

    def get_cloudcast(self, username, slug=None, name=None):
        pass



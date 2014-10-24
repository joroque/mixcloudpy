import requests

class Mixcloud(object):
    api_base = 'http://api.mixcloud.com/'
    
    def request(self, resource):
        r  = requests.get(self.api_base + resource)
        if r.status_code == 200:
            return r.json()

    def get_user(self, username):
        return self.request(username)

    def get_tag(self, slug=None, name=None):
        return self.request('tag/' + slug)

    def get_artist(self, slug=None, name=None):
        return self.request('artist/' + slug)

    def get_cloudcast(self, username, slug=None, name=None):
        return self.request(username + '/' + slug)


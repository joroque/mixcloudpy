import requests
from slugify import slugify

class Mixcloud(object):
    api_base = 'http://api.mixcloud.com/'
    
    def request(self, resource):
        r  = requests.get(self.api_base + resource)
        if r.status_code == 200:
            return r.json()

    def get_user(self, username):
        return self.request(username)

    def get_tag(self, name):
        name = slugify(unicode(name))
        return self.request('tag/' + name)

    def get_artist(self, name):
        name = slugify(unicode(name))
        return self.request('artist/' + name)

    def get_cloudcast(self, username, name):
        name = slugify(unicode(name))
        return self.request(username + '/' + name)


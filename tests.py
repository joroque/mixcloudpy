import os
import unittest
from urlparse import urlparse

import mixcloud

class TestUsers(unittest.TestCase):

    mc = mixcloud.Mixcloud()
    
    def test_get_user(self):
        """ Test GET /<username> """
        user = self.mc.get_user('romeroqj')
        self.assertEqual(user['username'], 'romeroqj')

    def test_get_tag_slug(self):
        """ Test GET /tag/<tag> where <tag> is a slug """
        tag = self.mc.get_tag('house')
        self.assertEqual(tag['name'], 'House')

    def test_get_tag_name(self):
        """ Test GET /tag/<tag> where <tag> is a name """
        tag = self.mc.get_tag('House')
        self.assertEqual(tag['key'], '/tag/house/')

    def test_get_artist_slug(self):
        """ Test GET /artist/<artist> where <artist> is a slug """
        artist = self.mc.get_artist('carl-cox')
        self.assertEqual(artist['name'], 'Carl Cox')

    def test_get_artist_name(self):
        """ Test GET /artist/<artist> where <artist> is a name """
        artist = self.mc.get_artist('Carl Cox')
        self.assertEqual(artist['slug'], 'carl-cox')

    def test_get_cloudcast_slug(self):
        """ Test GET /<username>/<cloudcast> where <cloudcast> is a slug """
        cloudcast = self.mc.get_cloudcast('spartacus', 'party-time')
        self.assertEqual(cloudcast['name'], 'Party Time')

    def test_get_cloudcast_name(self):
        """ Test GET /<username>/<cloudcast> where <cloudcast> is a name """
        cloudcast = self.mc.get_cloudcast('spartacus', 'Party Time')
        self.assertEqual(cloudcast['slug'], 'party-time')

    def test_get_category_slug(self):
        """ Test GET /categories/<category> where <category> is a slug """
        category = self.mc.get_category('tech-house')
        self.assertEqual(category['name'], 'Tech House')
        
    def test_get_category_name(self):
        """ Test GET /categories/<category> where <category> is a name """
        category = self.mc.get_category('Tech House')
        self.assertEqual(category['slug'], 'tech-house')

    def test_get_oauth_uri(self):
        """ Test for a well formed OAuth URI.

        Set up env variables MIXCLOUD_CLIENT_ID and MIXCLOUD_CLIENT_SECRET to
        run this test.
        """
        client_id = os.environ['MIXCLOUD_CLIENT_ID']
        redirect_uri = 'http://www.redirecthere.com'
        oauth_uri = urlparse(self.mc.get_oauth_uri(client_id, redirect_uri))
        location = oauth_uri.netloc
        path = oauth_uri.path
        query = oauth_uri.query
        self.assertEqual(location, 'www.mixcloud.com')
        self.assertEqual(path, '/oauth/authorize')
        self.assertEqual(query, 'client_id={0}?redirect_uri={1}'\
                         .format(client_id, redirect_uri))


if __name__ == '__main__':
    unittest.main()
            

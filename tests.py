import unittest

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

if __name__ == '__main__':
    unittest.main()
            

import unittest

import mixcloud

class TestUsers(unittest.TestCase):

    mc = mixcloud.Mixcloud()
    
    def test_get_user(self):
        """ Test GET /<username> """
        user = self.mc.get_user('romeroqj')
        self.assertEqual(user['username'], 'romeroqj')

    def test_get_tag(self):
        """ Test GET /tag/<tag> """
        tag = self.mc.get_tag('house')
        self.assertEqual(tag['name'], 'House')

    def test_get_artist(self):
        """ Test GET /artist/<artist> """
        artist = self.mc.get_artist('carl-cox')
        self.assertEqual(artist['name'], 'Carl Cox')

    def test_get_cloudcast(self):
        """ Test GET /<username>/<cloudcast> """
        cloudcast = self.mc.get_cloudcast('spartacus', 'party-time')
        self.assertEqual(cloudcast['name'], 'Party Time')

if __name__ == '__main__':
    unittest.main()
            

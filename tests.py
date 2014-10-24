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

if __name__ == '__main__':
    unittest.main()
            

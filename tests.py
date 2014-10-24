import unittest

import mixcloud

class TestUsers(unittest.TestCase):
    def test_get_user(self):
        mc = mixcloud.Mixcloud()
        user = mc.get_user('romeroqj')
        self.assertEqual(user['username'], 'romeroqj')

if __name__ == '__main__':
    unittest.main()
            

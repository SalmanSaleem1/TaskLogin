from flask_testing import TestCase
import unittest




class UserViewsTests(TestCase):
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

if __name__=='__main__':
    unittest.main()

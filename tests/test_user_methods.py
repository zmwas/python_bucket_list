"""Tests for user methods.

"""

import unittest

from bucket_app.bucket_user import BucketUser


class UserTestCase(unittest.TestCase):
    """TestCase for user methods.
    """

    def setUp(self):
        self.bucket_user = BucketUser('Zacharia Mwangi', 'zacmwanginj@gmail.com')

    def test_create_user_returns_user(self):
        """
        Tests that the create_user method returns a user.

        """

        user = BucketUser("", "")
        zac = user.create_user('Zacharia Mwangi', 'zacmwanginj@gmail.com')
        self.assertIsInstance(zac, BucketUser, msg="create user method should return a user object")

    def test_create_user_requires_email(self):
        """
        Tests that create_user method checks for email.

        """

        user = BucketUser("", "")
        self.assertEqual(user.create_user('Zacharia Mwangi', ''), "Please provide an email",
                         msg="email should be provided to create user")

    def test_create_user_requires_name(self):
        """
        Tests that create_user method checks for name.

        """
        user = BucketUser("", "")
        self.assertEqual(user.create_user('', 'zacmwanginj@gmail.com'), 'Please provide your name',
                         msg="name should be provided to create user")

    def test_password_is_set(self):
        """
        Tests that set_password sets the password.

        """
        user = self.bucket_user.set_password("password")
        self.assertTrue(user)


if __name__ == '__main__':
    unittest.main()

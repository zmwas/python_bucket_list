import unittest

from accounts.bucket_user import BucketUser


class UserTestCase(unittest.TestCase):
    """TestCase for user methods

    """

    def setUp(self):
        self.bucket_user = BucketUser('Zacharia Mwangi', 'zacmwanginj@gmail.com')

    def test_create_user_returns_user_object(self):
        """
        Tests that the create_user method returns a user

        """

        user = BucketUser("", "")
        self.assertIsInstance(user.create_user('Zacharia Mwangi', 'zacmwanginj@gmail.com'), BucketUser,
                              msg="create user method should return a user object")

    def test_create_user_requires_email(self):
        """
        Tests that create_user method checks for email

        """

        user = BucketUser("", "")
        self.assertEqual(user.create_user('Zacharia Mwangi', ''), "Please provide an email",
                         msg="email should be provided to create user")

    def test_create_user_requires_name(self):
        """
        Tests that create_user method checks for name

        """
        user = BucketUser("", "")
        self.assertEqual(user.create_user('', 'zacmwanginj@gmail.com'), 'Please provide your name',
                         msg="name should be provided to create user")


if __name__ == '__main__':
    unittest.main()

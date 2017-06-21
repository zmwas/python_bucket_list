import unittest

from accounts.bucket_user import BucketUser


class UserTestCase(unittest.TestCase):
    """TestCase for user methods

    """

    def setUp(self):
        self.bucket_user = BucketUser('Zacharia Mwangi', 'zacmwanginj@gmail.com')

    def test_create_user_returns_user_object(self):
        """
        Tests whether the create_user method returns a user
        :return:
        """

        user = BucketUser("", "")
        self.assertIsInstance(user.create_user('Zacharia Mwangi', 'zacmwanginj@gmail.com'), BucketUser)

    def test_create_user_requires_email(self):
        user = BucketUser("", "")
        self.assertEqual(user.create_user('Zacharia Mwangi', ''), "Please provide an email")


if __name__ == '__main__':
    unittest.main()

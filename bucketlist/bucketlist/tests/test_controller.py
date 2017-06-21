"""
This module tests user controller and bucket controller methods

"""

import unittest
from user_controller import UserAuth


from bucket_controller import BucketController


class TestController(unittest.TestCase):
    """Tests user controller methods

    """

    def setUp(self):
        self.auth = UserAuth()
        self.buck = BucketController()

    def test_user_registration(self):
        """
        Tests successful user registration

        """
        self.assertTrue(len(self.auth.list_of_users) <
                        len(self.auth.add_user("Zack", "johndoe@gmail.com", "Hunter1")))


    def test_user_email_exists(self):
        """
        Test email is unique

        """
        self.assertEqual(self.auth.add_user("Identity Thief", "zacmwanginj@gmail.com", "1234"),
                         "That email is taken")


    def test_login(self):
        """
        Test successful login

        """

        self.auth.add_user("Zack", "zacmwanginj@gmail.com", "Hunter1")

        self.assertEqual(self.auth.login("zacmwanginj@gmail.com", "Hunter1"), "Welcome")


    def tearDown(self):
        del self.auth

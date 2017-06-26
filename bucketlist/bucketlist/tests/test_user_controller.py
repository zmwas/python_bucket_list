"""
This module tests user controller  controller methods

"""

import unittest

from controllers.user_controller import UserAuth


class TestController(unittest.TestCase):
    """Tests user controller methods

    """

    def setUp(self):
        self.auth = UserAuth()

    def tearDown(self):
        del self.auth

    def test_user_registration(self):
        """
        Tests successful user registration

        """
        self.assertTrue(len(self.auth.list_of_users) <
                        len(self.auth.add_user("Zack", "johndoe@gmail.com", "Hunter1")))

    def test_login(self):
        """
        Tests a login is successful

        """
        self.auth.add_user("Zack","zac@gmail.com","1234")
        self.assertEqual(self.auth.login("zac@gmail.com","1234"),"Welcome")




    def test_unsuccessful_login(self):
        """
        Tests a login attempt that was unsuccessful

        """
        self.auth.add_user("Zack", "first@gmail.com", "1234")
        self.assertEqual(self.auth.login("first@gmail.com", "12345"), "Wrong email or password")

    def test_empty_login(self):
        """
        Tests an empty

        """

        self.auth.add_user("Zack", "email@host.com", "1234")
        self.assertEqual(self.auth.login("", "1234"), "Wrong email or password")

    def test_user_email_exists(self):
        """
        Test email is unique

        """
        self.assertEqual(self.auth.add_user("Identity Thief", "johndoe@gmail.com", "1234"),
                         "That email is taken")


if __name__ == '__main__':
    unittest.main()

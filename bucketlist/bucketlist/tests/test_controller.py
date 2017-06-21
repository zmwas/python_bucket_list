import unittest
from user_controller import UserAuth


class TestController(unittest.TestCase):
    def setUp(self):
        self.auth = UserAuth()

    def test_user_registration_successful(self):
        """
        Tests successful user registration

        """
        # self.assertEqual(len(self.auth.add_user("Zack", "zacmwanginj@gmail.com", "Hunter1")), 1,
        #                  msg="Method should add user to list")
        self.assertTrue(len(self.auth.list_of_users) < len(self.auth.add_user("Zack", "johndoe@gmail.com", "Hunter1")))
    def test_user_email_exists(self):
        self.assertEqual(self.auth.add_user("Identity Thief", "zacmwanginj@gmail.com", "1234"), "That email is taken")

    def test_login(self):
        self.auth.add_user("Zack", "zacmwanginj@gmail.com", "Hunter1")

        self.assertEqual(self.auth.login("zacmwanginj@gmail.com", "Hunter1"), "Welcome")

    def tearDown(self):
        del self.auth
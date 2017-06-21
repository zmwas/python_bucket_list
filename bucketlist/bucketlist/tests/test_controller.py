import unittest
from accounts.bucket_user import BucketUser
from user_controller import list_of_users, UserAuth


class TestController(unittest.TestCase):
    def setUp(self):
        self.my_list = list_of_users

    def test_user_registration_successful(self):
        """
        Tests successful user registration
                 
        """
        user = BucketUser()
        user.create_user("Zack", "zacmwanginj@gmail.com")
        user.set_password("Hunter1")
        auth = UserAuth()
        self.assertEqual(len(auth.add_user(user)), len(self.my_list) + 1, msg="Method should add user to list")

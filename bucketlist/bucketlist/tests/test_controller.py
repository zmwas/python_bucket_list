import unittest
from accounts.bucket_user import BucketUser
from user_controller import list_of_users, UserAuth


class TestController(unittest.TestCase):
    def setUp(self):
        self.auth = UserAuth()
        self.user = BucketUser()

    def test_user_registration_successful(self):
        """
        Tests successful user registration

        """
        user = BucketUser()
        self.assertEqual(len(self.auth.add_user("Zack","zacmwanginj@gmail.com","Hunter1")), 1, msg="Method should add user to list")

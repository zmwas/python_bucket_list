import unittest
from accounts.bucket_user import BucketUser
from user_controller import list_of_users


class TestController(unittest.TestCase):
    def setUp(self):
        
        self.my_list=list_of_users


    def test_user_added_to_db(self):
        user = BucketUser()
        user.create_user("Zack","zacmwanginj@gmail.com")
        user.set_password("Hunter1")

        add_user(user)
        self.assertEqual(len(add_user),len(self.my_list)+1,msg="Method should add user to list")
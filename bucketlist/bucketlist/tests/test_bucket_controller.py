"""
This module tests bucket controller methods

"""

import unittest
from bucket_controller import BucketController
from user_controller import UserAuth
from buckets.buckets import BucketList
from buckets.bucket_items import BucketListItems


class BucketListTestCase(unittest.TestCase):
    """Test Case for bucket controller methods

    """

    def setUp(self):
        self.buck = BucketController()
        self.auth = UserAuth()

    def test_create_bucket_directory(self):
        self.auth.add_user("Zack", "zacmwanginj@gmail.com", "password")
        lists = len(self.buck.create_bucket_directory())
        users = len(self.auth.list_of_users)
        self.assertEqual(lists, users)

    def test_create_bucket_list(self):
        self.auth.add_user("Zack", "johndoe@gmail.com", "password")
        user= self.auth.list_of_users[0]
        bucket= self.buck.create_bucket_list(user.email, "name", "status")[0]

        self.assertEqual(len(bucket),2)

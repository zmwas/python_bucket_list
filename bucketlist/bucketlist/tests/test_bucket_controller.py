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

        user = self.auth.list_of_users[0]
        # The initial length of the list of bucket lists
        initial = len(self.buck.bucket_list_dictionaries.get(user.email))
        #create a bucket list
        self.buck.create_bucket_list(user.email, "name", "status")
        # The new length of the list after bucket list is created
        new = len(self.buck.bucket_list_dictionaries.get(user.email))

        self.assertEqual(initial + 1, new)



    def test_add_bucket_item(self):
        self.auth.add_user("Zack", "johndoe@gmail.com", "password")
        self.buck.create_bucket_directory()
        bucket = self.buck.create_bucket_list("johndoe@gmail.com", "new", "status")

        print(bucket)
        bucket_item = BucketListItems()

        bucket_item.create_bucket_items("Make something")
        created = self.buck.add_bucket_item("johndoe@gmail.com","new",bucket_item.name,bucket_item.completion_status)
        print(created)
        self.assertEqual(len(created),3)

if __name__ == '__main__':
    unittest.main()

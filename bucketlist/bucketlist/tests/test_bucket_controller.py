"""
This module tests bucket controller methods

"""

import unittest

from bucket_controller import BucketController

from buckets.bucket_items import BucketListItems
from controllers.user_controller import UserAuth


class BucketListTestCase(unittest.TestCase):
    """Test Case for bucket controller methods

    """

    def setUp(self):
        self.buck = BucketController()
        self.auth = UserAuth()




    def test_create_bucket_list(self):
        """
        Tests that a bucket list is created
        """


        self.auth.add_user("Zack", "johndoe@gmail.com", "password")

        user = self.auth.list_of_users[0]
        # The initial length of the list of bucket lists
        initial = len(self.buck.bucket_list_dictionaries.get(user.email))
        #create a bucket list
        self.buck.create_bucket_list(user.email, "2017", "status")
        print(self.buck.create_bucket_list(user.email, "2017", "status"))
        # The new length of the list after bucket list is created
        new = len(self.buck.bucket_list_dictionaries.get(user.email))

        self.assertEqual(initial + 1, new)



    def test_add_bucket_item(self):
        """
        Tests that a bucket item is created

        """


        self.auth.add_user("Zack", "johndoe@gmail.com", "password")
        bucket = self.buck.create_bucket_list("johndoe@gmail.com", "new", "status")

        print(bucket)
        bucket_item = BucketListItems()

        bucket_item.create_bucket_items("Make something")
        created = self.buck.add_bucket_item("johndoe@gmail.com","new",bucket_item.name,bucket_item.completion_status)
        print(created)
        self.assertEqual(len(created),3)



if __name__ == '__main__':
    unittest.main()

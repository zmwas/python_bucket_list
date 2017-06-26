"""
This module tests bucket controller methods

"""

import unittest

from bucket_app.bucket_items import BucketListItems
from bucket_app.buckets import BucketList
from bucket_app.bucket_controller import BucketController
from bucket_app.bucket_items import BucketListItems
from bucket_app.user_controller import UserAuth


class BucketListTestCase(unittest.TestCase):
    """Test Case for bucket controller methods

    """

    def setUp(self):
        self.buck = BucketController()
        self.auth = UserAuth()

    def test_add_bucket_item(self):
        """
        Tests that a bucket item is created

        """

        self.auth.add_user("Zack", "johndoe@gmail.com", "password")
        list_of_buckets = self.buck.bucket_list_dictionaries.get("johndoe@gmail.com")
        bucket = BucketList()
        bucket.create_bucket_list("name", "status")
        list_of_buckets.append(bucket)

        bucket_item = BucketListItems("Make something")

        created = self.buck.add_bucket_item("johndoe@gmail.com", 0, bucket_item.name, bucket_item.completion_status)
        self.assertEqual(len(created), 3)

    def test_create_bucket(self):
        """
        Tests that a bucket is create

        """
        self.auth.add_user("Zack", "zackdoe@gmail.com", "password")
        list_of_buckets = self.buck.bucket_list_dictionaries.get("zackdoe@gmail.com")
        initial = len(list_of_buckets)
        buckets = self.buck.create_bucket("zackdoe@gmail.com", "name", "status")
        new = len(list_of_buckets)
        self.assertEqual(initial + 1, new)

    def test_delete_bucket(self):
        """
        Tests that a bucket is deleted

        """
        self.auth.add_user("Zack", "zack@awesome.com", "pass")
        list_of_buckets = self.buck.bucket_list_dictionaries.get("zack@awesome.com")
        buckets = self.buck.create_bucket("zack@awesome.com", "name", "state")
        list_of_buckets.append(buckets)
        initial = len(list_of_buckets)
        self.buck.delete_bucket("zack@awesome.com", 0)
        new = len(list_of_buckets)
        self.assertEqual(initial - 1, new)

    def test_view_single_bucket(self):
        """
        Tests that a bucket can be viewed

        """
        self.auth.add_user("Zack", "zack@great.com", "pass")
        list_of_buckets = self.buck.bucket_list_dictionaries.get("zack@great.com")
        buckets = self.buck.create_bucket("zack@great.com", "name", "state")
        list_of_buckets.append(buckets)
        bucket = self.buck.view_single_bucket("zack@great.com", 0)
        self.assertIsInstance(bucket, BucketList)

    def test_delete_bucket_item(self):
        """
        Test that a bucket list item can be viewed

        """
        user = self.auth.add_user("Zack", "zack@happy.com", "pass")
        list_of__buckets = self.buck.bucket_list_dictionaries.get("zack@happy.com")
        buckets = self.buck.create_bucket("zack@happy.com", " A name", "status")
        list_of__buckets.append(buckets)
        bucket_item = BucketListItems("Make something")
        self.buck.add_bucket_item("zack@happy.com", 0, bucket_item.name, bucket_item.completion_status)
        bucket_item = BucketListItems("Make something else")
        initial = len(self.buck.add_bucket_item("zack@happy.com", 0, bucket_item.name, bucket_item.completion_status))
        deleted = len(self.buck.delete_bucket_item("zack@happy.com", 0, "Make something"))
        self.assertEqual(initial - 1, deleted)


if __name__ == '__main__':
    unittest.main()

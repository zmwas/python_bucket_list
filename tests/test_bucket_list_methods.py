"""This module contains tests for bucket list methods

"""
import unittest

from bucket_app.buckets import BucketList


class TestBucket(unittest.TestCase):
    """TestCase class for BucketList.

    """

    def setUp(self):
        self.my_bucket = BucketList("My resolutions", "In Progress")

    def test_create_bucket_list_return(self):
        """
        Tests if a bucket list method is returned by the create bucket list method.

        """
        bucket = BucketList("", "")
        bucket = bucket.create_bucket_list("Name", "Completed")
        self.assertIsInstance(bucket, BucketList)

    def test_create_bucket_list_name(self):
        """
        Tests if the create bucket list method checks for a name

        """
        bucket = BucketList("", "")
        bucket = bucket.create_bucket_list("")
        self.assertEqual(bucket, "Please provide a name for your bucket list", )


if __name__ == '__main__':
    unittest.main()


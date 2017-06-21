"""This module contains tests for bucket list methods

"""
import unittest
from buckets.buckets import BucketList


class TestBucket(unittest.TestCase):
    """TestCase class for BucketList

    """

    def setUp(self):
        self.my_bucket = BucketList("My resolutions", "In Progress")

    def test_create_bucket_list_returns_bucket_list(self):
        bucket = BucketList("", "")
        bucket = bucket.create_bucket_list("Name", "Completed")
        self.assertIsInstance(bucket, BucketList)

    def test_create_bucket_list_checks_for_name(self):
        bucket = BucketList("", "")
        bucket = bucket.create_bucket_list("")
        self.assertEqual(bucket, "Please provide a name for your bucket list", )

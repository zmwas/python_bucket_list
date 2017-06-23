"""This module contains tests for bucket items
"""
import unittest
from buckets.bucket_items import  BucketListItems
class BucketItemsTestCase(unittest.TestCase):
    """
    Test Case for bucket item methods
    """

    def setUp(self):
        self.item = BucketListItems("name","In Progress")


    def test_create_bucket_item(self):
        """
        Tests that method can create a bucket list item

        """
        items = BucketListItems()
        self.assertIsInstance(items.create_item("Finish a gallon of yoghurt","In Progress"),BucketListItems)

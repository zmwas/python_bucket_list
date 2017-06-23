"""Module for Bucket items object and its methods

"""


class BucketListItems(object):
    """Class for the buckets

    Args
        name (str): Name of the bucket list item
        completion_status(str): How far one has gotten in the bucket list item

    Attributes
        name (str): Name of the bucket list item
        completion_status(str): How far one has gotten in the bucket list item

    """

    def __init__(self, name=None, completion_status="On Ice"):
        self.name = name
        self.completion_status = completion_status

    def update_bucket_item(self, name, completion_status):
        """
        Args
            name (str): Name of the bucketlist
            completion_status (str):  How far one has gotten in the bucket list. Defaults to On Ice
        Returns
            bucketlist(obj):Bucket list object

        """
        self.name = name
        self.completion_status = completion_status
        return self

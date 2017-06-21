"""Module for Bucket object and its methods

"""


class BucketList(object):
    """Class for the buckets

    Args
        list_id(int):Auto incrementing bucket list id
        name (str): Name of the bucket list
        completion_status(str): How far one has gotten in the bucket list

    Attributes
        name (str): Name of the bucket list
        completion_status(str): How far one has gotten in the bucket list

    """

    def __init__(self, list_id, name=None, completion_status=None):
        self.id = list_id
        self.name = name
        self.completion_status = completion_status

    def create_bucket_list(self, name, completion_status="On Ice"):
        """
        Args
            name (str): Name of the bucketlist
            completion_status (str):  How far one has gotten in the bucket list. Defaults to On Ice
        Returns
            bucketlist(obj):Bucket list object

        """
        if name == "":
            return "Please provide a name for your bucket list"

        self.name = name
        self.completion_status
        return self

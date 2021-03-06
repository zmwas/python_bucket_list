"""Module for Bucket object and its methods

"""


class BucketList(list):
    """Class for the buckets

    Args
        name (str): Name of the bucket list
        completion_status(str): How far one has gotten in the bucket list

    Attributes
        name (str): Name of the bucket list
        completion_status(str): How far one has gotten in the bucket list

    """

    def __init__(self, name=None, completion_status=None):
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
        self.completion_status = completion_status
        self.append(name)
        self.append(completion_status)
        return self

    def update_bucket_list(self, name, completion_status):
        """
        Args
            name (str): Name of the bucketlist
            completion_status (str):  How far one has gotten in the bucket list. Defaults to On Ice
        Returns
            bucketlist(obj):Bucket list object

        """
        self.name = name
        self.completion_status = completion_status
        self.append(name)
        self.append(completion_status)
        return self

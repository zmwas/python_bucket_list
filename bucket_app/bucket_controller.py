"""This module contains a class that creates bucket lists and bucket items

"""

from buckets import BucketList

from bucket_items import BucketListItems


class BucketController():
    """Class for bucket controller method that create bucket and bucket items.

    """

    # This is  a dictionary that contains the user email as the key and the user's list of bucket lists as the value
    bucket_list_dictionaries = {}

    def create_bucket(self, email, name, completion_status):
        """
        Args
            email (str): Email  of the user
            name (str): Name of the user
            completion_status(str): How far along you are in your bucket list
        Returns
            buckets (list): The list of the user's bucket list
        """

        bucketlist = BucketList()
        # Retrieve the list of a user's buckets given the email as the key
        buckets = self.bucket_list_dictionaries.get(email)
        # Check if the user already has bucket lists
        if buckets:
            for bucket in buckets:
                # If there exists a bucket list with a similar name return an error message
                if name == bucket[0]:
                    return "Try another name for your bucket"
            # Create a bucket list and append it to the user's list of bucket list
            bucketlist.create_bucket_list(name, completion_status)
            buckets.append(bucketlist)
        else:
            # Create a bucket list and append it to the user's list of bucket list if the user
            bucketlist.create_bucket_list(name, completion_status)
            buckets.append(bucketlist)

        return buckets

    def add_bucket_item(self, email, id, name, completion_status="On Ice"):
        """
        Args
            email (str): Email  of the user
            id (int): The id of the bucket list you want to add the item in
            name (str): Name of the bucket item
            completion_status(str): Whether a task is completed or not
        Returns
            single_bucket (list): The list of the bucket items
        """

        bucket_item = BucketListItems(name, completion_status)
        # Retrieve the list of a user's buckets given the email as the key
        buckets = self.bucket_list_dictionaries.get(email)
        # Retrieve a single bucket list given the index of the list
        single_bucket = buckets[id]
        # Add an item to the bucket list
        single_bucket.append(bucket_item)

        return single_bucket

    def view_single_bucket(self, email, id):
        """
        Args
            email (str): Email  of the user
            id (int): The id of the bucket list you want to view

        Returns
            single_bucket (list): The list of the bucket items
        """
        buckets = self.bucket_list_dictionaries.get(email)
        bucket = buckets[id]
        return bucket

    def delete_bucket(self, email, id):
        """
        Args
            email (str): Email  of the user
            id (int): The id of the bucket list you want to delete

        Returns
            buckets (list): The list of the bucket items
        """

        buckets = self.bucket_list_dictionaries.get(email)
        # Retrieve a single bucket list given the index of the list
        bucket = buckets[id]
        buckets.remove(bucket)
        return buckets

    def delete_bucket_item(self, email, id, name):
        """
       Args
           email (str): Email  of the user
           id (int): The id of the bucket list you want to delete

       Returns
           bucket (list): The list of the  items after an item is removed
       """
        buckets = self.bucket_list_dictionaries.get(email)
        # Retrieve a single bucket
        bucket = buckets[id]
        print(bucket)
        # Looop through the items and find the item matching the name
        for item in bucket[2:]:
            print(item)
            if name == item.name:
                bucket.remove(item)

        print(bucket)
        return bucket

    def update_bucket(self, email, id, name, completion_status):
        """
        Args
            email (str): Email  of the user
            id (int): The id of the bucket list you want to delete
            name (str): Name of the bucket item
            completion_status(str): Whether a task is completed or not

        Returns
            buckets (list): The list of the bucket items
        """

        buckets = self.bucket_list_dictionaries.get(email)
        # Retrieve a single bucket list given the index of the list
        bucket = buckets[id]
        bucket[0]=name
        bucket[1]=completion_status
        print(name)
        print(completion_status)
        return bucket

    def update_bucket_item(self, email, id,old_name, name, completion_status):
        """
       Args
           email (str): Email  of the user
           id (int): The id of the bucket list you want to delete

       Returns
           bucket (list): The list of the  items after an item is updated
       """
        buckets = self.bucket_list_dictionaries.get(email)
        # Retrieve a single bucket
        bucket = buckets[id]
        print(bucket)
        # Looop through the items and find the item matching the name
        for item in bucket[2:]:
            if old_name ==item.name:
                item.update_bucket_item(name, completion_status)

        print(bucket)
        return bucket

from user_controller import UserAuth
from buckets.buckets import BucketList
from buckets.bucket_items import BucketListItems


class BucketController():
    bucket_list_dictionaries = {}

    def create_bucket_directory(self):
        auth = UserAuth()
        users = auth.list_of_users

        for user in users:
            self.bucket_list_dictionaries.setdefault(user.email, [])

        return self.bucket_list_dictionaries

    def create_bucket_list(self,email ,name, completion_status):
        bucketlist = BucketList()
        bucketlist.create_bucket_list(name, completion_status)
        buckets= self.bucket_list_dictionaries.get(email)
        buckets.append(bucketlist)
        return buckets


    def add_bucket_item(self,email,bucket_name,name,completion_status):
        bucket_item = BucketListItems()
        bucket_item.create_bucket_items(name,completion_status)

        buckets= self.bucket_list_dictionaries.get(email)
        for bucket in buckets:
            if bucket_name == bucket[0]:
                bucket.append(bucket_item)


                return bucket





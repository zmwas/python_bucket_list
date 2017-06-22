from buckets.bucket_items import BucketListItems
from buckets.buckets import BucketList


class BucketController():
    bucket_list_dictionaries = {}

    def create_bucket(self, email, name, completion_status):
        bucketlist = BucketList()
        buckets = self.bucket_list_dictionaries.get(email)
        if buckets:
            for bucket in buckets:
                print(bucket)
                if name == bucket[0]:
                    return "Try another name for your bucket"

            bucketlist.create_bucket_list(name, completion_status)
            buckets.append(bucketlist)
        else:
            bucketlist.create_bucket_list(name, completion_status)
            buckets.append(bucketlist)

        return buckets

    def add_bucket_item(self, email, bucket_name, name, completion_status):
        bucket_item = BucketListItems()
        bucket_item.create_bucket_items(name, completion_status)
        buckets = self.bucket_list_dictionaries.get(email)
        print(self.bucket_list_dictionaries.__dict__)
        for bucket in buckets:
            if bucket_name == bucket[0]:
                bucket.append(bucket_item)
                return bucket

        return bucket

    def view_single_bucket(self,email,id):
        buckets = self.bucket_list_dictionaries.get(email)
        bucket=buckets[id]
        return bucket

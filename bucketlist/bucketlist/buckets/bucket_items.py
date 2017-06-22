


class BucketListItems(object):


    def __init__(self,name=None,completion_status="On Ice"):
        self.name = name
        self.completion_status = completion_status



    def create_bucket_items(self,name,completion_status="On Ice"):
        self.name = name



    def update_bucket_item(self,name,completion_status):
        self.name = name
        self.completion_status = completion_status





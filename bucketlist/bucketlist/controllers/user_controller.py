"""This module contains methods for registering and logging in users

"""
# list where users are added on registration

from accounts.bucket_user import BucketUser
from controllers.bucket_controller import BucketController


class UserAuth():
    list_of_users = []
    current_user=BucketUser()

    def add_user(self, name, email, password):
        users = self.list_of_users
        for user in users:
            if email == user.email:

                # break
                return "That email is taken"


        user = BucketUser()
        user.create_user(name, email)
        user.set_password(password)
        users.append(user)
        bucket_controller = BucketController()
        directory_entry = bucket_controller.bucket_list_dictionaries[user.email] = []


        return users


    def login(self,email,password):
        users = self.list_of_users

        for user in users:
            if email == user.email and password == user.get_password():
                user.is_logged_in = True
                self.current_user= user
                print(self.current_user.__dict__)
                print(self.current_user.email)
                return "Welcome"

            else:
                return "Wrong email or password"



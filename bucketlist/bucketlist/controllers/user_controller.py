"""This module contains methods for registering and logging in users

"""
# list where users are added on registration

from accounts.bucket_user import BucketUser


class UserAuth():
    list_of_users = []

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

        return users


    def login(self,email,password):
        users = self.list_of_users

        for user in self.list_of_users:
            if email == user.email and password == user.get_password():
                return "Welcome"

            else:
                return "Wrong email or password"

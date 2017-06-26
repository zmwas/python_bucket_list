"""This module contains methods for registering and logging in users

"""

from accounts.bucket_user import BucketUser
from controllers.bucket_controller import BucketController


class UserAuth():
    # List where users are added on registration
    list_of_users = []
    # Class variable for checking the user who is logged in. It is set in the log in method
    current_user = BucketUser()

    def add_user(self, name, email, password):
        """
        Args
            name (str): Name of the user
            email (str): Email for the user
            password (str): Password provided by the user
        Returns
            users (list): New list of users after registration
        """
        users = self.list_of_users
        for user in users:
            if email == user.email:
                # break
                return "That email is taken"

        user = BucketUser()
        user.create_user(name, email)
        user.set_password(password)
        self.list_of_users.append(user)
        bucket_controller = BucketController()
        directory_entry = bucket_controller.bucket_list_dictionaries[user.email] = []

        return users

    def login(self, email, password):
        """
        Args
            email (str): Email for the user
            password (str): Password provided by the user
        Returns
            message (str): Message returned on log in
        """
        # Get the list of users registered
        message = ""
        users =self.list_of_users
        for user in users:
            # Loop through each user and check for one who matches the email and password provided
            if email == user.email and password == user.get_password():
                user.is_logged_in = True
                self.current_user = user
                message = "Welcome"
                return message

            else:
                message = "Wrong email or password"
                print(user.email)
                print(user.get_password())
                return message

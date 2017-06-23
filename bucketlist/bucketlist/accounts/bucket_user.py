"""Module for BucketUser and user methods
"""


class BucketUser(object):
    """Class for the user

        Args:
            name (str): Name of the user
            email (str): Email of the user

        Attributes:
            name (str): Name of the user
            email (str): Email of the user

    """

    __password = ""
    def __init__(self,name=None, email=None, is_logged_in=False):
        self.name = name
        self.email = email
        self.__password = ""
        self.is_logged_in = is_logged_in

    def create_user(self, name, email):
        """
        Args
            name (str): Name of the user
            email (str): Email for the user
        Returns
            user (obj): User object
        """
        if email == "":
            return 'Please provide an email'
        elif name == "":
            return 'Please provide your name'
        self.name = name
        self.email = email
        return self

    def set_password(self, password):
        """
        Args
            password (str): Password for the user
        Returns
            True (bool): True if password is set. Otherwise False
        """

        self.__password = password
        return True



    def get_password(self):
        return self.__password
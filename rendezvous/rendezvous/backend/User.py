"""
User

Holds information about a user.
Their name, their
"""


class User:
    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__username = ""

    def get_first_name(self):
        """
        Gets the first name of the user
        :return: First name of user
        """
        return self.__first_name

    def get_last_name(self):
        """
        Gets the last name of the user
        :return: Last name of user
        """
        return self.__last_name

    def get_username(self):
        """
        Gets the username of the user
        :return: User's username
        """

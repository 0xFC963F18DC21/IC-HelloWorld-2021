"""
User

Holds information about a user.
Their name, their
"""


class User:
    __next_id: int = 0

    def __init__(self, first_name: str = "", last_name: str = "", username: str = "", spotify_access_token: str = ""):
        self.__user_id = User.__next_id
        User.__next_id += 1

        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__spotify_access_token = spotify_access_token

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

    def get_spotify_access_token(self):
        return self.__spotify_access_token

    def set_first_name(self, first_name: str = ""):
        self.__first_name = first_name

    def set_last_name(self, last_name: str = ""):
        self.__last_name = last_name

    def set_username(self, username: str = ""):
        self.__username = username

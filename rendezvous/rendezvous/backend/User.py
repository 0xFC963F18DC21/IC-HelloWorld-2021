"""
User

Holds information about a user.
Their name, their
"""


class User:
    __next_id: int = 0

    def __init__(self, first_name: str = "", last_name: str = "", username: str = "", spotify_access_token: str = ""):
        """
        Create a new user
        :param first_name: User's first name
        :param last_name: User's last name
        :param username: User's username
        :param spotify_access_token: User's spotify access token
        """
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
        """
        Gets the user's spotify access token. BE CAREFUL WITH WHAT USES THIS API.
        :return: User's spotify access token
        """
        return self.__spotify_access_token

    def set_first_name(self, first_name: str = ""):
        """
        Set a new first name for this user
        :param first_name: New first name for the user
        """
        self.__first_name = first_name

    def set_last_name(self, last_name: str = ""):
        """
        Set a new last name for this user
        :param last_name: New last name for this user
        """
        self.__last_name = last_name

    def set_username(self, username: str = ""):
        """
        Set a new username for this user
        :param username: New username for this user
        """
        self.__username = username

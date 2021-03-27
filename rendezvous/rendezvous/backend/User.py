"""
User

Holds information about a user.
Their name, their username, etc.
"""

import time
import uuid
from pwd import pwd_hash


class User:
    def __init__(self, first_name: str = "", last_name: str = "", username: str = "", password: str = "", spotify_access_token: str = ""):
        """
        Create a new user
        :param first_name: User's first name
        :param last_name: User's last name
        :param username: User's username
        :param password: User's initial password, DO NOT STORE AS PLAINTEXT
        :param spotify_access_token: User's spotify access token
        """
        self.__user_uuid = str(uuid.uuid4())
        self.__toc = str(time.time())

        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__spotify_access_token = spotify_access_token

        self.__password = pwd_hash(self.__toc + password + self.__user_uuid)

    def try_login(self, password: str = "") -> bool:
        """
        Attempt a login with a password
        :param password: Given password
        :return: True if successful, False otherwise
        """
        return pwd_hash(self.__toc + password + self.__user_uuid) == self.__password

    def get_user_uuid(self) -> str:
        """
        Gets the current user's unique id
        :return: User's unique id
        """
        return self.__user_uuid

    def get_first_name(self) -> str:
        """
        Gets the first name of the user
        :return: First name of user
        """
        return self.__first_name

    def get_last_name(self) -> str:
        """
        Gets the last name of the user
        :return: Last name of user
        """
        return self.__last_name

    def get_username(self) -> str:
        """
        Gets the username of the user
        :return: User's username
        """

    def get_spotify_access_token(self) -> str:
        """
        Gets the user's spotify access token. BE CAREFUL WITH WHAT USES THIS API.
        :return: User's spotify access token
        """
        return self.__spotify_access_token

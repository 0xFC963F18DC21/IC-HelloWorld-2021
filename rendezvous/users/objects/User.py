"""
User

Holds information about a user.
Their name, their username, etc.
"""

import time
import uuid
from pwd import pwd_hash


class User:
    def __init__(
        self, first_name: str = "", last_name: str = "", username: str = "",
        password: str = "", spotify_refresh_code: str = "",
        spotify_access_code: str = ""
    ):
        """
        Create a new user.
        This assumes that the access code is initially fetched at the same time as the user is created.
        :param first_name: User's first name
        :param last_name: User's last name
        :param username: User's username
        :param password: User's initial password, DO NOT STORE AS PLAINTEXT
        :param spotify_refresh_code: User's spotify refresh code
        :param spotify_access_code: User's temporary access code
        """
        self.__user_uuid = str(uuid.uuid4())
        self.__toc = str(time.time())

        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__spotify_refresh_code = spotify_refresh_code
        self.__spotify_access_code = spotify_access_code
        self.__last_access_fetch = float(self.__toc)

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
        return self.__username

    def get_spotify_refresh_code(self) -> str:
        """
        Gets the user's permanent spotify refresh code.
        BE CAREFUL WITH WHAT USES THIS API.
        :return: User's permanent spotify refresh code
        """
        return self.__spotify_refresh_code

    def get_spotify_access_code(self) -> str:
        """
        Gets the user's short-lived spotify access code.
        BE CAREFUL WITH WHAT USES THIS API.
        :return: User's short-lived spotify access code
        """
        if time.time() - self.__last_access_fetch > 3600.0:
            raise RuntimeWarning("The access code is likely invalid!")

        return self.__spotify_access_code

    def set_spotify_access_code(self, spotify_access_code: str = ""):
        """
        Gets this user's short-lived spotify access token.
        :param spotify_access_code:
        """
        self.__spotify_access_code = spotify_access_code
        self.__last_access_fetch = time.time()

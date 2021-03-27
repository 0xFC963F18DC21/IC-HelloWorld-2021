"""
pwd

Small, rudimentary hashing module so that the same hashing function is used everywhere.
"""

import hashlib


def pwd_hash(string: str) -> str:
    """
    Single, standard hashing method used to store a password
    :param string: String to hash
    :return: Hex representation of string hash
    """
    md = hashlib.sha512()
    md.update(string)
    return md.hexdigest()

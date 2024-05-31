#!/usr/bin/env python3
"""
authentication package
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """
    takes in password string
    Returns:
        bytes
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def _generate_uuid():
    """
    return a string uuid
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register a user
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {user.email} already exists")
        except NoResultFound:
            hsh_pass = _hash_password(password)
            new_user = self._db.add_user(email=email, hashed_password=hsh_pass)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        validate login
        """
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password
            if user:
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    return True
                else:
                    return False
            else:
                return False
        except NoResultFound:
            return False

#!/usr/bin/env python3
"""
authentication package
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    takes in password string
    Returns:
        bytes
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

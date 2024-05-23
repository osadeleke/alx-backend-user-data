#!/usr/bin/env python3
"""
basic authentication module
"""
import base64
from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """
    class for basic authentication/authorization
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        get base 64 
        authorization header value
        """
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        substring = "Basic "
        if substring in authorization_header:
            return authorization_header[6:]
        else:
            return None

    def decode_base64_authorization_header(self, base_64_authorization_header: str) -> str:
        """
        decode base 64
        authorization header
        """
        if not base_64_authorization_header:
            return None
        if not isinstance(base_64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base_64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except base64.binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        get user credential
        from basic authorization
        """
        if not decoded_base64_authorization_header:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        details = decoded_base64_authorization_header.split(':')
        return details[0], details[1]

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        returns the user instance based on
        his/her email and password
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

#!/usr/bin/env python3
"""basic authentication module"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class for basic authentication"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:  # noqa: E501
        """
        get base 64 authorization header value
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

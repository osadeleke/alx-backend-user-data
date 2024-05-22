#!/usr/bin/env python3
""" Authentication module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method for requiring authentication
        """
        if not path or not excluded_paths:
            return True

        normalized_path = path.rstrip('/')

        for excluded_path in excluded_paths:
            if normalized_path == excluded_path.rstrip('/'):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization header method"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user method"""
        return None

#!/usr/bin/env python3
"""
Session Authentication Module
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    Session Authentication Class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Module create a session
        Returns:
            session id (str)
        """
        if not user_id:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Method to get user from session id
        """
        if not session_id:
            return None
        if not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """
        Method returns a user based on cookie
        """
        auth_cookie = self.session_cookie(request)
        print(f'auth cookie is {auth_cookie}')
        auth_user_id = self.user_id_for_session_id(auth_cookie)
        print(f'auth user id is {auth_user_id}')
        user = User.get(auth_user_id)
        print(user)
        return user

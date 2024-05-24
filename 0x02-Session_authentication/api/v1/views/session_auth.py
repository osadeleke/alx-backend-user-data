#!/usr/bin/env python3
"""
Session authentication view
"""
from api.v1.views import app_views
from flask import request, jsonify, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """
    Handle session login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    list_user = User.search({'email': email})
    if not list_user:
        return jsonify({"error": "no user found for this email"}), 404
    user = list_user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    out = make_response(user.to_json())
    cookie_name = os.getenv('SESSION_NAME')
    out.set_cookie(cookie_name, session_id)
    return out

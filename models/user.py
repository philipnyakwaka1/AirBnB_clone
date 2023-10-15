#!/usr/bin/python3
"""This is module defines the user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the user class
    Attributes:
        email (str): user's email
        password (str): user's password
        first_name (str): user's firstname
        last_name (str): user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
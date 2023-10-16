#!/usr/bin/python3
"""This is module defines the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is the Review class
    Attributes:
        place_id (str): place's id
        user_id (str): user's id
    """

    place_id = ""
    user_id = ""
    text = ""

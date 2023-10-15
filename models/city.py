#!/usr/bin/python3
"""This is module defines the City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This is the City class
    Attributes:
        state_id (str): This is the state id
        name (str): city's name
    """

    state_id = ""
    name = ""

#!/usr/bin/python3
"""This is module defines the state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    This is the State class
    Attributes:
        name (str): name of state
    """
    name = ""
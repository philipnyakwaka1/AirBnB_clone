#!/usr/bin/python3
"""This is module defines the Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    This is the Place class
    Attributes:
        city_id (str): city's id
        user_id (str): user's id
        name (str): place's name
        description (str): place's description
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): price per night
        latitude (float): place's latitude
        longitude (float): place's longitude
        amenity_ids (list of strings): list of amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
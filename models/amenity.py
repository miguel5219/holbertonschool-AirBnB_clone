#!/usr/bin/python3
"""
module contains that class Amenity that
inherits from class BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    define Amenity

        attribute:
            name: the name of the amenity
    """
    name = ""

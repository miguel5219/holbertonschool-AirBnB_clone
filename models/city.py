#!/usr/bin/python3
""" module contains the class city that
inherits from class BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """define city

        attribute:
            name: the name of the city
    """

    state_id = ""
    name = ""

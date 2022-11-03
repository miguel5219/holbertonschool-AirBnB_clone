#!/usr/bin/python3
""" module contains the class state that
inherits from class BaseModel"""


from models.base_model import BaseModel


class State(BaseModel):
    """ define state

        attribute:
            name: the name of the states
    """

    name = ""

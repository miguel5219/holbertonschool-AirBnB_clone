#!/usr/bin/python3
"""
This module contains the User that
inherits from class BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Define the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

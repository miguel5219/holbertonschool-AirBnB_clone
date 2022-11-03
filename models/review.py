#!/usr/bin/python3
"""
module contains the class review that
inherits from class BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    define Review

        attributes:
            place_id: the id of the place of the review
            user_id: the id of the user of the review
            text: the text of the review
    """

    place_id = ""
    user_id = ""
    text = ""

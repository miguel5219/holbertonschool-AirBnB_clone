#!/usr/bin/python3
"""
module containsthe class Place that
inherits from class BaseModel
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """ define Place

    attribute:
        city_id: the id of the city
        user_id: the id of the user
        name: the name of the place
        description: a descripition of the place
        number_rooms: the numbers of the rooms of the place
        number_bathrooms: the number of the bathrooms of the place
        max_guest: the maximum number of guests allowed in the place
        price_by_night: price for each night in the place
        latitude: the latitud of the location of the place
        longitude: the longitude of the locatio of the place
        amenity_ids: the list containing the ids of the amenities
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0)
    longitude = float(0)
    amenity_ids = []

#!/usr/bin/python3
"""
Unittest for class Place
"""
import unittest
from models.place import Place
from datetime import datetime
import os


class TestPlace(unittest.TestCase):

    def test_place_city_id(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'city_id'))
        self.assertEqual(place1.city_id, "")
        place1.city_id = "051051"
        self.assertEqual(place1.city_id, "051051")

    def test_place_user_id(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'user_id'))
        self.assertEqual(place1.user_id, "")
        place1.user_id = "1038807923"
        self.assertEqual(place1.user_id, "1038807923")

    def test_place_name(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'name'))
        self.assertEqual(place1.name, "")
        place1.name = "Holbie House"
        self.assertEqual(place1.name, "Holbie House")

    def test_place_description(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'description'))
        self.assertEqual(place1.description, "")
        place1.description = "Excelent"
        self.assertEqual(place1.description, "Excelent")

    def test_place_number_rooms(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'number_rooms'))
        self.assertEqual(place1.number_rooms, 0)
        place1.number_rooms = 5
        self.assertEqual(place1.number_rooms, 5)

    def test_place_number_bathrooms(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'number_bathrooms'))
        self.assertEqual(place1.number_bathrooms, 0)
        place1.number_bathrooms = 2
        self.assertEqual(place1.number_bathrooms, 2)

    def test_place_max_guests(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'max_guest'))
        self.assertEqual(place1.max_guest, 0)
        place1.max_guest = 8
        self.assertEqual(place1.max_guest, 8)

    def test_place_price_by_night(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'price_by_night'))
        self.assertEqual(place1.price_by_night, 0)
        place1.price_by_night = 240000
        self.assertEqual(place1.price_by_night, 240000)

    def test_place_longitude(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'longitude'))
        self.assertEqual(place1.longitude, float(0))
        place1.longitude = 15.2
        self.assertEqual(place1.longitude, 15.2)

    def test_place_latitude(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'latitude'))
        self.assertEqual(place1.latitude, float(0))
        place1.latitude = 8.5
        self.assertEqual(place1.latitude, 8.5)

    def test_place_amenity_ids(self):

        place1 = Place()
        self.assertTrue(hasattr(place1, 'amenity_ids'))
        self.assertEqual(place1.amenity_ids, [])
        place1.amenity_ids = ["1", "2", "3"]
        self.assertEqual(place1.amenity_ids, ["1", "2", "3"])

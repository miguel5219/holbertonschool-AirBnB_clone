#!/usr/bin/python3
""" Unittest for class Amenity """

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity_name(self):
        review = Amenity()
        self.assertTrue(hasattr(review, 'name'))
        self.assertEqual(review.name, "")
        review.name = "mirador de san felix"
        self.assertEqual(review.name, "mirador de san felix")

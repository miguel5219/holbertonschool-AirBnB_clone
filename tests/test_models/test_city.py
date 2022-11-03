#!/usr/bin/python3
""" Unittest for class City """

import unittest
from models.city import City
from datetime import datetime
import os


class TestCity(unittest.TestCase):

    def test_city_name(self):

        city_ = City()
        self.assertTrue(hasattr(city_, 'name'))
        self.assertEqual(city_.name, "")
        city_.name = "Envigado"
        self.assertEqual(city_.name, "Envigado")

    def test_city_state_id(self):

        city_ = City()
        self.assertTrue(hasattr(city_, 'state_id'))
        self.assertEqual(city_.state_id, "")
        city_.state_id = "0400"
        self.assertEqual(city_.state_id, "0400")

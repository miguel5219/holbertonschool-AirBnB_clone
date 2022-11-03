#!/usr/bin/python3
""" Unittest for class State """

import unittest
from models.state import State
from datetime import datetime
import os


class TestState(unittest.TestCase):

    def test_state_name(self):

        state_ = State()
        self.assertTrue(hasattr(state_, 'name'))
        self.assertEqual(state_.name, "")
        state_.name = "Medellin"
        self.assertEqual(state_.name, "Medellin")

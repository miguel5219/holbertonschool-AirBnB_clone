#!/usr/bin/python3
"""
Unittest for class User
"""
import unittest
from models.user import User
from datetime import datetime
import os


class TestUser(unittest.TestCase):

    def test_user_email(self):

        user1 = User()
        self.assertTrue(hasattr(user1, 'email'))
        self.assertEqual(User.email, "")
        user1.email = "jhonatan.ramox@gmail.com"
        self.assertEqual(user1.email, "jhonatan.ramox@gmail.com")

    def test_user_password(self):
        user1 = User()
        self.assertTrue(hasattr(user1, 'password'))
        self.assertEqual(User.password, "")
        user1.password = "mxncbv"

    def test_user_first_name(self):

        user1 = User()
        self.assertTrue(hasattr(user1, 'first_name'))
        self.assertEqual(User.first_name, "")
        user1.first_name = "Jhonatan"
        self.assertEqual(user1.first_name, "Jhonatan") 

    def test_user_last_name(self):
    
        user1 = User()
        self.assertTrue(hasattr(user1, 'last_name'))
        self.assertEqual(User.last_name, "")
        user1.last_name = "Ramos"
        self.assertEqual(user1.last_name, "Ramos")

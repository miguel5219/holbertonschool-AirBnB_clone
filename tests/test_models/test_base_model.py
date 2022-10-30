#!/usr/bin/python3
""" Test for task 3"""


from models.base_model import BaseModel
import unittest


class TestsBaseModel(unittest.TestCase):

    def setUp(self):
        self.instanceOne = BaseModel()
        self.instanceTwo = BaseModel()

    def testBaseModel(self):
        myModelOne = self.instanceOne.updated_at
        self.instanceOne.save()
        myModelTwo = self.instanceOne.updated_at
        self.assertNotEqual(myModelOne, myModelTwo)

    def testId(self):
        self.assertNotEqual(self.instanceOne.id, self.instanceTwo.id)

    def testDict(self):
        self.assertIn("id", self.instanceOne.to_dict())
        self.assertIn("__class__", self.instanceOne.to_dict())
        self.assertIn("created_at", self.instanceOne.to_dict())
        self.assertIn("updated_at", self.instanceOne.to_dict())

    def testStr(self):
        self.assertIsInstance(self.instanceOne.__str__(), str)
        self.assertIn(self.instanceOne.id, self.instanceOne.__str__())
        self.assertIn(type(self.instanceOne).__name__,
                        self.instanceOne.__str__())

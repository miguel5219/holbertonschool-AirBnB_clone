#!/usr/bin/python3
""" test for task 3"""


from abc import update_abstractmethods
from models.basemodel import BaseModel
from datetime import datetime
import unittest


class TestsBaseModel(unittest.TestCase):
    def testBm(self):
        myModel = BaseModel()
        bm = myModel.update_at
        bm = save()
        myModel1 = bm.update_at
        self.assertNotEqual(myModel, myModel)

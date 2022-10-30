#!/usr/bin/python3
'''
This file is an unittest for class FileStore
'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestsFileStorage(unittest.TestCase):

    def testFileStorage(self):
        dictOne = FileStorage.all(self)
        self.assertIsInstance(dictOne, dict)
        self.assertEqual(len(dictOne), 0)
        instanceBase = BaseModel()
        self.assertGreater(len(dictOne), 0)

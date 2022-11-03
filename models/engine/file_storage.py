#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file
    and deserilizes JSON file to instances
"""

import json
import os.path
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """class FileStorage that serializes instances to a JSON file
        and deserilizes JSON file to instances

    attributes:
        __file_path: path to the JSON file
        __objects: dictionary that will store all
        objects by <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ method that returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        method that set s the obj in __objects with key
        <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
            method that serializes __objects to
            the JSON file
        """
        new_dict = {k: v.to_dict() for k, v in self.all().items()}
        with open(FileStorage.__file_path, mode="w+", encoding="UTF-8") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """
        method that deserialize the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                dictionary = f.read()

            py_obj = json.loads(dictionary)
            FileStorage.__objects = {k: eval(f"{v['__class__']}(**{v})")
                                     for k, v in py_obj.items()}

#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file
    and deserilizes JSON file to instances
"""

import json
import os.path
from models.base_model import BaseModel


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
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
            method that serializes __objects to
            the JSON file
        """
        with open(FileStorage.__file_path, mode="w", encoding="UFT-8") as f:
            new_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dumps(new_dict, f, indent=4)

    def reload(self):
        """
        method that deserialize the JSON file to __objects
        """
        from models.base_model import BaseModel
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                dictionary = json.load(f)
                for k, v in dictionary.items():
                    obj = eval(v["__class__"])(**V)
                    FileStorage.__objects[k] = obj
        else:
            return

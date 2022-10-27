#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file
    and deserilizes JSON file to instances
"""

import json
import os


class FileStorage():
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
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
            method that serializes __objects to
            the JSON file
        """

        with open(FileStorage.__file_path, "w+") as f:
            new_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """
        method that deserialize the JSON file to __objects
        """
        try:
            dictionary = {}
            with open(FileStorage.__file_path, "r") as f:
                dictionary = json.load(f)

                for i, j in dictionary.items():
                    self.all()[i] = classes[j['__class__']](**j)
        except FileNotFoundError:
            pass

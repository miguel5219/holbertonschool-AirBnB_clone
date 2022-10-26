#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file
    and deserilizes JSON file to instances
"""

import json
from os.path import exists

class FileStorage():
    """class FileStorage that serializes instances to a JSON file
        and deserilizes JSON file to instances

    attributes:
        __file_path: path to the JSON file
        __objects: dictionary that will store all
        objects by <class name>.id
    """
    __file_path = ""
    __objects = {}

    def all(self):
        """ method that returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        method that set s the obj in __objects with key
        <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
            method that serializes __objects to
            the JSON file
        """
        save_dict = {}

        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(save_dict, f)

    def reload(self):
        """
        method that deserialize the JSON file to __objects
        """
        if exists(self.__file_path):
            try:
                with open(self.__file_path, mode="r", encoding="utf-8") as f:
                    str_json = f.read()
                    dictionary = json.loads(str_json)

                    for i, j in dictionary.items():
                        self.__objects[i] = eval(f"{j.get('__class__')}(**j")
            except Exception:
                pass

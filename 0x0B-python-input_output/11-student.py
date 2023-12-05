#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        for x, r in json.items():
            setattr(self, x, r)

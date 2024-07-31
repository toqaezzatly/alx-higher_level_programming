#!/usr/bin/python3

"""
Contains the class BaseGeometry
"""

class BaseGeometry:
    """ A Class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

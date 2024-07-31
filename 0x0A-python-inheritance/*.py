#!/usr/bin/python3
==> 0-lookup.py <==
"""
contains the lookup function
"""

def lookup(obj):
    """returs the attributes of an obj"""
    return dir(obj)

==> 100-my_int.py <==
"""
Contains the class MyInt
"""


class MyInt(int):
    """rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other

==> 101-add_attribute.py <==
#!/usr/bin/python3
""" A attribute adding module """


def add_attribute(a_class, name, value):
    """ Adds a new attribute to an object if it’s possible """
    if hasattr(a_class, "__dict__"):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attribute")

==> 10-square.py <==
"""
Contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2

==> 11-square.py <==
"""
Contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

==> 1-my_list.py <==
""" My list module """


class MyList(list):
    """ Class that inherits from list """
    def print_sorted(self):
        """ Prints sorted lists """
        print(sorted(self.copy()))

==> 2-is_same_class.py <==

"""
This module contains the function is_same_class
"""

def is_same_class(obj, a_claa):
    """ returns true if obj is the exact class a_class, otherwise false"""
    return(type(obj) == a_class)

==> 3-is_kind_of_class.py <==
"""
Contains the is_kind_of_class function
"""
def is_kind_of_class(obj, a_class):
    """ True if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))

==> 4-inherits_from.py <==
"""
contains the inherits_from from
"""

def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)

==> 5-base_geometry.py <==
"""
contains the class BaseGeometry
"""

class BaseGeometry:
    """ An Empty class"""
    pass

==> 6-base_geometry.py <==

"""
Contains the class BaseGeometry
"""

class BaseGeometry:
    """ A Class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

==> 7-base_geometry.py <==
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

==> 8-rectangle.py <==
"""
Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

==> 9-rectangle.py <==
"""
Contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

==> *.py <==
#!/usr/bin/python3

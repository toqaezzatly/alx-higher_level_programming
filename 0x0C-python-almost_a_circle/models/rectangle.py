#!/usr/bin/python3
# models/rectangle.py
from base import Base
class Rectangle(Base):
    """
    Rectangle class that inherits from Base

    Args:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        x (int, optional): X-coordinate of the rectangle (default: 0)
        y (int, optional): Y-coordinate of the rectangle (default: 0)
        id (int, optional): ID of the rectangle (inherited from Base)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializer for the Rectangle class

        Calls the superclass constructor (Base) and assigns attributes.
        """
        super().__init__(id)  # Call Base class constructor with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute (validates value)"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute (validates value)"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be a positive integer")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute (validates value)"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute (validates value)"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        self.__x = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of the Rectangle object"""
        return f"[Rectangle] ({self.id}) - x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}"

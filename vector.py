"""
For Vector operations
"""

from math import acos
from math import degrees
from math import sqrt
from numbers import Number

class Vector(object):
    """
    Creates vector instances and allows for operations
    """
    def __init__(self, coordinates):
        self.coordinates = tuple(coordinates)

    def __str__(self):
        return str(self.coordinates)

    def __add__(self, other):
        s_coor = self.coordinates
        o_coor = other.coordinates
        if len(s_coor) != len(o_coor):
            raise ValueError("Different length coordinates")
        result = [sum(x) for x in zip(s_coor, o_coor)]
        return Vector(result)

    def __sub__(self, other):
        s_coor = self.coordinates
        o_coor = other.coordinates
        if len(s_coor) != len(o_coor):
            raise ValueError("Different length coordinates")
        result = [x - y for x, y in zip(s_coor, o_coor)]
        return Vector(result)

    def __mul__(self, scalar):
        if not isinstance(scalar, Number):
            raise ValueError("Scalar needs to be a scalar")
        s_coor = self.coordinates
        result = [scalar * x for x in s_coor]
        return Vector(result)

    def _square(self, num):
        return pow(num, 2)

    def magnitude(self):
        """Return magnitude of vector"""
        return sqrt(sum(map(self._square, self.coordinates)))

    def normalize(self):
        """Return unit vector of vector"""
        mag = self.magnitude()
        try:
            return self * (1. / mag)
        except ZeroDivisionError:
            raise Exception("Cannot divide by zero")

    def dot_product(self, other):
        """Return dot product of two vectors"""
        if not isinstance(other, Vector):
            return Exception("Not a vector")
        s_coor = self.coordinates
        o_coor = other.coordinates
        result = [x * y for x, y in zip(s_coor, o_coor)]
        return sum(result)

    def angle_with(self, other, in_degrees=False):
        """Returns angle between two vectors, default in radians"""
        if not isinstance(other, Vector):
            return Exception("Not a vector")
        dot = self.dot_product(other)
        mag_product = self.magnitude() * other.magnitude()
        try:
            angle_val = acos(float(dot) / mag_product)
            if in_degrees:
                return degrees(angle_val)
            return angle_val
        except ZeroDivisionError:
            raise Exception("Cannot divide by zero")

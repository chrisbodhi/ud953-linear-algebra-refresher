"""
For Vector operations
"""

from math import acos
from math import degrees
from math import pi
from math import sqrt
from decimal import Decimal, getcontext
from numbers import Number

getcontext().prec = 30


class Vector(object):
    """
    Creates vector instances and allows for operations
    """
    def __init__(self, coordinates):
        self.coordinates = tuple([Decimal(str(x)) for x in coordinates])
        self.dimension = len(self.coordinates)

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
            return self * Decimal(1.0 / mag)
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

    def is_zero(self):
        """Returns True if zero vector"""
        coord_set = set(tuple(self.coordinates))
        return len(coord_set) == 1 and coord_set.pop() == 0

    def is_parallel(self, other):
        """Returns True if self and other are scalar multiples"""
        return (self.is_zero() or
                other.is_zero() or
                self.angle_with(other) == 0 or
                self.angle_with(other) == pi)


    def is_orthogonal(self, other):
        """Returns True if self and other have a zero dot product"""
        return self.dot_product(other) == 0

    def parallel(self, basis):
        """Returns component parallel"""
        unit = basis.normalize() # will fail if basis vector is zero
        return unit * self.dot_product(unit)

    def ortho(self, basis):
        """Returns component perpendicular"""
        return self - self.parallel(basis)

    def components(self, basis):
        """Returns a dictionary of vector-parallel and vector-orthogonal"""
        return {'parallel': self.parallel(basis), 'ortho': self.ortho(basis)}

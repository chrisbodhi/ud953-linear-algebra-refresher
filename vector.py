from numbers import Number

class Vector(object):
    def __init__(self, coordinates):
        self.coordinates = tuple(coordinates)

    def __str__(self):
        return str(self.coordinates)

    def __add__(self, other):
        s_coor = self.coordinates
        o_coor = other.coordinates
        if len(s_coor) != len(o_coor):
            raise ValueError("Different length coordinates")
        return tuple(sum(x) for x in zip(s_coor, o_coor))

    def __sub__(self, other):
        s_coor = self.coordinates
        o_coor = other.coordinates
        if len(s_coor) != len(o_coor):
            raise ValueError("Different length coordinates")
        # to_iterate = len(s_coor)
        # result = []
        # for ind in range(to_iterate):
        #     result.append(s_coor[ind] - o_coor[ind])
        # return tuple(result)
        result = [x - y for x, y in zip(s_coor, o_coor)]
        return Vector(result)


    def __mul__(self, scalar):
        s_coor = self.coordinates
        if not isinstance(scalar, Number):
            raise ValueError("Scalar needs to be a scalar")
        # to_iterate = len(s_coor)
        # result = []
        # for ind in range(to_iterate):
        #     result.append(scalar * s_coor[ind])
        # return tuple(result)
        result = [scalar * x for x in s_coor]
        return Vector(result)

# Lesson 2

## Vectors

### Operating on Vectors

- Addition
  - Place head of first vector on tail of second vector; measure from tail of first vector to head of second vector to get the sum
  - [1 2] + [3 1] = [4 3]
  - [x1 y1] + [x2 y2] = [x1 + x2 y1 + y2]

```
def __add__(self, other):
    s_coor = self.coordinates
    o_coor = other.coordinates
    if len(s_coor) != len(o_coor):
        raise ValueError("Different length coordinates")
    return Vector(sum(x) for x in zip(s_coor, o_coor))
```

- Subtraction
  - Draw vector connecting the heads of both vectors, from the head of **w** to the head of **v** for the formula **v** - **w**
  - **w** + (**v** - **w**) = **v**
  - [1 3] - [5 1] = [-4 2]
  - [x1 y1] - [x2 y2] = [x1 - x2 y1 - y2]

```
def __sub__(self, other):
    s_coor = self.coordinates
    o_coor = other.coordinates
    if len(s_coor) != len(o_coor):
        raise ValueError("Different length coordinates")
    # to_iterate = len(s_coor)
    # result = []
    # for ind in range(to_iterate):
    #    result.append(s_coor[ind] - o_coor[ind])
    result = [x - y for x, y in zip(s_coor, o_coor)]
    return Vector(result)
```

- Scalar Multiplication
  - A vector is multiplied by a number, known as a `scalar`.
  - 2 [1 2] = [2 4]
  - -0.5 [3 2 1] = [-1.5, -1, -0.5]

```
from numbers import Number

def __mul__(self, scalar):
    s_coor = self.coordinates
    if not isinstance(scalar, Number):
        raise ValueError("Scalar needs to be a scalar")
    # to_iterate = len(s_coor)
    # result = []
    # for ind in range(to_iterate):
    #    result.append(scalar * s_coor[ind])
    result = [scalar * x for x in s_coor]
    return Vector(result)
```
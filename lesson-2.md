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

## Magnitude and Direction

### Magnitude

- Magnitude is how much movement a vector quantifies
- Direction refers to where the v's movement is pointed

- Magnitude is length of vector
    - use the pythagorean theorum to get the hypotenuse
    - || **v** || = \sqrt{v_x^2 + v_y^2}
    - double bars denote magnitude of vector **v**

### Unit Vectors

- Normalization: process of finding a unit vector in the same direction as a given vector
    - Step 1: find the vector's mag
    - Step 2: scalar multiplication: (1 / || **v** ||) * **v** to get the unit vector in the vector's direction

- Unit vector: a vector of magnitude 1

### Direction

- A vector's direction can be represented by a unit vector

### Zero Vector

- If all vector coordinates are zero, that there is a zero vector, noted as a zero with an arrow over top. Or **0** for here and now.
- A vector indicating no change, with no normalization and no direction, with a magnitude of zero.

### Coding Magnitude and Direction

```
from math import sqrt

def magnitude(self):
    """Return magnitude of vector"""
    # Your LISP is showing...
    return sqrt(sum(map(self._square, self.coordinates)))

def _square(self, num):
    return pow(num, 2)
```

```
# def direction(self):
def normalize(self):
    """Return unit vector of vector"""
    mag = self.magnitude()
    try:
        return self * (1. / mag)
    except ZeroDivisionError:
        raise Exception("no zero divide to get nrml")
```

## Inner Product, or Dot Product

**v** dot **w** = ||**v**|| * ||**w**|| * cos(theta)

magnitude of v times magnitude of w times cosine of angle between vectors v and w

Returns a number

theta = arccos(**v** dot **w** / ||**v**|| * ||**w**||)

or

theta = arccos((1 / ||**v**||)**v** * (1/||**w**||)**w**)

**v** dot **w** = (v1 * w1) + (v2 * w2) + ... (vn * wn)

#### Cauchy-Schwarz Inequality

**v** dot **w** <= abs(||**v**|| * ||**w**||)

cosine(zero) = 1

cosine(180 degree or pi radians) = -1

### Coding the Dot Product and Angle

```
def dot_product(self, other):
    """Return dot product of two vectors"""
    if not isinstance(other, Vector):
        return Exception("Not a vector")

    s_coor = self.coordinates
    o_coor = other.coordinates
    results = [x * y for x, y in zip(s_coor, o_coor)]
    return sum(results)
```

```
def angle_with(self, other, in_radians=True):
    """Returns angle between two vectors, default in radians, passed falsy for third param for degrees"""
    if not isinstance(other, Vector):
        return Exception("Not a vector")
    dot = self.dot_product(other)
    mag_product = self.magnitude() * other.magnitude()
    try:
        angle_val = acos(float(dot) / mag_product)
        return angle_val if in_radians else degrees(angle_val)
    except ZeroDivisionError:
        raise Exception("Cannot divide by zero")
```

## Parallel and Orthogonal Vectors

### Parallel Vectors

Two vectors are parallel if one is a scalar multiple of the other.

All Parallel
- **v**
- 2**v**
- 0.5**v**
- -**v**
- **0**
- 1**v**

They can point in opposite directions.

### Orthogonal Vectors

Two vectors are orthogonal if their dot product is zero.

**v** dot **w** = 0

makes them orthogonal, _if_ neither of them are zero vectors.

_Interesting_: zero vector is parallel and orthogonal to all other vectors

The only vector orthogonal to itself.

**v** dot **v** = 0
...then || **v** || ^ 2 = 0
...then **v** = 0

### Checking Parallel, Orthogonal

#### Parallels
```
def is_zero(self):
    """Returns True if zero vector"""
    coord_set = set(tuple(self.coordinates))
    return len(coord_set) == 1 and coord_set.pop() == 0

def is_parallel(self, other):
    """Returns True if self and other are scalar multiples"""
    if self.is_zero() or other.is_zero():
        return True
    s_coor = self.coordinates
    o_coor = other.coordinates
    result = [x / y for x, y in zip(s_coor, o_coor)]
    return len(set(result)) == 1
```
#### Orthogonal

```
def is_orthogonal(self, other):
    """Returns True if self and other have a zero dot product"""
    return self.dot_product(other) == 0
```

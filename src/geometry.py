"""Imago geometry module."""

from math import sin, cos, atan, pi

class V(object):
    """Class for vector manipulation."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return V(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return V(self.x - other.x, self.y - other.y)

    def __rmul__(self, other):
        return V(other * self.x, other * self.y)

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif type(key) != int:
            raise TypeError("V indices must be integers") 
        else:
            raise KeyError("V index ({}) out of range".format(key))

    def __iter__(self):
        yield self.x
        yield self.y

    @property
    def normal(self):
        return V(-self.y, self.x)

def projection(p, l, v):
    #TODO what is this?
    return V(*intersection(line(p, p + v.normal), line(*l)))

def l2ad((a, b), size):
    """Represent line as (angle, distance).
    
    Take a line (represented by two points) and image size.
    Return the line represented by its angle and distance
    from the center of the image.

    """
    if (a[0] - b[0]) == 0:
        angle = pi / 2
    else:
        q = float(a[1] - b[1]) / (a[0] - b[0])
        angle = atan(q)

    if angle < 0:
        angle += pi
    if angle > pi:
        angle -= pi

    distance = (((a[0] - (size[0] / 2)) * sin(angle)) + 
                ((a[1] - (size[1] / 2)) * - cos(angle)))
    return (angle, distance)

def line(x, y):
    """Return parametric representation of line."""
    a = x[1] - y[1]
    b = y[0] - x[0]
    c = a * y[0] + b * y[1]
    return (a, b, c)

def intersection(p, q):
    """Return intersection of two lines."""
    det = p[0] * q[1] - p[1] * q[0]
    if det == 0:
        return None
    return (int(round(float(q[1] * p[2] - p[1] * q[2]) / det)), 
            int(round(float(p[0] * q[2] - q[0] * p[2]) / det)))

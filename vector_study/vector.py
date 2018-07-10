from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 3

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)
            self._magnitude = None
            self._normalization = None

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __abs__(self):
        return Vector([abs(x) for x in self.coordinates])

    def __add__(self, v):
        return Vector([x[0] + x[1] for x in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        return Vector([x[0] - x[1] for x in zip(self.coordinates, v.coordinates)])

    def times(self, c):
        return Vector([x * Decimal(c) for x in self.coordinates])

    @property
    def magnitude(self):
        if not self._magnitude:
            self._magnitude = Decimal(sqrt(sum([x**2 for x in self.coordinates])))

        return self._magnitude

    @property
    def normalization(self):
        if not self._normalization:
            self._normalization = self.times(Decimal(1)/self.magnitude)

        return self._normalization

    def is_zero(self, tolerance=1e-10):
        return self.magnitude < tolerance

    def dot(self, v):
        return sum([x[0] * x[1] for x in zip(self.coordinates, v.coordinates)])

    def angle(self, v, degrees=False):
        radians = acos(self.normalization.dot(v.normalization))
        if degrees:
            return radians * 180 / pi
        return Decimal(radians)

    def parallel_with(self, v):
        return self.is_zero() or self.is_zero() \
                or self.angle(v) == 0 or self.angle(v) == pi

    def orthogonal_with(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def component_projection(self, b):
        return self.dot(b.normalization) * b.normalization

    def projection_orthogonal(self, b):
        return self - self.projection(b)

def cal_n_m():
    v1 = Vector((-0.211, 7.437))
    print(v1.magnitude)

    v3 = Vector((5.581, -2.136))
    print(v3.normalization)

def cal_pro_agl():
    v1=Vector((7.887, 4.138))
    w1=Vector((-8.802, 6.776))

    print(v1.dot(w1))
    v2=Vector((-5.955, -4.904, -1.874))
    w2=Vector((-4.496, -8.755, 7.103))
    print(v2.dot(w2))

    v3=Vector((3.183, -7.627))
    w3=Vector((-2.668, 5.319))
    print(v3.angle(w3))

    v4=Vector((7.35, 0.221, 5.188))
    w4=Vector((2.751, 8.259, 3.985))
    print(v4.angle(w4, True))

def paral_orthogonal():
    v1 = Vector((-7.57, -7.88))
    w1 = Vector((22.737, 23.64))
    v2 = Vector((-2.029, 9.97, 4.172))
    w2 = Vector((-9.231, -6.639, -7.245))
    v3 = Vector((-2.328, -7.284, -1.214))
    w3 = Vector((-1.821, 1.072, -2.94))
    v4 = Vector((2.118, 4.827))
    w4 = Vector((0, 0))
    print(v1.parallel_with(w1))
    print(v1.orthogonal_with(w1))
    print(v1.angle(w1))
    print(v2.parallel_with(w2))
    print(v2.orthogonal_with(w2))
    print(v2.angle(w2))
    print(v3.angle(w3))
    print(v3.orthogonal_with(w3))
    print(v3.dot(w3))

def projection():

if __name__== "__main__":
    #cal_n_m()
    #cal_pro_agl()
    paral_orthogonal()

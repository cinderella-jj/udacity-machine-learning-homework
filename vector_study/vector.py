from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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

    def __add__(self, v):
        return Vector([x[0] + x[1] for x in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        return Vector([x[0] - x[1] for x in zip(self.coordinates, v.coordinates)])

    def times(self, c):
        return Vector([x * c for x in self.coordinates])

    @property
    def magnitude(self):
        if not self._magnitude:
            self._magnitude = sqrt(sum([x**2 for x in self.coordinates]))

        return self._magnitude

    @property
    def normalization(self):
        if not self._normalization:
            self._normalization = self.times(1/self.magnitude)

        return self._normalization

    def product(self, v):
        return sum([x[0] * x[1] for x in zip(self.coordinates, v.coordinates)])

def cal_n_m():
    v1 = Vector((-0.211, 7.437))
    print(v1.magnitude)

    v3 = Vector((5.581, -2.136))
    print(v3.normalization)

def cal_pro_agl():
    v1=Vector((7.887, 4.138))
    v2=Vector((-8.802, 6.776))

    print(v1.product(v2))
    v3=Vector((-5.955, -4.904, -1.874))
    v4=Vector((-4.496, -8.755, 7.103))
    print(v3.product(v4))


if __name__== "__main__":
    cal_n_m()

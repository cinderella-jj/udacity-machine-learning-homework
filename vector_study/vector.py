from math import sqrt, acos, pi

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

    def angle(self, v, degrees=False):
        #radians = acos(self.product(v) / (self.magnitude * v.magnitude))
        radians = acos(self.normalization.product(v.normalization))
        if degrees:
            return radians * 180 / pi
        return radians

def cal_n_m():
    v1 = Vector((-0.211, 7.437))
    print(v1.magnitude)

    v3 = Vector((5.581, -2.136))
    print(v3.normalization)

def cal_pro_agl():
    v1=Vector((7.887, 4.138))
    w1=Vector((-8.802, 6.776))

    print(v1.product(w1))
    v2=Vector((-5.955, -4.904, -1.874))
    w2=Vector((-4.496, -8.755, 7.103))
    print(v2.product(w2))

    v3=Vector((3.183, -7.627))
    w3=Vector((-2.668, 5.319))
    print(v3.angle(w3))

    v4=Vector((7.35, 0.221, 5.188))
    w4=Vector((2.751, 8.259, 3.985))
    print(v4.angle(w4, True))

if __name__== "__main__":
    #cal_n_m()
    cal_pro_agl()

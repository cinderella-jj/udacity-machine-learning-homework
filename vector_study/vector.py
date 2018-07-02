from itertools import izip

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        return Vector([x[0] + x[1] for x in izip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        return Vector([x[0] - x[1] for x in izip(self.coordinates, v.coordinates)])

    def ____(self, ):
        return Vector([sum(x) for x in list(zip(self.coordinates, v.coordinates))])

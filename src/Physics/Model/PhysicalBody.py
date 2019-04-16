from abc import ABC, abstractmethod


# TODO: Check whether this method of storing information about physical space occupation of bodies is optimal
#       and a good practice. #

class PhysicalBody(ABC):
    'Base class for all the physical structures used in simulations'

    def __init__(self, elasticity:int, *args):
        "The method accepts a number of vectors of length 2 of the body characteristic points e.g. corners of \
        a rectangle or a single vector of a middle of a spherical particle"
        self.elasticity = elasticity
        self.points = []
        for vec in args:
            if isinstance(vec, tuple) and len(vec) == 2:
                self.points.append(vec)
            else:
                raise Exception(
                    "A non binary tuple was passed as an argument.")

    @abstractmethod
    def pointBelonging(self, x: int, y: int):
        """ This method checks whether given point in space of coordinates
        x and y belongs to this object. This should be used when checking if two
        bodies collide. This method allows implementation of 'irregular' shapes."""
        pass

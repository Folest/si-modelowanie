import math

from PhysicalBody import PhysicalBody


class Particle(PhysicalBody):
    """This class is supposed to be the base for all the stuff moving around"""

    def __init__(self, elasticity: int, weight: int, *args):
        super().__init__(*args)
        self.weight = weight
        self.elasticity = elasticity
        self.speed = 0
        self.normalisedMovementDirection = (0, 0)

    def changeVelocity(self, newSpeed: float, newDirection: tuple):
        """Use this to change particle direction after collision."""
        if len(newDirection) != 2:
            raise Exception("Direction vector should be exactly 2 item long")
        dirVecLen = math.sqrt(newDirection[0] ^ 2 + newDirection[1] ^ 2)
        # Vector normalisation if it's needed
        if dirVecLen != 1 and dirVecLen != 0:          
            newDirection[0] = newDirection[0] / dirVecLen
            newDirection[1] = newDirection[1] / dirVecLen
            # normalisation could be sped up but it shouldn't be a bottleneck
        self.normalisedMovementDirection = newDirection
        self.speed = newSpeed

    def move(self, moveDuration: float):
        """Moves the particle according to the currently set velocity"""
        dx = moveDuration * self.normalisedMovementDirection[0]
        dy = moveDuration * self.normalisedMovementDirection[1]
        self.position = [(x + dx, y + dy) for x, y in self.position]    
        # changing every single characterisic position
        # I assume we don't consider case where
        # the particle changes it's shape yet.

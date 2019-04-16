from ..Model.Obstacles.LinearBorder import LinearBorder
from ..Model.Particles.Particle import Particle
from ..Model.PhysicalBody import PhysicalBody

# TODO: Consider situation when a particle collides with 2 objects simultaneously. Although this will be a problem during
#   collision time prediction.

X = 0
Y = 1
START = 0
END = 1


class Collider:
	def __init__(self):
		pass

	def collide(self, body1: PhysicalBody, body2: PhysicalBody):
		if isinstance(body1, LinearBorder) or isinstance(body2,
		                                                 LinearBorder):  # the collision happens between border and a particle
			if isinstance(body1, LinearBorder):
				body = body2
				obstacle = body1
			else:
				body = body1
				obstacle = body2
			if isinstance(body, Particle):
				direction = body.normalisedMovementDirection
				speed = body.speed
				obstacleVect = ((obstacle.points[START]), obstacle.points[END])
				obstacleVectLen = sqrt((obstacleVect[END][X] - obstacleVect[START][X]) ^ 2 +
				                       (obstacleVect[END][Y] - obstacleVect[START][Y]) ^ 2)
				if obstacleVectLen != 0 and obstacleVectLen != 1:
					obstacleNormVect = ((obstacleVect[END][X] - obstacleVect[START][X]) / obstacleVectLen,
					                    (obstacleVect[END][Y] - obstacleVect[START][Y]) / obstacleVectLen)
		# TODO: Finish this

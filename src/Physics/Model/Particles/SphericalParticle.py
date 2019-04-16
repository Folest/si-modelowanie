from ..PhysicalBody import PhysicalBody

X = 0
Y = 1  # nie wiem czy to prawilne


class SphericalParticle(PhysicalBody):
	def __init__(self, elasticity, radius, weight, xm, ym, ):
		# The characteristic vector is the middle point of the particle
		super().__init__(elasticity, (xm, ym))
		self.radius = radius
		self.weight = weight

	def pointBelonging(self, x: int, y: int):
		return x - self.points[0][X] <= self.radius \
		       and y - self.points[0][Y] <= self.radius

	def x(self):
		return self.points[0][X]

	def y(self):
		return self.points[0][Y]

import vpython as vp

from src.Physics.Model.Particles.SphericalParticle import SphericalParticle


class WorldPOC:
	def __init__(self):
		self.elements = []
		self.scene = vp.canvas(title="Particle simulation", color=vp.vector(0.12, 0.52, 0),
		                       height=600, width=1200)
		# debug
		self.lastX = -3
		self.lastY = -3
		self._wasVisualised = False

	def addElement(self, element: SphericalParticle):
		self.elements.append(element)

	def viewWorld(self):
		self.representations = list(map(lambda x: vp.sphere(radius=x.radius, pos=vp.vector(self.lastX, self.lastY, 0)),
		                                self.elements))
		self._wasVisualised = True

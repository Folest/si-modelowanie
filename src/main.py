import vpython as vp
from Physics.WorldPOC import WorldPOC
from Physics.Model.Particles.SphericalParticle import SphericalParticle
# A small sample of vp 2D. No idea how to change created objects position.

scene = vp.canvas(title="Testing vpython for physics", height=600,
                  width=1200, background=vp.vector(0.12, 0.52, 0))

# circle = vp.shapes.circle(pos=[1, 0], radius=0.1)
# circle2 = vp.shapes.circle(pos=[3.1, 1.2], radius=0.2)

# circle_path = [vp.vector(0, 0, 0), vp.vector(0.0, 0, 0.00001)]

# vp.extrusion(path=circle_path, shape=circle)
# vp.extrusion(path=circle_path, shape=circle2)

world = WorldPOC()

world.addElement(SphericalParticle(1, 1, 1, 0.01, 1))

world.viewWorld()

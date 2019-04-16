import vpython as vp
import time
from Physics.Model.Ball import Ball
from Physics.Tools.Collider import Collider
# A small sample of vp 2D. No idea how to change created objects position.



scene = vp.canvas(title="Testing vpython for physics", height=600,
                  width=1200, background=vp.vector(0.12, 0.52, 0))


kula = vp.sphere(canvas=scene)
kula.color = vp.vector(1, 0, 1)

kula2 = vp.sphere(canvas=scene)
kula2.color = vp.vector(0, 0, 1)

ball1 = Ball(0, 0, 3, 3)
ball2 = Ball(0, 5, 3, 3)

ball1.move_direction = (-0.5, 0)
ball2.move_direction = (0.5, 2)

collider = Collider()
while True:
    time.sleep(1)

    collider.collide_balls(ball1, ball2)

    kula.pos = vp.vector(ball1.xm, ball1.ym, kula.pos.z)
    kula2.pos = vp.vector(ball2.xm, ball2.ym, kula2.pos.z)


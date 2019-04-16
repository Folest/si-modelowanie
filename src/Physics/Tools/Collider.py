import math as m
from ..Model.Ball import Ball

class Collider:
    def __init__(self):
        self.elasticity = 1

    def collide_balls(self, b1: Ball, b2: Ball):

#        // Distance       between balls
        fDistance = m.sqrt((b1.xm - b2.xm) * (b1.xm - b2.xm) + (b1.ym - b2.ym) * (b1.ym - b2.ym))

        # Normal
        nx = (b2.xm - b1.xm) / fDistance
        ny = (b2.ym - b1.ym) / fDistance

        # Tangent
        tx = -ny
        ty = nx

        #
        v1x = b1.speed * b1.move_direction[0]
        v1y = b1.speed * b1.move_direction[1]
        v2x = b2.speed * b1.move_direction[0]
        v2y = b2.speed * b1.move_direction[1]

        # Dot Product Tangent
        dpTan1 = v1x * tx + v1y * ty
        dpTan2 = v2x * tx + v2y * ty

        # Dot Product Normal
        dpNorm1 = v1x * nx + v1y * ny
        dpNorm2 = v2x * nx + v2y * ny

        # Conservation of momentum in 1D
        m1 = (dpNorm1 * (b1.weight - b2.weight) + 2.0 * b2.weight * dpNorm2) / (b1.weight + b2.weight)
        m2 = (dpNorm2 * (b2.weight - b1.weight) + 2.0 * b1.weight * dpNorm1) / (b1.weight + b2.weight)

        # Update ball velocities
        # b1->vx = tx * dpTan1 + nx * m1
        # b1->vy = ty * dpTan1 + ny * m1
        # b2->vx = tx * dpTan2 + nx * m2
        # b2->vy = ty * dpTan2 + ny * m2

        v1x = tx * dpTan1 + nx * m1
        v1y = ty * dpTan1 + ny * m1
        v2x = tx * dpTan2 + nx * m2
        v2y = ty * dpTan2 + ny * m2

        final_speed1 = m.sqrt(v1x ** 2 + v1y ** 2)
        final_speed2 = m.sqrt(v2x ** 2 + v2y ** 2)


        v1x /= final_speed1
        v1y /= final_speed1
        v2x /= final_speed2
        v2y /= final_speed2

        b1.speed = final_speed1
        b1.move_direction = (v1x, v1y)
        b2.speed = final_speed2
        b2.move_direction = (v2x, v2y)

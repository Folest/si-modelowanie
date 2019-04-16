X = 0
Y = 1
import math as m

class Ball:
    def __init__(self, x: float, y: float, radius: float, weight: float):
        self.xm = x
        self.ym = y
        self.radius = radius
        self.speed = 10
        self.move_direction = (0.0, 0.0)
        self.weight = weight

    def change_velocity(self, new_speed: float, new_direction: (float, float)):
        self.speed = new_speed
        vector_length = m.sqrt(new_direction[X] ** 2 + new_direction[Y] ** 2)
        self.speed = (new_direction[X] / vector_length, new_direction[Y] / vector_length)
        self.move_direction = new_direction

    #
    # def move(self, time_ms: int, friction_factor: float):
    #     end_speed = self.speed - time_ms * friction_factor
    #     avg_speed = (self.speed - end_speed) / 2
    #     self.xm += self.move_direction[X] * avg_speed
    #     self.ym += self.move_direction[Y] * avg_speed
    #     self.speed = end_speed




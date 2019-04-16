from ..PhysicalBody import PhysicalBody


class LinearBorder(PhysicalBody):
    def __init__(self, elasticity: int, x1: int, y1: int, x2: int, y2: int):
        """"x1, y1 - border beginning x2,y2 - border ending.
         Linear border characteristic points are [0] it's start [1] it's end"""
        super().__init__(elasticity, (x1, y1), (x2, y2))

    def pointBelonging(self, x: int, y: int):
        if self.points[0][0] <= x <= self.points[1][0] \
                and self.points[0][1] <= y <= self.points[1][1]:
            return True
        else:
            return False

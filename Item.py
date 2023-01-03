from random import uniform

from ursina import *

from CustomMath import Vec2
from Flame import Flame
from RainDrop import RainDrop


class Item:
    def onUse(self, user: RainDrop):
        pass

    def refill(self):
        pass

class FlameThrower(Item):
    inaccuracy: float = 0.13
    maxPower: int = 100
    power: float

    def __init__(self):
        self.power = self.maxPower
        pass

    def onUse(self, user: RainDrop):
        if self.power <= 0:
            return

        Flame(user.x, user.y, Vec2(mouse.x + uniform(-self.inaccuracy, self.inaccuracy), mouse.y + uniform(-self.inaccuracy, self.inaccuracy)), user)
        self.power -= 1

    def refill(self):
        if self.power >= self.maxPower:
            return

        self.power += time.dt
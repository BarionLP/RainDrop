from random import uniform

from ursina import *

from CustomMath import Vec2
from Flame import Flame
from RainDrop import RainDrop
from SingleValueEvent import SingleValueEvent


class Weapon:
    inaccuracy: float = 0.12
    maxAmmo: int = 100
    _ammo: float = 0
    onAmmoChangeEvent = SingleValueEvent()

    @property
    def ammo(self):
        return self._ammo

    @ammo.setter
    def ammo(self, value):
        self._ammo = value
        self.onAmmoChangeEvent.invoke(value)

    def __init__(self):
        self.ammo = self.maxAmmo

    def onUse(self, user: RainDrop):
        pass

    def refill(self):
        pass


class FlameThrower(Weapon):
    def __init__(self):
        super().__init__()

    def onUse(self, user: RainDrop):
        if self.ammo < 1:
            return

        Flame(user.x, user.y, Vec2(mouse.x + uniform(-self.inaccuracy, self.inaccuracy), mouse.y + uniform(-self.inaccuracy, self.inaccuracy)), user)
        self.ammo -= 1

    def refill(self):
        if self.ammo >= self.maxAmmo:
            return

        self.ammo += time.dt
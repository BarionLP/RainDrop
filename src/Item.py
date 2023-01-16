from random import uniform

from ursina import *

from CustomMath import Vec2
from Flame import Flame
from RainDrop import RainDrop
from SingleValueEvent import SingleValueEvent
from src.Event import Event


class Weapon:
    inaccuracy: float = 0.10
    maxAmmo: int = 100
    _ammo: float = 0
    onAmmoChangeEvent: SingleValueEvent
    onFireStart: Event
    onFireEnd: Event
    wasUsing: bool = False

    @property
    def ammo(self):
        return self._ammo

    @ammo.setter
    def ammo(self, value):
        self._ammo = value
        self.onAmmoChangeEvent.invoke(value)

    def __init__(self):
        self.onAmmoChangeEvent = SingleValueEvent()
        self.ammo = self.maxAmmo
        self.onFireStart = Event()
        self.onFireEnd = Event()

    def onUse(self, user: RainDrop):
        pass

    def refill(self):
        pass


class FlameThrower(Weapon):
    shootClip: Audio

    def __init__(self):
        super().__init__()
        self.shootClip = Audio('flame', autoplay=False, auto_destroy=False, loop=True)
        self.onFireStart.addListener(self.startShootClip)
        self.onFireEnd.addListener(self.stopShootClip)

    def onUse(self, user: RainDrop):
        if self.ammo < 1:
            return

        Flame(user.x, user.y, Vec2(mouse.x + uniform(-self.inaccuracy, self.inaccuracy), mouse.y + uniform(-self.inaccuracy, self.inaccuracy)).normalised()*user.scale_x, user)
        self.ammo -= 1

    def refill(self):
        if self.ammo >= self.maxAmmo:
            return

        self.ammo += time.dt

    def startShootClip(self):
        # self.shootClip.play()
        pass

    def stopShootClip(self):
        # self.shootClip.stop()
        pass

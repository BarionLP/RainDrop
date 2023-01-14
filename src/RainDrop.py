from math import degrees, atan2

from ursina import *
from ursina import time
from ursina.hit_info import HitInfo

from CustomMath import Vec2
from src.Event import Event


class RainDrop(Entity):
    speed: float
    _water: float
    immunityTime: float = 0
    onDeath: Event
    highlight: Entity

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, value: float):
        self._water = value
        self.__updateSize()

    def __init__(self, x: float, y: float, speed: float, water: float, **kwargs):
        super().__init__(texture="assets/raindrop.png", model="quad", collider="sphere", **kwargs)
        self.x = x
        self.y = y
        self.speed = speed
        self.water = water
        self.onDeath = Event()

    def getMovement(self) -> Vec2:
        pass

    def update(self):
        force = self.getMovement()

        if force.magnitudeSqr() != 0:
            self.water -= self.scale_x*0.001
            self.x += force.x * self.speed * time.dt
            self.y += force.y * self.speed * time.dt
            self.rotation_z = degrees(atan2(-force.x, -force.y))

        if self.immunityTime > 0:
            self.immunityTime -= time.dt

        if self.intersects():
            self.onCollision(self.intersects())

        if self.water < 0.5:
            self.kill()

    def onCollision(self, hit: HitInfo):
        for collided in hit.entities:
            if not isinstance(collided, RainDrop):
                continue
            if collided.water <= self.water:
                continue
            if self.getDistance(collided) > 0.3:  # TODO: make size dependent
                continue

            collided.mergedWithRainDrop(self.water)
            self.kill()

    def damage(self, amount: float, source: Entity):
        if self.immunityTime > 0:
            return

        self.water -= amount

        self.immunityTime = 0.2

        if self.isDriedOut():
            self.kill()

    def mergedWithRainDrop(self, waterOther: float):
        self.water += waterOther * 0.6

    def __updateSize(self):
        size = self.water / 40 + 0.5
        self.scale = Vec3(size, size, size)

    def isDriedOut(self) -> bool:
        return self.water <= 0

    def kill(self):
        self.onDeath.invoke()
        destroy(self)

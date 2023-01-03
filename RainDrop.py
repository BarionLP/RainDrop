from ursina import *
from ursina import time
from ursina.hit_info import HitInfo


class RainDrop(Entity):
    speed: float
    _water: float
    immunityTime: float = 0

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, value: float):
        self._water = value
        self.__updateSize()

    def __init__(self, x: float, y: float, speed: float, water: float, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.speed = speed
        self.water = water

    def move(self):
        pass

    def update(self):
        self.move()

        if self.immunityTime > 0:
            self.immunityTime -= time.dt

        if self.intersects().entity is not None:
            self.onCollision(self.intersects())

    def onCollision(self, hit: HitInfo):
        # TODO:
        # support multiple collisions

        if not isinstance(hit.entity, RainDrop):
            return
        if hit.entity.water <= self.water:
            return
        if self.getDistance(hit.entity) > 0.2:
            return

        hit.entity.mergedWithRainDrop(self.water)
        self.kill()

    def damage(self, amount: float, source: Entity):
        if self.immunityTime > 0:
            return

        self.water -= amount

        self.immunityTime = 0.2

        if self.isDriedOut():
            self.kill()

    def mergedWithRainDrop(self, waterOther: float):
        self.water += waterOther

    def __updateSize(self):
        size = self.water / 40 + 0.5
        self.scale = Vec3(size, size, size)

    def isDriedOut(self) -> bool:
        return self.water <= 0

    def kill(self):
        destroy(self)

from ursina import *

from CustomMath import Vec2


class Rain(Entity):
    direction: Vec2

    def __init__(self, parent, direction: Vec2, offset: Vec2 = Vec2(0, 0)):
        super().__init__(model="quad", texture="assets/raindrops.png", parent=parent)
        self.direction = direction
        self.scale = 2
        self.alpha = .7
        self.z = -1
        self.texture_offset = offset

    def move(self):
        self.position += self.direction

    def update(self):
        self.texture_offset += self.direction * time.dt


class RainManager(Entity):
    __windDirection: Vec2
    __rain1: Rain
    __rain2: Rain

    @property
    def windDirection(self) -> Vec2:
        return self.__windDirection

    @windDirection.setter
    def windDirection(self, value: Vec2):
        self.__windDirection = value
        self.rain1.direction = value
        self.rain2.direction = value

    def __init__(self, parent: Entity):
        super().__init__(parent=parent)
        rain = Vec2(133, 339).normalised()
        self.rain1 = Rain(self, rain)
        self.rain2 = Rain(self, rain, Vec2(.5, .5))

    def update(self):
        # self.rain1.mot
        pass

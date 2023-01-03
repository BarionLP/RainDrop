from ursina import *

from CustomMath import Vec2
from RainDrop import RainDrop


class Enemy(RainDrop):
    target = None

    def __init__(self, x: float, y: float, target):
        super().__init__(x, y, 2, 20, model="circle", color=color.red, collider="sphere")
        self.target = target

    def move(self):
        direction = Vec2(self.target.x - self.x, self.target.y - self.y)

        self.x += direction.x * self.speed * time.dt
        self.y += direction.y * self.speed * time.dt

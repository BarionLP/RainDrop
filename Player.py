from ursina import *

from CustomMath import Vec2
from Item import Item, FlameThrower
from RainDrop import RainDrop


class Player(RainDrop):
    velocity: Vec2 = Vec2(0, 0)
    speed: float = 0.4
    attackCooldown: float = 0
    linearDrag: float = 0.93
    item: Item = FlameThrower()

    def __init__(self, x: float, y: float):
        super().__init__(x, y, 0.4, 20, model="circle", color=color.cyan, collider="sphere")
        pass

    def update(self):
        super().update()
        self.attackCooldown -= time.dt

        if mouse.left and self.attackCooldown <= 0:
            self.attackCooldown = 0.1
            self.item.onUse(self)
        else:
            self.item.refill()

    def move(self):
        self.velocity += getInput()
        self.x += self.velocity.x * time.dt * self.speed
        self.y += self.velocity.y * time.dt * self.speed
        self.velocity *= self.linearDrag


def getInput() -> Vec2:
    return Vec2(held_keys['d'] - held_keys['a'], held_keys['w'] - held_keys['s']).normalised()

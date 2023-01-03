from random import uniform

from ursina import *

from CustomMath import Vec2
from Flame import Flame
from RainDrop import RainDrop


class Player(RainDrop):
    velocity: Vec2 = Vec2(0, 0)
    speed: float = 0.4
    attackCooldown: float = 0
    linearDrag: float = 0.93
    particleOffset = 0.13

    def __init__(self, x: float, y: float):
        super().__init__(x, y, 0.4, 20, model="circle", color=color.cyan, collider="sphere")
        pass

    def update(self):
        super().update()
        self.attackCooldown -= time.dt

        if mouse.left and self.attackCooldown <= 0:
            self.attackCooldown = 0.1
            Flame(self.x, self.y, Vec2(mouse.x + uniform(-self.particleOffset, self.particleOffset), mouse.y + uniform(-self.particleOffset, self.particleOffset)), self)

    def move(self):
        self.velocity += getInput()
        self.x += self.velocity.x * time.dt * self.speed
        self.y += self.velocity.y * time.dt * self.speed
        self.velocity *= self.linearDrag


def getInput() -> Vec2:
    right = held_keys['d']
    left = held_keys['a']
    up = held_keys['w']
    down = held_keys['s']

    return Vec2(right - left, up - down).normalised()

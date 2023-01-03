from ursina import *

from CustomMath import Vec2
from RainDrop import RainDrop

repulsionStrength = 0.4
maxDistance = 5


class Enemy(RainDrop):
    target = None
    repulsionStrength = 0.5

    def __init__(self, x: float, y: float, target):
        super().__init__(x, y, 2, 20, model="circle", color=color.red, collider="sphere")
        self.target = target

    def move(self):
        direction = self.getAttraction()
        repulsion = self.getRepulsion()

        force = direction + repulsion

        self.x += force.x * self.speed * time.dt
        self.y += force.y * self.speed * time.dt

    def getAttraction(self) -> Vec2:
        return Vec2(self.target.x - self.x, self.target.y - self.y).normalised()

    def getRepulsion(self) -> Vec2:
        repulsionForce = Vec2(0, 0)

        for other in scene.entities:
            if other == self.target or other == self:
                continue
            if not isinstance(other, Enemy):
                continue

            distance = self.getDistance(other)

            if distance < maxDistance:
                repulsionForce += Vec2(self.position.x - other.position.x, self.position.y - other.position.y).normalised() * repulsionStrength
                # repulsionForce += (self.position - other.position).normalized() * repulsionStrength * (maxDistance - distance)

        return repulsionForce

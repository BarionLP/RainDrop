from ursina import *

from CustomMath import Vec2
from RainDrop import RainDrop

repulsionStrength = 0.4
maxDistance = 5


class Enemy(RainDrop):
    target: RainDrop = None
    repulsionStrength: float = 0.5

    def __init__(self, x: float, y: float, water: int, target: RainDrop):
        super().__init__(x, y, 2, water, model="circle", color=color.red, collider="sphere")
        self.target = target

    def move(self):
        direction = self.getAttraction()
        repulsion = self.getRepulsion()

        force = direction + repulsion

        self.x += force.x * self.speed * time.dt
        self.y += force.y * self.speed * time.dt

    def getAttraction(self) -> Vec2:
        if not self.target:
            return Vec2(0, 0)

        return Vec2(self.target.x - self.x, self.target.y - self.y).normalised()

    def getRepulsion(self) -> Vec2:
        repulsionForce = Vec2(0, 0)

        for other in scene.entities:
            if not isinstance(other, Enemy) or other == self:
                continue

            distanceToOther = self.getDistance(other)

            if distanceToOther < maxDistance:
                repulsionForce += Vec2(self.position.x - other.position.x, self.position.y - other.position.y).normalised() * repulsionStrength
                # repulsionForce += (self.position - other.position).normalized() * repulsionStrength * (maxDistance - distanceToOther)

        return repulsionForce

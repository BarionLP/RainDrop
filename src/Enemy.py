from ursina import *

from CustomMath import Vec2
from RainDrop import RainDrop

repulsionStrength = 0.3
maxDistance = 5


class Enemy(RainDrop):
    target: RainDrop = None

    def __init__(self, x: float, y: float, water: int, target: RainDrop):
        super().__init__(x, y, 2.2, water)
        self.target = target

    def getMovement(self) -> Vec2:
        direction = self.getAttraction()
        repulsion = self.getRepulsion()

        return direction + repulsion

    def getAttraction(self) -> Vec2:
        if not self.target:
            return Vec2(0, 0)

        if self.target.water > self.water:
            return Vec2(self.x - self.target.x, self.y - self.target.y).normalised() / 2

        return Vec2(self.target.x - self.x, self.target.y - self.y).normalised() / 2

    def getRepulsion(self) -> Vec2:
        repulsionForce = Vec2(0, 0)

        for other in scene.entities:
            if not isinstance(other, Enemy) or other == self:
                continue

            distanceToOther = self.getDistance(other)

            if distanceToOther < maxDistance:
                repulsionForce += Vec2(self.x - other.position.x, self.y - other.position.y).normalised() * repulsionStrength * (maxDistance - distanceToOther)
                # repulsionForce += (self.position - other.position).normalized() * repulsionStrength * (maxDistance - distanceToOther)

        return repulsionForce.normalised()

from ursina import *
from ursina.hit_info import HitInfo

from CustomMath import Vec2
from RainDrop import RainDrop


class Flame(Entity):
    direction = Vec2(0, 0)
    liveTime: float = 0.9
    speed: float = 6
    source: RainDrop

    def __init__(self, x: float, y: float, direction: Vec2, source: RainDrop):
        super().__init__(model="quad", size_x=0.3, texture="assets/flame.png", collider="sphere")
        self.x = x
        self.y = y
        self.direction = direction.normalised() * source.scale_x*2
        destroy(self, self.liveTime)
        self.alpha = 1
        self.source = source
        self.scale = self.source.scale

    def update(self):
        self.direction *= 0.99
        self.x += self.direction.x * time.dt * self.speed
        self.y += self.direction.y * time.dt * self.speed
        self.scale *= 1 + time.dt * 0.5
        self.alpha -= time.dt/1.5

        if self.intersects():
            self.OnCollision(self.intersects())

    def OnCollision(self, hit: HitInfo):
        for collided in hit.entities:
            if not isinstance(collided, RainDrop) or collided == self.source:
                continue

            collided.damage(self.source.scale_x*0.2, self.source)

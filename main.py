from ursina import *

from Enemy import Enemy
from Player import Player
from RainDrop import RainDrop


class CameraController:
    target: RainDrop
    speed: float

    def __init__(self, target: RainDrop, speed: float = 7):
        self.target = target
        self.speed = speed

    def update(self):
        self.entity.world_position = lerp(
            self.entity.world_position,
            self.target.world_position + Vec3(0,0, (self.target.scale_x * -15) - 15),
            time.dt * self.speed)


def main():
    app = Ursina()

    player = Player(0, 0)
    Enemy(10, 10, player)
    Enemy(-10, 10, player)
    Enemy(10, -10, player)
    Enemy(-10, -10, player)

    camera.add_script(CameraController(player))

    app.run()


if __name__ == "__main__":
    main()

from ursina import *

from Enemy import Enemy
from Player import Player
from RainDrop import RainDrop
from src.RainManager import RainManager


class CameraController:
    target: RainDrop = None
    speed: float

    def __init__(self, target: RainDrop, speed: float = 7):
        self.target = target
        self.speed = speed

    def update(self):
        if not self.target:
            return

        self.entity.world_position = lerp(
            self.entity.world_position,
            self.target.world_position + Vec3(0, 0, (self.target.scale_x * -15) - 15),
            time.dt * self.speed)


def onPlayerDeath():
    pass


def main():
    app = Ursina()
    RainManager(camera.ui)

    player = Player(0, 0)
    player.onDeath.addListener(onPlayerDeath)
    Enemy(10, 15, 35, player)
    Enemy(-10, 10, 20, player)
    Enemy(-10, 5, 29, player)
    Enemy(10, -10, 25, player)
    Enemy(-20, -20, 50, player)
    Enemy(-40, -20, 80, player)

    camera.add_script(CameraController(player))

    app.run()


if __name__ == "__main__":
    main()

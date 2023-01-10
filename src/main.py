from ursina import *

from Enemy import Enemy
from Player import Player
from RainDrop import RainDrop


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
    print("player died")


def main():
    app = Ursina()

    player = Player(0, 0)
    player.onDeath.addListener(onPlayerDeath)
    Enemy(10, 10, 30, player)
    Enemy(-10, 10, 21, player)
    Enemy(10, -10, 25, player)
    Enemy(-10, -10, 40, player)

    camera.add_script(CameraController(player))

    app.run()


if __name__ == "__main__":
    main()

from ursina import *

from Enemy import Enemy
from Player import Player


def main():
    app = Ursina()

    player = Player(0, 0)
    enemy = Enemy(12, 12, player)
    # entity2 = Enemy(-4, -4, player)

    # background = Entity(model="quad", scale=(13, 6), texture="assets/smiley.jpg", z=1)

    camera.add_script(SmoothFollow(target=player, offset=[0, 0, -30]))

    app.run()


if __name__ == "__main__":
    main()

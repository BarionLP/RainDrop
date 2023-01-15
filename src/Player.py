from ursina import *

from Bar import Bar
from CustomMath import Vec2
from Item import Weapon, FlameThrower
from RainDrop import RainDrop


class Player(RainDrop):
    velocity: Vec2 = Vec2(0, 0)
    speed: float = 0.4
    attackCooldown: float = 0
    linearDrag: float = 0.93
    weapon: Weapon
    ammoBar: Bar

    def __init__(self, x: float, y: float):
        super().__init__(x, y, 0.3, 25)
        self.weapon = FlameThrower()
        self.ammoBar = Bar(max_value=self.weapon.maxAmmo, bar_color=color.orange, roundness=0.5)
        self.weapon.onAmmoChangeEvent.addListener(self.updateAmmoBar)
        self.highlight = Entity(texture="assets/highlight_round", color=Color((0, 0.84, 1, 1)), parent=self, model="quad", scale=1.8)
        self.z = -0.1

    def updateAmmoBar(self, value):
        self.ammoBar.value = math.floor(value)

    def update(self):
        super().update()
        self.attackCooldown -= time.dt

        if mouse.left:
            if not self.weapon.wasUsing:
                self.weapon.onFireStart.invoke()
                self.weapon.wasUsing = True

            if self.attackCooldown <= 0:
                self.attackCooldown = 0.1
                self.weapon.onUse(self)
        else:
            if self.weapon.wasUsing:
                self.weapon.wasUsing = False
                self.weapon.onFireEnd.invoke()
            self.weapon.refill()

    def getMovement(self) -> Vec2:
        self.velocity += getInput()
        self.velocity *= self.linearDrag
        return self.velocity


def getInput() -> Vec2:
    return Vec2(held_keys['d'] - held_keys['a'], held_keys['w'] - held_keys['s']).normalised()

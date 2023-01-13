import math

from ursina import Vec2 as Vec2Ursina


class Vec2(Vec2Ursina):

    def __init__(self, x: float, y: float):
        super().__init__(x, y)

    def magnitudeSqr(self) -> float:
        return (self.x * self.x) + (self.y * self.y)

    def magnitude(self) -> float:
        return math.sqrt(self.magnitudeSqr())

    def normalised(self):
        dist = self.magnitude()
        if dist == 0:
            return self
        return self / dist

    def normalise(self):
        dist = self.magnitude()
        if dist > 0:
            self /= dist

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, fac: float):
        return Vec2(self.x * fac, self.y * fac)

    def __truediv__(self, fac: float):
        if fac == 0:
            raise ZeroDivisionError()
        return Vec2(self.x / fac, self.y / fac)

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def rotated(self, degree: float):
        return self.rotatedRad(degree * math.pi / 180.0)

    def rotate(self, degree: float):
        self.rotateRad(degree * math.pi / 180)

    def rotatedRad(self, radiant: float):
        return Vec2(self.x * math.cos(radiant) - self.y * math.sin(radiant),
                    self.x * math.sin(radiant) + self.y * math.cos(radiant))

    def rotateRad(self, radiant: float):
        x = self.x * math.cos(radiant) - self.y * math.sin(radiant)
        y = self.x * math.sin(radiant) + self.y * math.cos(radiant)

        self.x = x
        self.y = y

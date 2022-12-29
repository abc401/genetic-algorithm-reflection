from pygame import Vector2, Surface, draw, Color
from math import inf, isinf


class Ray:
    def __init__(self, pos: Vector2, theta: Vector2, color: Color) -> None:
        self.pos = pos
        self.theta = theta.normalize()
        self.color = color
        self.collide_point = Vector2(inf, inf)
    
    def look_at(self, point: Vector2):
        self.theta = (point - self.pos).normalize()
        self.collide_point = Vector2(inf, inf)
    
    def draw(self, surface: Surface):
        if isinf(self.collide_point.magnitude()):
            draw.line(surface, self.color, self.pos, self.pos + 10 * self.theta)
        else:
            draw.line(surface, self.color, self.pos, self.collide_point)
from pygame import Vector2, Surface, draw, Color


class Ray:
    def __init__(self, pos: Vector2, theta: Vector2, color: Color) -> None:
        self.pos = pos
        self.theta = theta.normalize()
        self.color = color
        self.collide_point = Vector2(self.pos)
    
    def draw(self, surface: Surface):
        draw.line(surface, self.color, self.pos, self.collide_point + 10 * self.pos)
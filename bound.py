from abc import ABC, abstractmethod

from ray import Ray

from pygame import Vector2, Surface, draw, Color
import colors

class Bound(ABC):
    def __init__(self, color: Color = colors.BLACK) -> None:
        self.color = color
    
    @abstractmethod
    def collide(self, ray: Ray) -> Vector2 | None:
        pass

    @abstractmethod
    def interact(self, ray: Ray) -> Ray | None:
        pass


class LineBound(Bound):
    def __init__(self, p1: Vector2, p2: Vector2) -> None:
        super().__init__()
        self.p1 = Vector2(p1)
        self.p2 = Vector2(p2)
    
    def collide(self, ray: Ray) -> Vector2 | None:
        x1, y1 = ray.pos.xy
        x2, y2 = (ray.pos + ray.theta).xy
        x3, y3 = self.p1.xy
        x4, y4 = self.p2.xy

        denomenator = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
        if denomenator == 0:
            return
        t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) / denomenator
        u = ((x1 - x3)*(y1 - y2) - (y1 - y3)*(x1 - x2)) / denomenator
        if t >= 0 and 0 <= u <= 1:
            return Vector2(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    
    def interact(self, ray: Ray) -> Ray | None:
        collide_point = self.collide(ray)
        if not collide_point:
            return
        if collide_point.magnitude() < ray.collide_point.magnitude():
            ray.collide_point = collide_point
    
    def draw(self, surface: Surface):
        draw.line(surface, self.color, self.p1, self.p2)
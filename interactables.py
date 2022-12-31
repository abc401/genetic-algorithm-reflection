from abc import ABC, abstractmethod

from ray import Ray

from pygame import Vector2, Surface, draw, Color
import colors
from math import inf

class Interactable(ABC):
    def __init__(
        self, vertices: list[Vector2],
        color: Color = colors.BLACK, closed: bool = False,
        view_normals: bool = False
    ) -> None:
        self.vertices = vertices
        self.closed = closed
        self.color = color
        self.view_normals = view_normals
    
    def collide_with_segment(self, seg_index: int, ray: Ray) -> Vector2 | None:
        x1, y1 = ray.pos.xy
        x2, y2 = (ray.pos + ray.theta).xy
        x3, y3 = self.vertices[seg_index].xy
        x4, y4 = self.vertices[seg_index+1].xy

        denomenator = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
        if denomenator == 0:
            return Vector2(inf, inf)
        t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) / denomenator
        u = ((x1 - x3)*(y1 - y2) - (y1 - y3)*(x1 - x2)) / denomenator
        if t >= 0 and 0 <= u <= 1:
            return Vector2(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
        return Vector2(inf, inf)

    def collide(self, ray: Ray):
        seg_index = 0
        collide_point = Vector2(inf, inf)
        for i in range(len(self.vertices)-1):
            tmp = self.collide_with_segment(i, ray)
            if tmp.magnitude() < collide_point.magnitude():
                collide_point = tmp
                seg_index = i
        if collide_point.magnitude() < ray.collide_point.magnitude():
            ray.collide_point = collide_point
        return collide_point, seg_index

    def get_normal(self, seg_index: int) -> Vector2:
        return (self.vertices[seg_index] - self.vertices[seg_index+1]).normalize().rotate(90)

    @abstractmethod
    def interact(self, ray: Ray) -> Ray | None:
        pass

    def draw(self, surface: Surface):
        draw.aalines(surface, self.color, self.closed, self.vertices)
        if self.view_normals:
            for i in range(len(self.vertices)-1):
                p1, p2 = self.vertices[i], self.vertices[i+1]
                start = (p2 + p1)/2
                draw.line(
                    surface, colors.BLUE,
                    start,
                    start + self.get_normal(i)*10
                )

class ReflectorObstacle(Interactable):
    def __init__(
        self, vertices: list[Vector2], 
        color: Color = colors.BLACK,
        closed: bool = False,
        view_normals: bool = False
    ) -> None:
        super().__init__(vertices, color, closed, view_normals)

    def interact(self, ray: Ray, seg_index: int) -> Ray:
        return self.reflect(ray, seg_index)
    
    def reflect(self, ray: Ray, seg_index: int):
        normal = self.get_normal(seg_index)
        theta = ray.theta.angle_to(normal)
        reflected = Vector2()
        reflected.from_polar((1, theta))
        return reflected

        


        
        

# class LineObstacle(Obstacle):
#     def __init__(self, p1: Vector2, p2: Vector2) -> None:
#         super().__init__()
#         self.p1 = Vector2(p1)
#         self.p2 = Vector2(p2)
    
#     def interact(self, ray: Ray) -> Ray | None:
#         collide_point = self.collide(ray)
#         if not collide_point:
#             return ray
#         if collide_point.magnitude() < ray.collide_point.magnitude():
#             ray.collide_point = collide_point
    
#     def draw(self, surface: Surface):
#         draw.line(surface, self.color, self.p1, self.p2)
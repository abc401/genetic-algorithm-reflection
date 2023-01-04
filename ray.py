from __future__ import annotations
from pygame import Vector2, Surface, draw, Color
from math import inf, isinf
from random import random
import colors


class Ray:
    def __init__(self, pos: Vector2, theta: Vector2, color: Color = colors.RED, debug: bool = False) -> None:
        self.original_pos = pos
        self.original_theta = theta.normalize()
        self.reset()

        self.color = color
        self.debug = debug
    
    @classmethod
    def from_random(
        cls, 
        pos: Vector2 = None,
            min_pos_x: float = 0, max_pos_x: float = 100,
            min_pos_y: float = 0, max_pos_y: float = 100,
        theta: Vector2 = None, min_angle: float = 0, max_angle: int = 360
    ):
        if pos is None:
            pos = Vector2(
                min_pos_x + random()*(max_pos_x - min_pos_x),
                min_pos_y + random()*(max_pos_y - min_pos_y)
            )
        if theta is None:
            theta = Vector2()
            theta.from_polar((1, min_angle + random()*(max_angle - min_angle)))
        return Ray(pos, theta)
    
    def reset(self):
        self.collide_point = Vector2(inf, inf)
        self.pos = self.original_pos
        self.theta = self.original_theta
        self.prev_positions: list[Vector2] = [self.original_pos]
        self.reached_target = False
    
    def update(self, new_pos: Vector2, new_theta: Vector2 = Vector2()):
        self.pos = new_pos
        self.prev_positions.append(self.pos)
        try:
            self.theta = new_theta.normalize()
        except ValueError:
            self.theta = Vector2()
        self.collide_point = Vector2(inf, inf)
    
    def set_collide_point(self, collide_point: Vector2):
        prev_mag = (self.collide_point - self.pos).magnitude()
        curr_mag = (collide_point - self.pos).magnitude()
        if curr_mag < prev_mag:
            # print(f'prev {prev_mag}, curr {curr_mag}')
            self.collide_point = collide_point
            return True
        return False

    def score(self):
        # print(self.reached_target)
        return 50 if self.reached_target else 1
    
    def reproduce(self, other: Ray):
        t = random()
        return Ray(
            (self.original_pos + other.original_pos)/2,
            (self.original_theta + other.original_theta)/2
        )
    
    def mutate(self):
        if random() < 0.5:
            self.theta.from_polar((1, random()*360))
        else:
            self.original_pos.x += random() * 600
            self.original_pos.y += random() * 600
        # self.original_theta = self.original_theta.normalize()
        self.reset()

    def draw(self, surface: Surface):
        try:
            draw.aalines(surface, self.color, False, self.prev_positions)
        except ValueError:
            pass
        
        if self.theta.x == 0 and self.theta.y == 0:
            draw.circle(surface, self.color, self.pos, 5)
        else:
            draw.line(surface, self.color, self.pos, self.pos + 10 * self.theta)
            
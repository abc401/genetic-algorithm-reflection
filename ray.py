from pygame import Vector2, Surface, draw, Color
from math import inf, isinf
import colors


class Ray:
    def __init__(self, pos: Vector2, theta: Vector2, color: Color = colors.RED, debug: bool = False) -> None:
        self.original_pos = pos
        self.original_theta = theta.normalize()
        self.reset()

        self.color = color
        self.debug = debug
    
    def reset(self):
        self.collide_point = Vector2(inf, inf)
        self.pos = self.original_pos
        self.theta = self.original_theta
        self.prev_positions: list[Vector2] = [self.original_pos]
    
    def update(self, new_pos: Vector2, new_theta: Vector2 = Vector2()):
        self.pos = new_pos
        self.prev_positions.append(self.pos)
        try:
            self.theta = new_theta.normalize()
        except ValueError:
            self.theta = new_theta
        self.collide_point = Vector2(inf, inf)
    
    def set_collide_point(self, collide_point: Vector2):
        prev_mag = (self.collide_point - self.pos).magnitude()
        curr_mag = (collide_point - self.pos).magnitude()
        if curr_mag < prev_mag:
            # print(f'prev {prev_mag}, curr {curr_mag}')
            self.collide_point = collide_point
            print(f'curr < prev')
            return True
        print(f'curr > prev')
        return False

    # def score(self, target: Target):
        

    def draw(self, surface: Surface):
        try:
            draw.aalines(surface, self.color, False, self.prev_positions)
        except ValueError:
            pass
        if self.debug:
            if self.theta.x == 0 and self.theta.y == 0:
                draw.circle(surface, self.color, self.pos, 10)
            else:
                draw.line(surface, self.color, self.pos, self.pos + 10 * self.theta)
                
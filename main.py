from app import App

from pygame.event import Event
from pygame import Vector2, draw
import pygame

from ray import Ray
from bound import LineBound

import colors


class Main(App):
    def __init__(self, width: int = 600, height: int = 600, fps: float = 120) -> None:
        super().__init__(width, height, fps)
        self.ray = Ray(
            Vector2(50, 50),
            Vector2(1, 1),
            colors.RED
        )
        self.bound = LineBound(
            Vector2(100, 50),
            Vector2(100, 300)
        )

    def update(self, dt):
        mouse = Vector2(pygame.mouse.get_pos())
        self.bound.p1 = mouse
    
    def draw(self):
        self.surface.fill(colors.WHITE)
        self.ray.draw(self.surface)
        self.bound.draw(self.surface)
        collide_point = self.bound.collide(self.ray)
        if collide_point:
            draw.circle(self.surface, colors.GREEN, self.bound.collide(self.ray), 2)
            # self.surface.set_at((int(self.bound.collide(self.ray).x), int(self.bound.collide(self.ray).y)), colors.GREEN)

    def event_handler(self, event: Event):
        pass
    
if __name__ == '__main__':
    Main().run()
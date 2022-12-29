from app import App

from pygame.event import Event
from pygame import Vector2, draw
import pygame
from random import random

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
        self.bounds = [
            LineBound(
                Vector2(random() * self.width, random() * self.height),
                Vector2(random() * self.width, random() * self.height),
            )
            for i in range(5)
        ]

    def update(self, dt):
        mouse = Vector2(pygame.mouse.get_pos())
        self.ray.look_at(mouse)
        [bound.interact(self.ray) for bound in self.bounds]
        pass
    
    def draw(self):
        self.surface.fill(colors.WHITE)
        self.ray.draw(self.surface)
        [bound.draw(self.surface) for bound in self.bounds]

    def event_handler(self, event: Event):
        pass
    
if __name__ == '__main__':
    Main().run()
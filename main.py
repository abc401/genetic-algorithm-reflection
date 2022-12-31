from app import App

from pygame.event import Event
from pygame import Vector2, draw
import pygame
from random import random

from ray import Ray
from interactables import ReflectorObstacle

import colors


class Main(App):
    def __init__(self, width: int = 600, height: int = 600, fps: float = 120) -> None:
        super().__init__(width, height, fps)
        self.ray = Ray(
            Vector2(50, 50),
            Vector2(1, 1),
            colors.RED
        )
        self.interactable = ReflectorObstacle(
            [
                Vector2(100, 100), 
                Vector2(150, 200),
                Vector2(300, 150)
            ], 
            view_normals=True
        )
        # self.bounds = [
        #     LineObstacle(
        #         Vector2(random() * self.width, random() * self.height),
        #         Vector2(random() * self.width, random() * self.height),
        #     )
        #     for i in range(5)
        # ]

    def update(self, dt):
        pass
        mouse = Vector2(pygame.mouse.get_pos())
        # self.ray.look_at(mouse)
        self.interactable.vertices[1] = mouse
        # [bound.interact(self.ray) for bound in self.bounds]
    
    def draw(self):
        self.surface.fill(colors.WHITE)
        # self.ray.draw(self.surface)
        # [bound.draw(self.surface) for bound in self.bounds]
        self.interactable.draw(self.surface)
        end = Vector2()
        end.from_polar((90, 45))
        draw.line(self.surface, colors.BLACK, Vector2(), end)

    def event_handler(self, event: Event):
        pass
    
if __name__ == '__main__':
    Main().run()
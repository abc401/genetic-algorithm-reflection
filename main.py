from app import App

from pygame.event import Event
from pygame import Vector2, draw
import pygame
from random import random

from level import Level
from ray import Ray
from interactables import Reflector, Absorber

import colors


class Main(App):
    def __init__(self, width: int = 600, height: int = 600, fps: float = 120) -> None:
        super().__init__(width, height, fps)
        self.level = Level(
            [
                Reflector(
                    [
                        Vector2(400, 150),
                        Vector2(150, 200),
                        Vector2(300, 20)
                    ]
                ),
                Absorber(
                    [
                        Vector2(250, 250),
                        Vector2(350, 250),
                        Vector2(350, 350),
                        Vector2(250, 350)
                    ]
                )
            ],
            []
        )
        self.ray = Ray(
            Vector2(50, 50),
            Vector2(10, 1),
            colors.RED,
            True
        )

    def update(self, dt):
        self.ray.reset()
        mouse = Vector2(pygame.mouse.get_pos())
        self.level.obstacles[0].vertices[1] = mouse
        self.level.evaluate(self.ray)

    def draw(self):
        self.surface.fill(colors.WHITE)
        self.level.draw(self.surface)
        self.ray.draw(self.surface)

    def event_handler(self, event: Event):
        pass


if __name__ == '__main__':
    Main().run()

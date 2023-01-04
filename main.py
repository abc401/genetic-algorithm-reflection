from app import App

from pygame.event import Event
from pygame import Vector2, draw
import pygame
from random import random

from level import Level
from ray import Ray
from interactables import Reflector, Absorber
from genetics import GeneticsManeger

import colors


class Main(App):
    def __init__(self, width: int = 600, height: int = 600, fps: float = 120) -> None:
        super().__init__(width, height, fps)
        self.genetic_manager = GeneticsManeger(500, self.creature_generator, self.environment_generator)
        # self.level = Level(
        #     [
        #         Reflector(
        #             [
        #                 Vector2(400, 150),
        #                 Vector2(350, 200),
        #                 Vector2(300, 20)
        #             ]
        #         ),
        #         Absorber(
        #             [
        #                 Vector2(250, 250),
        #                 Vector2(350, 250),
        #                 Vector2(350, 350),
        #                 Vector2(250, 350)
        #             ],
        #             closed=True
        #         ),
        #         Absorber(
        #             [
        #                 Vector2(0, -1),
        #                 Vector2(self.width, -1),
        #                 Vector2(self.width, self.height),
        #                 Vector2(0, self.height)
        #             ],
        #             closed=True
        #         )
        #     ],
        #     []
        # )
        # self.ray = Ray(
        #     Vector2(50, 50),
        #     Vector2(10, 1),
        #     colors.RED,
        #     True
        # )
    
    def creature_generator(self) -> Ray:
        return Ray.from_random(
            pos=Vector2(500, 20)
        )
        return Ray.from_random(
           min_pos_x=0, max_pos_x=600, min_pos_y=0, max_pos_y=600 
        )
    
    def environment_generator(self) -> Level:
        return Level(
            [
                Reflector(
                    [
                        Vector2(400, 150),
                        Vector2(350, 200),
                        Vector2(300, 20)
                    ]
                ),
                Absorber(
                    [
                        Vector2(0, -1),
                        Vector2(self.width, -1),
                        Vector2(self.width, self.height),
                        Vector2(0, self.height)
                    ],
                    closed=True
                ),
                Absorber(
                    [
                        Vector2(250, 250),
                        Vector2(350, 250),
                        Vector2(350, 350),
                        Vector2(250, 350)
                    ],
                    closed=True,
                    is_target=True
                )
            ]
        )
        

    def update(self, dt):
        # self.ray.reset()
        # mouse = Vector2(pygame.mouse.get_pos())
        # self.level.obstacles[0].vertices[1] = mouse
        # self.level.evaluate(self.ray)
        pass

    def draw(self):
        self.surface.fill(colors.WHITE)
        self.genetic_manager.draw(self.surface)
        # self.level.draw(self.surface)
        # self.ray.draw(self.surface)

    def event_handler(self, event: Event):
        pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # print(f'space')
                self.genetic_manager.reproduce()


if __name__ == '__main__':
    Main().run()

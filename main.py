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
        self.interacted_rays = []
        self.ray = Ray(
            Vector2(50, 50),
            Vector2(10, 1),
            colors.RED
        )
        self.ref_ray = Ray(Vector2(), Vector2(10, 10))
        self.interactable = ReflectorObstacle(
            [
                Vector2(400, 150), 
                Vector2(150, 200),
                Vector2(300, 20)
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
        self.interacted_rays = [self.ray]
        self.ray.update()
        mouse = Vector2(pygame.mouse.get_pos())
        # self.ray.look_at(mouse)
        self.interactable.vertices[1] = mouse
        tmp = self.interactable.interact(self.ray)
        for i in range(10):
            if tmp is None:
                break
            self.interacted_rays.append(tmp)
            tmp = self.interactable.interact(tmp)
    
    def draw(self):
        self.surface.fill(colors.WHITE)
        for ray in self.interacted_rays:
            ray.draw(self.surface)
        # self.ray.draw(self.surface)
        # self.ref_ray.draw(self.surface)

        # print(self.ray.pos, self.ray.theta)
        # print(self.ref_ray.pos, self.ref_ray.theta)
        # print(self.ref_ray.theta.angle_to(Vector2(1, 0)))
        # [bound.draw(self.surface) for bound in self.bounds]
        self.interactable.draw(self.surface)
        end = Vector2(10, 1)
        end.from_polar((90, 135))
        draw.line(self.surface, colors.BLACK, Vector2(300, 300), end)

    def event_handler(self, event: Event):
        pass
    
if __name__ == '__main__':
    Main().run()
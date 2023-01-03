from interactables import Interactable
from ray import Ray
from pygame import Surface


class Level:
    def __init__(self, obstacles: list[Interactable], targets: list[Interactable]) -> None:
        self.obstacles = obstacles
        self.targets = targets
        self.interactables = self.obstacles + self.targets
        self.max_interactions = 30
    
    def evaluate(self, ray: Ray):
        for _ in range(self.max_interactions):
            min_obstacle_index = None
            min_seg_index = None
            for i, obstacle in enumerate(self.interactables):
                can_interact, collide_point, seg_index = obstacle.can_interact_with(ray)
                if not can_interact:
                    # print(f'cannot interact {i}')
                    continue
                print(f'can interact {can_interact}, {i}, seg {seg_index}')
                print(f'set collide {i}')
                min_obstacle_index = i
                min_seg_index = seg_index
             
            if min_obstacle_index is None:
                print(f'min_obstacle None')
                break

            self.interactables[min_obstacle_index].interact_with_segment(ray, min_seg_index)
            print(min_obstacle_index)

            if self.interactables[min_obstacle_index] in self.targets:
                break
    
    def draw(self, surface: Surface):
        for interactable in self.interactables:
            interactable.draw(surface)


        
import pygame
from abc import ABC, abstractmethod

class App(ABC):
    def __init__(
        self,
        width: int = 0,
        height: int = 0,
        fps: float = 60
    ) -> None:
        
        
        pygame.init()
        self.fps = fps
        self.dt = 1/fps
        self.clock = pygame.time.Clock()
        self.flags = 0
        if not width or not height:
            self.flags = pygame.FULLSCREEN
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((width, height), self.flags)
        self.running = False
    
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def update(self, dt):
        pass
    
    @abstractmethod
    def event_handler(self, event: pygame.event.Event):
        pass
    
    def run(self):
        self.running = True
        while(self.running):
            self.draw()
            pygame.display.update()
            
            self.update(self.dt)
            
            for event in pygame.event.get():
                self.event_handler(event)
                if event.type == pygame.QUIT:
                    self.running = False
            self.dt = self.clock.tick(self.fps)

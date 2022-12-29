from app import App
from pygame.event import Event


class Main(App):
    def __init__(self, width: int = 600, height: int = 600, fps: float = 120) -> None:
        super().__init__(width, height, fps)

    def update(self, dt):
        return super().update(dt)
    
    def draw(self):
        return super().draw()
    
    def event_handler(self, event: Event):
        return super().event_handler(event)

if __name__ == '__main__':
    Main().run()
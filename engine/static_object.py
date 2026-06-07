import pygame
from engine.game_object import GameObject


class StaticObject(GameObject):
    def __init__(self, x=0, y=0, color=(255, 0, 0), size=50):
        super().__init__(x, y, size)

        self.color = color

    def update(self, scene):
        pass

    def render(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.size, self.size)
        )
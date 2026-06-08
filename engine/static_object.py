import pygame
from engine.game_object import GameObject


class StaticObject(GameObject):
    def __init__(self, x, y, size=50, color=(255, 0, 0)):
        super().__init__(x, y, size)
        self.color = color

    def update(self, scene):
        pass

    def render_with_camera(self, screen, camera):
        pygame.draw.rect(
            screen,
            self.color,
            (
                self.x - camera.x,
                self.y - camera.y,
                self.size,
                self.size
            )
        )
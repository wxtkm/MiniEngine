import pygame
from engine.game_object import GameObject


class Sprite(GameObject):
    def __init__(self, x=0, y=0, color=(0, 255, 0), size=50, speed=5):
        super().__init__(x, y, size)

        self.color = color
        self.speed = speed

    def update(self, scene):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_a]:
            dx = -self.speed
        elif keys[pygame.K_d]:
            dx = self.speed

        if keys[pygame.K_w]:
            dy = -self.speed
        elif keys[pygame.K_s]:
            dy = self.speed

        # движение с коллизией
        if not scene.check_collision(self, dx, 0):
            self.x += dx

        if not scene.check_collision(self, 0, dy):
            self.y += dy

        self.x = max(0, self.x)
        self.y = max(0, self.y)

        self.x = min(self.x, scene.width - self.size if hasattr(scene, "width") else 800 - self.size)
        self.y = min(self.y, scene.height - self.size if hasattr(scene, "height") else 600 - self.size)

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
import pygame
import sys
from engine.scene import Scene
from engine.sprite import Sprite


class Game:
    def __init__(self, width=800, height=600, title="MiniEngine"):
        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        self.width, self.height = self.screen.get_size()

        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.running = False

        self.scene = Scene()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.scene.update()
        self.check_win()

    def render(self):
        self.screen.fill((30, 30, 30))
        self.scene.render(self.screen)
        pygame.display.flip()

    def check_win(self):
        player = self.scene.get_player()
        if not player:
            return

        if player.x > self.width - player.size:
            print("YOU WIN!")
            self.running = False

    def run(self):
        self.running = True

        while self.running:
            self.clock.tick(60)

            self.handle_events()
            self.update()
            self.render()

        pygame.quit()
        sys.exit()
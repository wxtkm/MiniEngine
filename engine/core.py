import pygame
import sys
from engine.scene import Scene
from engine.sprite import Sprite
from engine.camera import Camera



class Game:
    def __init__(self, width=800, height=600, title="MiniEngine"):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width, self.height = self.screen.get_size()

        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.running = False

        self.scene = Scene(self.width, self.height)

        self.background_color = (30, 30, 30)

        self.camera = Camera(self.width, self.height)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.scene.update()

        player = self.scene.get_player()

        if player:
            self.camera.follow(player)

    def render(self):
        self.screen.fill(self.background_color)
        self.scene.render(self.screen, self.camera)
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
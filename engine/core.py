import pygame
import sys


class Game:
    def __init__(self, width=800, height=600, title="MiniEngine"):
        pygame.init()

        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.running = False

        self.fps = 60

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass  # логика игры будет здесь

    def render(self):
        self.screen.fill((30, 30, 30))  # фон
        pygame.display.flip()

    def run(self):
        self.running = True

        while self.running:
            self.clock.tick(self.fps)

            self.handle_events()
            self.update()
            self.render()

        self.quit()

    def quit(self):
        pygame.quit()
        sys.exit()
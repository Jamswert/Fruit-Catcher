import pygame
from config.settings import BG_COLOUR, WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from src.sprites import Player

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption(WINDOW_TITLE)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.framerate = FPS
        self.clock = pygame.time.Clock()
        self.delta_time = 0.1
        self.running = True

        self.player = None
        self.all_sprites = None
        self.fruit_sprite = None

        self.setup_sprites()

    def setup_sprites(self):
        self.all_sprites = pygame.sprite.Group()
        self.fruit_sprites = pygame.sprite.Group()

        self.player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50)
        self.all_sprites.add(self.player)

    def tick(self):
        self.delta_time = self.clock.tick(self.framerate) / 1000
        self.delta_time = max(0.001, min(0.1, self.delta_time))
    
    def main(self):
        while self.running:
            self.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.all_sprites.update(self.delta_time)

            self.screen.fill(BG_COLOUR)

            self.all_sprites.draw(self.screen)

            pygame.display.flip()
        
        pygame.quit()
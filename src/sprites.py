from typing import override
import pygame
from config.settings import BASE_SPRITE_SIZE, PLAYER_SPRITE, SPRITE_SCALE, WINDOW_WIDTH, WINDOW_HEIGHT

class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        # Convert Path object to string if needed (pygame.image.load accepts both, but explicit is clearer)
        path_str = str(image_path) if hasattr(image_path, '__str__') else image_path
        self.image = pygame.image.load(path_str).convert_alpha()

        self.image = pygame.transform.scale(self.image, (BASE_SPRITE_SIZE  * SPRITE_SCALE, BASE_SPRITE_SIZE * SPRITE_SCALE))

        self.rect = self.image.get_rect(topleft=(x,y))
    
    def update(self, delta_time):
        pass

class Player(BaseSprite):
    def __init__(self, x, y):
        super().__init__(PLAYER_SPRITE, x, y)

        self.fruit_sprite_ref = None
        

        self.base_y = y

    @override
    def update(self, delta_time):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        sprite_center_x = mouse_x - (self.rect.width // 2)
        
        
        clamped_x = max(0, min(sprite_center_x, WINDOW_WIDTH - self.rect.width))
        
        self.rect.x = clamped_x
        self.rect.y = self.base_y
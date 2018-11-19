import pygame
from pygame.sprite import Sprite

class Officer(Sprite):
    def __init__(self, screen, game_settings):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("img/up.png").convert_alpha()
        self.image = pygame.transform.scale(self.image , (150,150))
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

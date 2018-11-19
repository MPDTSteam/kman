import pygame
from pygame import *
from settings import Settings

game_settings = Settings()

class Boost(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spd_.png")
        self.rect = Rect(x,y, game_settings.boost_width, game_settings.boost_height)
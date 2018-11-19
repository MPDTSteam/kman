import pygame
from pygame import *
from settings import Settings

game_settings = Settings()

class Wall(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/walls.png")
        self.rect = Rect(x,y, game_settings.wall_width, game_settings.wall_height)
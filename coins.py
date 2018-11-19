import pygame
from pygame import *
from settings import Settings

game_settings = Settings()

class Coin(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/coin.png")
        self.rect = Rect(x,y, game_settings.coin_width, game_settings.coin_height)
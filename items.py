import pygame
from pygame import *
from settings import Settings

game_settings = Settings()

class Wall(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/l2_walls.jpg")
        self.rect = Rect(x,y, game_settings.wall_width, game_settings.wall_height)

class GrassWall(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/grass.jpg").convert_alpha()
        self.rect = Rect(x,y, game_settings.wall_width, game_settings.wall_height)


class Boost(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/speed.png")
        self.rect = Rect(x,y, game_settings.boost_width, game_settings.boost_height)

class Door(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/door_c.png")
        self.rect = Rect(x,y, game_settings.door_width, game_settings.door_height)


class Teleport(sprite.Sprite):
    def __init__(self, x, y, goX, goY):
        sprite.Sprite.__init__(self)
        self.goX = goX
        self.goY = goY
        self.image = pygame.image.load("img/portal.png")
        self.rect = Rect(x, y, game_settings.tp_width, game_settings.tp_height)
    def update(self):
        self.image.blit(self.image,(0,0))
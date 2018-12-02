import pygame
from pygame import *
from settings import Settings

game_settings = Settings()

class Coin(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/coin.png")
        self.rect = Rect(x,y, game_settings.coin_width, game_settings.coin_height)

class Wall(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/l2_walls.jpg")
        self.rect = Rect(x,y, game_settings.wall_width, game_settings.wall_height)

class Side_Wall(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/l2_sidewall.jpg")
        self.rect = Rect(x,y, game_settings.wall_width, game_settings.wall_height)

class Edge_Wall(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/l2_edgewall.jpg")
        self.rect = Rect(x,y, game_settings.wall_width, game_settings.wall_height)

class Center_Wall(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/c_wall.jpg")
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
        self.goX = goX  # координаты назначения перемещения
        self.goY = goY  # координаты назначения перемещения
        self.image = pygame.image.load("img/portal.png")
        self.rect = Rect(x, y, game_settings.wall_width, game_settings.wall_height)
    def update(self):
        self.image.blit(self.image,(0,0))
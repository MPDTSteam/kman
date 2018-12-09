import pygame
from pygame import *
from settings import Settings
from items import *
import items

g_f = Settings()
animCount = 0
walkDown = [pygame.image.load("img/bot2_animation_main.png"),pygame.image.load("img/bot_main_2.png"), pygame.image.load("img/bot2_animation_main2.png")]
walkUp = [pygame.image.load("img/bot2_animation_back.png"),pygame.image.load("img/bot_2_back_2.png"), pygame.image.load("img/bot2_animation_back_2.png")]
walkLeft = [pygame.image.load("img/bot2_animation_left.png"),pygame.image.load("img/bot2_animation_left_2.png")]
walkRight = [pygame.image.load("img/bot2_animation_right.png"),pygame.image.load("img/bot2_right.png")]
class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen,x,y):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("img/bot_main_2.png").convert_alpha()  #розмір героя
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.yvel = 0
        self.speed = g_f.e_speed
        self.rect = Rect(x,y, 45, 55)


    def blitme(self):
        self.screen.blit(self.image, self.rect)

                                       #рух


    def update(self,e_left,e_right,e_up,e_down,walls,doors,grass):
        global animCount

        if animCount + 1 >= 30:
            animCount = 0
        if e_up:
            #self.xvel = 0
            self.yvel = -self.speed
            self.image = walkUp[animCount // 10]
            animCount += 1
        if e_down:
            #self.xvel = 0
            self.yvel = self.speed
            self.image = walkDown[animCount // 10]
            animCount += 1
        if e_left:
            #self.yvel = 0
            self.xvel = -self.speed
            self.image = walkLeft[animCount // 15]
            animCount += 1
        if e_right:
            #self.yvel = 0
            self.xvel = self.speed
            self.image = walkRight[animCount // 15]
            animCount += 1
        if not (e_left or e_right) and not (e_up or e_down):
            self.xvel = 0
            self.yvel = 0
            self.image = pygame.image.load("img/bot_main_2.png")
        self.rect.y += self.yvel
        self.collide(0,self.yvel,walls,doors,grass)

        self.rect.x += self.xvel
        self.collide(self.xvel,0,walls,doors,grass)

    def collide(self,xvel,yvel,walls,doors,grass):
        for w in walls:
            if sprite.collide_rect(self,w):

                if xvel > 0:
                    self.rect.right = w.rect.left

                if xvel < 0:
                    self.rect.left = w.rect.right

                if yvel > 0:
                    self.rect.bottom = w.rect.top
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = w.rect.bottom
                    self.yvel = 0
        for d in doors:
            if sprite.collide_rect(self,d):

                if xvel > 0:
                    self.rect.right = d.rect.left

                if xvel < 0:
                    self.rect.left = d.rect.right

                if yvel > 0:
                    self.rect.bottom = d.rect.top
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = d.rect.bottom
                    self.yvel = 0
        for g in grass:
            if sprite.collide_rect(self,g):
                if isinstance(g, items.GrassWall):
                    self.speed = g_f.e_speed - 5
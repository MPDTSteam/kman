import pygame, random
from pygame import *
from settings import Settings
import items
from hero_enemy import Enemy
pygame.init()
tp_sound = pygame.mixer.Sound("tp.wav")
animCount = 0
g_f = Settings()
walkDown = [pygame.image.load("img/animation_main.png"),pygame.image.load("img/down.png"), pygame.image.load("img/animation_main_2.png")]
walkUp = [pygame.image.load("img/animation_back.png"),pygame.image.load("img/up.png"), pygame.image.load("img/animation_back_2.png")]
walkLeft = [pygame.image.load("img/animation_left.png"),pygame.image.load("img/left.png"), pygame.image.load("img/animation_left_2.png")]
walkRight = [pygame.image.load("img/animation_right.png"),pygame.image.load("img/right.png"), pygame.image.load("img/animation_right_2.png")]
class Hero(pygame.sprite.Sprite):
    def __init__(self,screen,x,y):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("img/left.png").convert_alpha()  #розмір героя
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.yvel = 0
        self.speed = g_f.h_speed
        self.rect = Rect(x,y, 45, 55)
        self.start_ticks_speed = 0
        self.random_boost = False


    def blitme(self):
        self.screen.blit(self.image, self.rect)

                                       #рух


    def update(self,left,right,up,down,walls,grass):
        global animCount

        if animCount + 1 >= 27:
            animCount = 0
        if up:
            self.xvel = 0
            self.yvel = -self.speed
            self.image = walkUp[animCount // 10]
            animCount += 1
        if down:
            self.xvel = 0
            self.yvel = self.speed
            self.image = walkDown[animCount // 10]
            animCount += 1
        if left:
            self.yvel = 0
            self.xvel = -self.speed
            self.image = walkLeft[animCount // 15]
            animCount += 1
        if right:
            self.yvel = 0
            self.xvel = self.speed
            self.image = walkRight[animCount // 15]
            animCount += 1
        if not (left or right) and not (up or down):
            self.xvel = 0
            self.yvel = 0
            self.image = pygame.image.load("img/down.png")
        self.rect.y += self.yvel
        self.collide(0,self.yvel,walls,grass)

        self.rect.x += self.xvel
        self.collide(self.xvel,0,walls,grass)


    def collide(self,xvel,yvel,walls,grass):
        for w in walls:
            if sprite.collide_rect(self,w):
                if isinstance(w, items.Teleport):
                    tp_sound.play()
                    self.teleporting(w.goX, w.goY)
                else:
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
        for g in grass:
            if sprite.collide_rect(self,g):
                if isinstance(g, items.GrassWall):
                    self.speed = g_f.h_speed - 5
    def teleporting(self,goX,goY):
        self.rect.x = goX
        self.rect.y = goY
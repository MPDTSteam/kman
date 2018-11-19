import pygame, sys, random
from pygame import *
from settings import Settings
from hero import Hero
import game_function as  g_f
from pygame.sprite import Group
from coins import Coin
from menu import Menu
from wall import Wall
from hero_enemy import Enemy
from boosts import Boost



def init_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width,game_settings.height))  # екран
    bg = pygame.image.load("img/background.jpg")
    pygame.display.set_caption("Kursant Man")  #назва гри
    officers = Group()
    hero = Hero(screen,15,15)

    left = False
    right = False
    up = False
    down = False
    e_left = False
    e_right = False
    e_down = False
    e_up = False
    punkts = [(1010, 85, u'Play', (0, 0, 0), (128, 0, 0), 0),
              (960, 177, u'Settings', (0, 0, 0), (128, 0, 0), 1),
              (1010, 270, u'Exit', (0, 0, 0), (128, 0, 0), 2)]
    game = Menu(punkts)
    game.menu(screen)

    #g_f.create_fleet(screen, game_settings, officers, hero)

    entities = pygame.sprite.Group()
    walls = []
    boosts = []
    coins = []
#33x23
    level = [
            "-------------------------------------------------------------------------------------",
            "-       -     -     -     -                                       -                 -",
            "-       -     -     -     -                                       -                 -",
            "-       -     -     -     -                                       -                 -",
            "-       -     -     -     -                                       -                 -",
            "-       -                        ---------------------------      -                 -",
            "-       -                        ---------------------------      -                 -",
            "-       -                                                         -------------     -",
            "-       -                                                                     -     -",
            "-    B  -------------     -                                                   -     -",
            "-                   -     -                                                   -     -",
            "-                   -     -------    ----------------                         -     -",
            "-                   -           -    -              -             -------------     -",
            "-                   -           -    -              -                               -",
            "-                   -           -    -              -                               -",
            "-         ------    -           -    -              -                               -",
            "-         -    -    --------    ----------------    -                               -",
            "------    -    -           -                        -                               -",
            "-         -    -           -                        ---------------------           -",
            "-         -    -           -                                            -           -",
            "-         -    -           -                                            -           -",
            "-         -    -           -                                            -           -",
            "-         -    -     -     ---------    --------                        -           -",
            "-         -    -     -     -            -      -                        -           -",
            "-     -----    -     -     -            -      -                        -           -",
            "-     -        -     -     -            -      -    ---------------------           -",
            "-     -        -     -     -            -      -    -                               -",
            "-     -        -     -     ---------    -      -    -                               -",
            "-     -        -     -                              -                               -",
            "-     -----    -     -                              -                               -",
            "-              -     -                              -                               -",
            "-              -     -                              -                               -",
            "-              -     -     --------------------------                               -",
            "-              -     -     -                                --------------------    -",
            "-              -     -     -                                -                       -",
            "-     ----------------     -                                -                       -",
            "-              -           -                                -                       -",
            "-              -           -    --------------              -                       -",
            "-              -           -    -            -              -                       -",
            "-              -           -    -            -         -----------       ------------",
            "-              -           ------            -         -    -                       -",
            "-     ----------     -     -    -            -         -    -                       -",
            "-              -     -     -    -            ----      -    -                       -",
            "-              -     -     -    -                      -    -                       -",
            "-              -     -     -                                -                  E    -",
            "-              -     -     -                                -                       -",
            "-              -     -     -                                -                       -",
            "-              -     -     -                                -                       -",
            "-------------------------------------------------------------------------------------"]

    x = y = 0
    for row in level:
        for col in row:
            if col == "-":
                wall = Wall(x, y)
                entities.add(wall)
                walls.append(wall)
            x += game_settings.wall_width
            if col == "B":
                boost = Boost(x,y)
                entities.add(boost)
                boosts.append(boost)
            if col == "E":
                enemy = Enemy(screen, x, y)

        y += game_settings.wall_height
        x = 0



    while True:    #цикл який не дає закривати гру
        pygame.time.Clock().tick(100)
        g_f.update_screen(hero,enemy, screen,officers,game_settings)
        entities.draw(screen)
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit
            if e.type == KEYDOWN:
                if e.key == K_UP:
                    up = True
                    down = False
                    left = False
                    right = False
                if e.key == K_DOWN:
                    down = True
                    up = False
                    left = False
                    right = False
                if e.key == K_RIGHT:
                    right = True
                    down = False
                    left = False
                    up = False
                if e.key == K_LEFT:
                    left = True
                    down = False
                    up = False
                    right = False
                if e.key == K_w:
                    e_up = True
                    e_down = False
                    e_left = False
                    e_right = False
                if e.key == K_s:
                    e_down = True
                    e_up = False
                    e_left = False
                    e_right = False
                if e.key == K_d:
                    e_right = True
                    e_down = False
                    e_left = False
                    e_up = False
                if e.key == K_a:
                    e_left = True
                    e_down = False
                    e_up = False
                    e_right = False
            if e.type == KEYUP:
                if e.key == K_UP:
                    up = False
                if e.key == K_DOWN:
                    down = False
                if e.key == K_RIGHT:
                    right = False
                if e.key == K_LEFT:
                    left = False
                if e.key == K_w:
                    e_up = False
                if e.key == K_s:
                    e_down = False
                if e.key == K_d:
                    e_right = False
                if e.key == K_a:
                    e_left = False
        if sprite.collide_rect(hero,enemy):
            init_game()
            # hero = Hero(screen, 15, 15)
            # enemy = Enemy(screen, 300, 300)
        if sprite.collide_rect(hero,boost):
            hero.speed = 15
            entities.remove(boost)
            boost = Boost(10000,10000)
            entities.update()

        screen.blit(bg,(0,0))
        hero.update(left, right, up, down, walls)
        enemy.update(e_left,e_right,e_up,e_down,walls)
        entities.draw(screen)
        for e in entities:
            screen.blit(e.image,(0,0))
init_game()





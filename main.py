import pygame, sys, random
from pygame import *
from os import path
from settings import Settings
from hero import Hero
from pygame.sprite import Group
from items import *
from hero_enemy import Enemy

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.music.load("game.mp3")
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play(-1)
current_map = "level1.txt"
pygame.font.init()
speed_font = pygame.font.Font(None, 32)
inf_font = pygame.font.SysFont(None, 24, True)
label_font = pygame.font.SysFont(None, 32, True)
step_sound = pygame.mixer.Sound("Step.wav")
win_sound = pygame.mixer.Sound("Victory.wav")
lose_sound = pygame.mixer.Sound("Lose.wav")
boost_sound = pygame.mixer.Sound("Zgushik.wav")
tp_sound = pygame.mixer.Sound("tp.wav")
end_sound = pygame.mixer.Sound("End.wav")
class End_Menu():
    def emenu(self,screen):
        done = True
        while done:
            screen.blit(pygame.transform.scale(pygame.image.load("end.jpg").convert_alpha(), (1920, 1080)),(0, 0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    sys.exit()

            screen.blit(screen, (0, 0))
            pygame.display.flip()
class Kursant_Menu():
    def __init__(self, LevelPunkts = [120, 140, u'Punkt', (250, 250, 30), (250, 30, 250)],current_map = "level1.txt"):
        self.punkts = LevelPunkts
        self.map = current_map
    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def lmenu(self,screen):
        done = True
        font_menu = pygame.font.Font(None, 70)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen.blit(pygame.transform.scale(pygame.image.load("img/off_won.png").convert_alpha(),(1920,1080)), (0,0))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_RIGHT:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        init_menu()
                    elif punkt == 1:
                        if self.map == "level1.txt":
                            init_game("level1.txt")
                        elif self.map == "level2.txt":
                            init_game("level2.txt")
                        elif self.map == "level3.txt":
                            init_game("level3.txt")
                    elif punkt == 2:
                        if self.map == "level1.txt":
                            init_game("level2.txt")
                        elif self.map == "level2.txt":
                            init_game("level3.txt")


            screen.blit(screen, (0, 0))
            pygame.display.flip()


class Officer_Menu():
    def __init__(self, Officer_Punkts=[120, 140, u'Punkt', (250, 250, 30), (250, 30, 250)],current_map = "level1.txt"):
        self.punkts = Officer_Punkts
        self.map = current_map

    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def lmenu(self, screen):
        done = True
        font_menu = pygame.font.Font(None, 100)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen.blit(pygame.transform.scale(pygame.image.load("img/off_win.png").convert_alpha(), (1920, 1080)), (0, 0))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_RIGHT:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        init_menu()
                    elif punkt == 1:
                        if self.map == "level1.txt":
                            init_game("level1.txt")
                        elif self.map == "level2.txt":
                            init_game("level2.txt")
                        elif self.map == "level3.txt":
                            init_game("level3.txt")
            screen.blit(screen, (0, 0))
            pygame.display.flip()


class Menu:
    def __init__(self, MenuPunkts = [120, 140, u'Punkt', (250, 250, 30), (250, 30, 250)]):
        self.punkts = MenuPunkts
    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self,screen):
        done = True
        font_menu = pygame.font.Font(None, 70)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen.blit(pygame.transform.scale(pygame.image.load("img/menu.jpeg").convert_alpha(),(1920,1080)), (0,0))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        init_game("level1.txt")
                    elif punkt == 2:
                        sys.exit()
            screen.blit(screen, (0, 0))
            pygame.display.flip()
def init_menu():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    MenuPunkts = [(1540, 125, u'Play', (0, 0, 0), (128, 0, 0), 0),
                  (1490, 247, u'Settings', (0, 0, 0), (128, 0, 0), 1),
                  (1540, 369, u'Exit', (0, 0, 0), (128, 0, 0), 2)]
    start_menu = Menu(MenuPunkts)
    start_menu.menu(screen)


def init_game(current_map):
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width,game_settings.height), pygame.FULLSCREEN)  # екран
    if current_map == "level1.txt":
        hero = Hero(screen,15,15)
        enemy = Enemy(screen,1000,500)
        tp = Teleport(810, 135, 495, 870)
        bg = pygame.transform.scale(pygame.image.load("img/bg1-01.jpeg").convert_alpha(),(1920,1080))
    if current_map == "level2.txt":
        hero = Hero(screen,960, 15)
        enemy = Enemy(screen, 960,1000)
        tp = Teleport(1605, 195, 480, 135)
        bg = pygame.transform.scale(pygame.image.load("img/bg1-02.jpeg").convert_alpha(),(1920,1080))
    if current_map == "level3.txt":
        hero = Hero(screen,1750, 60)
        enemy = Enemy(screen, 960,850)
        tp = Teleport(835, 15, 465, 555)
        bg = pygame.transform.scale(pygame.image.load("img/bg1-01-02.jpeg").convert_alpha(),(1920,1080))
    pygame.display.set_caption("Kursant Man")  #назва гри



    left = False
    right = False
    up = False
    down = False
    e_left = False
    e_right = False
    e_down = False
    e_up = False
    Kursant_Punkts = [(615, 785, u'Menu', (0, 0, 0), (128, 0, 0), 0),
                  (885, 785, u'Restart', (0, 0, 0), (128, 0, 0), 1),
                  (1200, 785, u'Next', (0, 0, 0), (128, 0, 0), 2)]
    Officer_Punkts = [(715, 785, u'Menu', (255, 255, 255), (128, 0, 0), 0),
                  (1100, 785, u'Restart', (255, 255, 255), (128, 0, 0), 1)]
    kurs_menu = Kursant_Menu(Kursant_Punkts,current_map)
    offi_menu = Officer_Menu(Officer_Punkts,current_map)
    end_menu = End_Menu()

    entities = pygame.sprite.Group()
    walls = []
    notwalls = pygame.sprite.Group()
    boosts = []
    grass = []
    doors = []
    entities.add(tp)
    walls.append(tp)
    notwalls.add(tp)
    random_bonuses = pygame.sprite.Group()

    game_folder = path.dirname(__file__)
    map_data = []
    with open(path.join(game_folder, current_map), "rt") as f:
        for line in f:
            map_data.append(line)
    x=y=0
    for row,tiles in enumerate(map_data):
        for col,tile in enumerate(tiles):
            if tile == "0":
                if current_map == "level1.txt":
                    wall = Wall(x, y)
                    entities.add(wall)
                    walls.append(wall)
                    wall.image = pygame.image.load("img/walls.png").convert_alpha()
                if current_map == "level2.txt":
                    wall = Wall(x, y)
                    entities.add(wall)
                    walls.append(wall)
                if current_map == "level3.txt":
                    wall = Wall(x, y)
                    entities.add(wall)
                    walls.append(wall)
                    wall.image = pygame.image.load("img/walls.png").convert_alpha()
            if tile == "B":
                wall = Wall(x, y)
                entities.add(wall)
                walls.append(wall)
                wall.image = pygame.image.load("img/c_wall.jpg").convert_alpha()
            if tile == "A":
                wall = Wall(x, y)
                entities.add(wall)
                walls.append(wall)
                wall.image = pygame.image.load("img/l2_edgewall.jpg").convert_alpha()
            if tile == "C":
                wall = Wall(x, y)
                entities.add(wall)
                walls.append(wall)
                wall.image = pygame.image.load("img/l2_sidewall.jpg").convert_alpha()
            if tile == "G":
                wall = Wall(x,y)
                entities.add(wall)
                walls.append(wall)
                wall.image = pygame.image.load("img/edge_wall.jpg").convert_alpha()
            if tile == "S":
                wall = Wall(x,y)
                entities.add(wall)
                walls.append(wall)
                wall.image = pygame.image.load("img/side_wall.jpg").convert_alpha()
            if current_map == "level3.txt":
                if tile == "T":
                    gwall = GrassWall(x,y)
                    entities.add(gwall)
                    grass.append(gwall)
            if tile == "X":
                if current_map == "level1.txt":
                    wall = Wall(x,y)
                    entities.add(wall)
                    walls.append(wall)
                    wall.image = pygame.image.load("img/exit1.jpg").convert_alpha()
                if current_map == "level2.txt":
                    wall = Wall(x, y)
                    entities.add(wall)
                    walls.append(wall)
                    wall.image = pygame.image.load("img/exit2.jpg").convert_alpha()
            if tile == "d":
                if current_map == "level1.txt":
                    wall = Wall(x, y)
                    entities.add(wall)
                    walls.append(wall)
                    wall.image = pygame.image.load("img/exit1.jpg").convert_alpha()
                if current_map == "level2.txt":
                    wall = Wall(x, y)
                    entities.add(wall)
                    walls.append(wall)
                    wall.image = pygame.image.load("img/exit2.jpg").convert_alpha()
            x+=game_settings.wall_width
            if tile == "E":
                enemy = Enemy(screen,x,y)
            if tile == "D":
                door1 = Door(x,y)
                entities.add(door1)
                doors.append(door1)
            if tile == "d":
                door2 = Door(x,y)
                entities.add(door2)
                doors.append(door2)
                door2.image = pygame.image.load("img/door_c1.png").convert_alpha()
            if tile == "p":
                boost1 = Boost(x,y)
                entities.add(boost1)
                boosts.append(boost1)
            if tile == "o":
                boost2 = Boost(x,y)
                entities.add(boost2)
                boosts.append(boost2)
            if tile == "i":
                boost3 = Boost(x,y)
                entities.add(boost3)
                boosts.append(boost3)

            if tile == "R":
                hero.random_boost = Boost(x,y)
                entities.add(hero.random_boost)
                boosts.append(hero.random_boost)


        y+=game_settings.wall_height
        x=0


    while True:    #цикл який не дає закривати гру
        pygame.time.Clock().tick(60)
        enemy.blitme()
        hero.blitme()
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit
            if e.type == KEYDOWN:
                if e.key == K_UP:
                    up = True
                    down = False
                    left = False
                    right = False
                    step_sound.play()
                if e.key == K_DOWN:
                    down = True
                    up = False
                    left = False
                    right = False
                    step_sound.play()
                if e.key == K_RIGHT:
                    right = True
                    down = False
                    left = False
                    up = False
                    step_sound.play()
                if e.key == K_LEFT:
                    left = True
                    down = False
                    up = False
                    right = False
                    step_sound.play()
                if e.key == K_w:
                    e_up = True
                    e_down = False
                    e_left = False
                    e_right = False
                    step_sound.play()
                if e.key == K_s:
                    e_down = True
                    e_up = False
                    e_left = False
                    e_right = False
                    step_sound.play()
                if e.key == K_d:
                    e_right = True
                    e_down = False
                    e_left = False
                    e_up = False
                    step_sound.play()
                if e.key == K_a:
                    e_left = True
                    e_down = False
                    e_up = False
                    e_right = False
                    step_sound.play()
            if e.type == KEYUP:
                if e.key == K_UP:
                    up = False
                    step_sound.stop()
                if e.key == K_DOWN:
                    down = False
                    step_sound.stop()
                if e.key == K_RIGHT:
                    right = False
                    step_sound.stop()
                if e.key == K_LEFT:
                    left = False
                    step_sound.stop()
                if e.key == K_w:
                    e_up = False
                    step_sound.stop()
                if e.key == K_s:
                    e_down = False
                    step_sound.stop()
                if e.key == K_d:
                    e_right = False
                    step_sound.stop()
                if e.key == K_a:
                    e_left = False
                    step_sound.stop()
        if sprite.collide_rect(hero,enemy):
            lose_sound.play()
            offi_menu.lmenu(screen)
        if sprite.collide_rect(hero,door1):
            door1.image = pygame.image.load("img/door_o.png").convert_alpha()
        if sprite.collide_rect(hero,door2):
            door2.image = pygame.image.load("img/door_c.png").convert_alpha()
        if sprite.collide_rect(hero,boost1):
            hero.speed = hero.speed+2
            entities.remove(boost1)
            boost1 = Boost(10000,10000)
            boost_sound.play()
        if sprite.collide_rect(hero,boost2):
            hero.speed = hero.speed+2
            entities.remove(boost2)
            boost2 = Boost(10000,10000)
            boost_sound.play()
        if sprite.collide_rect(hero,boost3):
            hero.speed = hero.speed+2
            entities.remove(boost3)
            boost3 = Boost(10000,10000)
            boost_sound.play()

        if current_map == "level1.txt":
            if (hero.rect.x > 1290 and hero.rect.x <1470) and (hero.rect.y > 345 and hero.rect.y < 510):
                win_sound.play()
                kurs_menu.lmenu(screen)
            if (hero.rect.x > 135 and hero.rect.x <615) and (hero.rect.y > 705 and hero.rect.y < 810):
                win_sound.play()
                kurs_menu.lmenu(screen)
        if current_map == "level2.txt":
            if (hero.rect.x > 1365 and hero.rect.x <1800) and (hero.rect.y > 600 and hero.rect.y < 750):
                win_sound.play()
                kurs_menu.lmenu(screen)
            if (hero.rect.x > 105 and hero.rect.x <555) and (hero.rect.y > 810 and hero.rect.y < 960):
                win_sound.play()
                kurs_menu.lmenu(screen)
        if current_map == "level3.txt":
            if hero.rect.y > 1065:
                end_sound.play()
                end_menu.emenu(screen)
        screen.blit(bg,(0,0))
        hero.update(left, right, up, down, walls,grass)
        enemy.update(e_left,e_right,e_up,e_down,walls,doors,grass)
        notwalls.update()
        entities.draw(screen)
        print(hero.speed)
        if current_map == "level3.txt":
            if not sprite.collide_rect(hero,gwall):
                if hero.speed < 11:
                    hero.speed += 0.5
            if not sprite.collide_rect(enemy,gwall):
                if enemy.speed < 11:
                    enemy.speed += 0.5

        # for e in entities:
        #     screen.blit(e.image,(0,0))

init_menu()






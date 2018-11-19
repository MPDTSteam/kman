import pygame
import sys

pygame.font.init()
speed_font = pygame.font.Font(None, 32)
inf_font = pygame.font.SysFont(None, 24, True)
label_font = pygame.font.SysFont(None, 32, True)
class Menu:
    def __init__(self, punkts = [120, 140, u'Punkt', (250, 250, 30), (250, 30, 250)]):
        self.punkts = punkts
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
            screen.blit(pygame.image.load("img/menu.jpeg"), (0,0))
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
                        done = False
                    elif punkt == 2:
                        sys.exit()
            screen.blit(screen, (0, 0))
            pygame.display.flip()



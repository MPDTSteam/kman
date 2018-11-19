import pygame
class Background():
    def __init__(self, screen):
        self.screen = screen
        self.bg_image = pygame.image.load("img/Parallax60.png").convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (1280, 720))
        self.rect_image = self.bg_image.get_rect()
        self.bg_speed    = 0.2
        self.bg_x1 = 0
        self.bg_x2 = -self.rect_image.width

    def update(self):
        self.bg_x1 += self.bg_speed
        self.bg_x2 += self.bg_speed
        if self.bg_x1 >= self.rect_image.width:
            self.bg_x1 = -self.rect_image.width
        if self.bg_x2 >= self.rect_image.width:
            self.bg_x2 = -self.rect_image.width
        self.screen.blit(self.bg_image, (self.bg_x1, 0))
        self.screen.blit(self.bg_image, (self.bg_x2, 0))
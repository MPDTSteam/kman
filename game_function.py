import pygame,sys
from hero import Hero
from officer import Officer
from settings import Settings




def update_screen(hero,enemy, screen, officers, game_settings):
    enemy.blitme()
    hero.blitme()
    officers.draw(screen)
    pygame.display.flip()



def create_officers(screen,game_settings, officers, officer_number, row_number):
    officer = Officer(screen, game_settings)
    officer_width = officer.rect.width
    officer.rect.x = officer_width + 2 * officer_width * officer_number
    officer.rect.y = officer.rect.height + 2*officer.rect.height*row_number
    officers.add(officer)



def get_number_officers_x(game_settings, officer_width):
    available_space_x = game_settings.width - 2 * officer_width
    number_officers_x = int(available_space_x/(officer_width*2))
    return number_officers_x


def create_fleet(screen, game_settings, officers, hero):
    officer = Officer(screen, game_settings)
    officer_width = officer.rect.width
    number_officers_x = get_number_officers_x(game_settings, officer_width)
    number_officers_y = get_number_officers_y(game_settings, hero, officer)
    for row_number in range(number_officers_y):
            for officer_number in range(number_officers_x):
                create_officers(screen, game_settings, officers, officer_number, row_number)

def get_number_officers_y(game_settings,hero, officer):
    available_space_y = game_settings.height - hero.rect.height - officer.rect.height
    number_rows = int(available_space_y/(officer.rect.height*1.2))
    return number_rows



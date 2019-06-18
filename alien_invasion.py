import pygame
from settings import Settings
from ship import Ship
from game_functions import check_events,update_screen
from pygame.sprite import Group

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.height))
    pygame.display.set_caption(game_settings.screen_name)
    bg_color = (game_settings.bg_color)
    ship = Ship(screen,game_settings)
    bullets = Group()

    while True:
        check_events(ship,bullets,screen,game_settings)
        ship.update()
        bullets.update()
        for bullet in bullets:
            if bullet.rect.bottom <= 0 :
                bullets.remove(bullet)
        update_screen(ship,bullets,screen,game_settings)


run_game()

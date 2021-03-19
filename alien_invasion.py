import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a Ship
    ship = Ship(ai_settings, screen)
    # Make group to store bullets in
    bullets = Group()

    # Set the background color
    # bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:
        # Watch for keyboard an mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets_update()
        # print(f' x position: {ship.rect.centerx}')
        gf.update_screen(ai_settings, screen, ship)


run_game()

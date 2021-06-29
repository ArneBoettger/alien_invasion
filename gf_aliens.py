import pygame

import game_functions as gf
from alien import Alien

def _create_fleet(ai_game):
    '''creates alien fleet, calculates number of alien ships per row and number of rows'''
    alien = Alien(ai_game)
    alien_width, alien_height = alien.rect.size
    #number per rows
    available_space_x = ai_game.settings.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x // (2 * alien_width)
    #number of rows
    ship_height = ai_game.ship.rect.height
    available_space_y = (ai_game.settings.screen_height - 3 * alien_height - ship_height)
    number_rows = available_space_y // (2 * alien_height)
    #create ships
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            _create_aliens(ai_game, alien_number, row_number)     

def _create_aliens(ai_game, alien_number, row_number):
    '''creates alien ships'''
    alien = Alien(ai_game)
    alien_width, alien_height = alien.rect.size
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    ai_game.aliens.add(alien)

def _update_aliens(ai_game):
    '''moves alien ships and checks collisions with player ship'''
    _check_fleet_edges(ai_game)
    ai_game.aliens.update()
    #checks for collisions
    if pygame.sprite.spritecollideany(ai_game.ship, ai_game.aliens):
        gf._ship_hit(ai_game)
    _check_aliens_bottom(ai_game)

def _check_fleet_edges(ai_game):
    '''respond if alien ships reach edge'''
    for alien in ai_game.aliens.sprites():
        if alien.check_edges():
            _change_fleet_direction(ai_game)
            break

def _change_fleet_direction(ai_game):
    '''drop alien fleet and change direction'''
    for alien in ai_game.aliens.sprites():
        alien.rect.y += ai_game.settings.fleet_drop_speed
    ai_game.settings.fleet_direction *= -1

def _check_aliens_bottom(ai_game):
    '''checks if aliens reach the bottom of the screen'''
    screen_rect = ai_game.screen.get_rect()
    for alien in ai_game.aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gf._ship_hit(ai_game)
            break
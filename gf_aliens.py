import pygame

from alien import Alien

def _create_fleet(settings, screen, ship, aliens):
    '''creates alien fleet, calculates number of alien ships per row and number of rows'''
    alien = Alien(screen, settings)
    alien_width, alien_height = alien.rect.size
    #number per rows
    available_space_x = settings.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x // (2 * alien_width)
    #number of rows
    ship_height = ship.rect.height
    available_space_y = (settings.screen_height - 3 * alien_height - ship_height)
    number_rows = available_space_y // (2 * alien_height)
    #create ships
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            _create_aliens(screen, settings, aliens, alien_number, row_number)     

def _create_aliens(screen, settings, aliens, alien_number, row_number):
    '''creates alien ships'''
    alien = Alien(screen, settings)
    alien_width, alien_height = alien.rect.size
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)

def _update_aliens(aliens, settings):
    '''moves alien ships'''
    _check_fleet_edges(aliens, settings)
    aliens.update()

def _check_fleet_edges(aliens, settings):
    '''respond if alien ships reach edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            _change_fleet_direction(aliens, settings)
            break

def _change_fleet_direction(aliens, settings):
    '''drop alien fleet and change direction'''
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1
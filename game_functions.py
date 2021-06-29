import sys
import pygame

from bullet import Bullet
from alien import Alien
import gf_aliens

def _check_events(ai_game):
    '''checks for events and runs event functions'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(ai_game, event)
        elif event.type == pygame.KEYUP:
            _check_keyup_events(event, ai_game.ship)

def _check_keydown_events(ai_game, event):
    '''handles keydown-events'''
    if event.key == pygame.K_LEFT:
        ai_game.ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ai_game.ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        _fire_bullet(ai_game)
    elif event.key == pygame.K_q:
        sys.exit()

def _check_keyup_events(event, ship):
    '''handles keyup-events'''
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False

def _update_screen(ai_game):
    '''fills screen, draws ship, bullets and updates screen'''
    ai_game.screen.fill(ai_game.settings.bg_color)
    for bullet in ai_game.bullets.sprites():
        bullet.draw_bullet()
    ai_game.aliens.draw(ai_game.screen)
    ai_game.ship.blitme()
    pygame.display.flip()

def _create_fleet(ai_game):
    '''creates alien fleet, calculates number of alien ships per row and number of rows'''
    gf_aliens._create_fleet(ai_game)  
def _create_aliens(ai_game, alien_number, row_number):
    '''creates alien ships'''
    gf_aliens._create_aliens(ai_game, alien_number, row_number)
def _update_aliens(aliens):
    '''moves alien ships'''
    gf_aliens._update_aliens(aliens)
def _check_fleet_edges(ai_game):
    '''respond if alien ships reach edge'''
    gf_aliens._check_fleet_edges(ai_game)
def _change_fleet_direction(aliens, settings):
    '''drop alien fleet and change direction'''
    gf_aliens._change_fleet_direction(aliens, settings)

def _fire_bullet(ai_game):
    '''creates new and adds to bullets group (if max not yet reached)'''
    if len(ai_game.bullets) < ai_game.settings.bullets_allowed:
        new_bullet = Bullet(ai_game)
        ai_game.bullets.add(new_bullet)

def _update_bullets(bullets):
    '''updates bullet positions and deletes old bullets'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
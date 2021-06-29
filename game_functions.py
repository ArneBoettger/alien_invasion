import sys
import pygame

from bullet import Bullet
from alien import Alien
import gf_aliens

def _check_events(settings, screen, ship, bullets):
    '''checks for events and runs event functions'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            _check_keyup_events(event, ship)

def _check_keydown_events(event, settings, screen, ship, bullets):
    '''handles keydown-events'''
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        _fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def _check_keyup_events(event, ship):
    '''handles keyup-events'''
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False

def _update_screen(settings, screen, ship, bullets, aliens):
    '''fills screen, draws ship, bullets and updates screen'''
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    ship.blitme()
    pygame.display.flip()

def _create_fleet(settings, screen, ship, aliens):
    '''creates alien fleet, calculates number of alien ships per row and number of rows'''
    gf_aliens._create_fleet(settings, screen, ship, aliens)  
def _create_aliens(screen, settings, aliens, alien_number, row_number):
    '''creates alien ships'''
    gf_aliens._create_aliens(screen, settings, aliens, alien_number, row_number)
def _update_aliens(aliens, settings):
    '''moves alien ships'''
    gf_aliens._update_aliens(aliens, settings)

def _fire_bullet(settings, screen, ship, bullets):
    '''creates new and adds to bullets group (if max not yet reached)'''
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def _update_bullets(bullets, aliens):
    '''updates bullet positions, deletes old bullets and checks for hits'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #check for hits
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
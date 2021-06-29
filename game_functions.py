import sys
import pygame

from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    '''checks for events and runs event functions'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''handles keydown-events'''
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    '''handles keyup-events'''
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False

def update_screen(ai_settings, screen, ship, bullets):
    '''fills screen, draws ship, bullets and updates screen'''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()

def fire_bullet(ai_settings, screen, ship, bullets):
    '''creates new and adds to bullets group (if max not yet reached)'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    '''updates bullet positions and deletes old bullets'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
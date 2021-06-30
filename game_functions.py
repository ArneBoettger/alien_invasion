import os.path
import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien
import gf_aliens
from enter_name import EnterNameTextField

def _check_events(ai_game):
    '''checks for events and runs event functions'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(ai_game, event)
        elif event.type == pygame.KEYUP:
            _check_keyup_events(ai_game, event)
        elif (event.type == pygame.MOUSEBUTTONDOWN 
                and not ai_game.stats.game_active):
            mouse_pos = pygame.mouse.get_pos()
            if ai_game.play_button.rect.collidepoint(mouse_pos):
                _start_game(ai_game)

def _check_keydown_events(ai_game, event):
    '''handles keydown-events'''
    if event.key == pygame.K_LEFT:
        ai_game.ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ai_game.ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        if not ai_game.stats.game_active:
             _start_game(ai_game)
        else:
            _fire_bullet(ai_game)
    elif event.key == pygame.K_q:
        sys.exit()

def _check_keyup_events(ai_game, event):
    '''handles keyup-events'''
    if event.key == pygame.K_LEFT:
        ai_game.ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ai_game.ship.moving_right = False

def _read_name(ai_game):
    name = ai_game.enter_name.temp_name
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if "left shift" in name:
                    i = name.index("left shift")
                    name.remove("left shift")
                    name[i] = name[i].upper()
                if "right shift" in name:
                    i = name.index("right shift")
                    name.remove("right shift")
                    name[i] = name[i].upper()
                special_keys = []
                for key in name:
                    if len(key) > 1:
                        special_keys.append(key)
                name = [key for key in name if key not in special_keys]
                _save_high_score(ai_game, "".join(name))
                name.clear()
            name.append(pygame.key.name(event.key))

def _start_game(ai_game):
    '''starts new game and resets everything'''
    ai_game.stats.reset_stats()
    ai_game.stats.game_active = True
    #prepare scoreboard, level, ships
    ai_game.sb.prep_score()
    ai_game.sb.prep_level()
    ai_game.sb.prep_ships()
    '''prepare playfield'''
    ai_game.aliens.empty()
    ai_game.bullets.empty()
    _create_fleet(ai_game)
    ai_game.ship.center_ship()
    #re-initializes level 1 settings
    ai_game.settings.initialize_dynamic_settings()
    #sets mouse invisible
    pygame.mouse.set_visible(False)

def _update_screen(ai_game):
    '''fills screen, draws ship, bullets and updates screen'''
    ai_game.screen.fill(ai_game.settings.bg_color)
    for bullet in ai_game.bullets.sprites():
        bullet.draw_bullet()
    ai_game.aliens.draw(ai_game.screen)
    ai_game.sb.show_score()
    ai_game.ship.blitme()
    #draw play-button if game is inactive, enter-name if new highscore
    if not ai_game.stats.game_active:
        if ai_game.enter_name_flag:
            ai_game.enter_name.draw_textfield(ai_game)
        else:
            ai_game.play_button.draw_button()
    pygame.display.flip()

def _create_fleet(ai_game):
    '''creates alien fleet, calculates number of alien ships per row and number of rows'''
    gf_aliens._create_fleet(ai_game)  
def _create_aliens(ai_game, alien_number, row_number):
    '''creates alien ships'''
    gf_aliens._create_aliens(ai_game, alien_number, row_number)
def _update_aliens(ai_game):
    '''moves alien ships'''
    gf_aliens._update_aliens(ai_game)

def _fire_bullet(ai_game):
    '''creates new and adds to bullets group (if max not yet reached)'''
    if len(ai_game.bullets) < ai_game.settings.bullets_allowed:
        new_bullet = Bullet(ai_game)
        ai_game.bullets.add(new_bullet)
        #loose points for every shot
        ai_game.stats.score -= 10
        ai_game.sb.prep_score()

def _update_bullets(ai_game):
    '''updates bullet positions, deletes old bullets and checks for hits'''
    ai_game.bullets.update()
    for bullet in ai_game.bullets.copy():
        if bullet.rect.bottom <= 0:
            ai_game.bullets.remove(bullet)  
    _check_bullet_alien_collision(ai_game)

def _check_bullet_alien_collision(ai_game):
    '''checks for hits'''
    collisions = pygame.sprite.groupcollide(ai_game.bullets, ai_game.aliens, True, True)
    #receive points for hitting aliens
    if collisions:
        for aliens in collisions.values():
            ai_game.stats.score += ai_game.settings.alien_points * len(aliens)
            ai_game.sb.prep_score()
            ai_game.sb.check_high_score()
    #if no more alien ships: creates new fleet and deletes remaining bullets, level-up
    if not ai_game.aliens:
        ai_game.bullets.empty()
        _create_fleet(ai_game)
        ai_game.settings.increase_speed()
        ai_game.stats.level += 1
        ai_game.sb.prep_level()

def _ship_hit(ai_game):
    '''responds to ship being hit, reduce number of ships left, clear playfield'''
    if ai_game.stats.ships_left > 1:
        ai_game.stats.ships_left -= 1
        ai_game.sb.prep_ships()
        ai_game.aliens.empty()
        ai_game.bullets.empty()
        _create_fleet(ai_game)
        ai_game.ship.center_ship()
        #stop the game for 0.5s
        sleep(0.5)
    else:
        ai_game.stats.game_active = False
        #set mouse visible
        pygame.mouse.set_visible(True)
        if _check_if_highscore(ai_game):
            ai_game.enter_name_flag = True
            msg = "New Highscore: " + str(ai_game.stats.score)
            ai_game.enter_name = EnterNameTextField(ai_game, msg)
            
def _check_if_highscore(ai_game):
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", encoding="utf-8") as hs:
            for line in hs:
                return int(line.split(":")[1]) < ai_game.stats.score
    return True

def _save_high_score(ai_game, name):
    with open("high_score.txt", "w", encoding="utf-8") as hs:
        hs.write(name + ":" + str(ai_game.stats.score))
    ai_game.enter_name_flag = False
    ai_game.stats.reset_stats()
""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

game_functions.py负责让游戏顺利运行的函数
"""

import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
    响应按键
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """
    如果子弹没有达到数目限制，则发射子弹
    """
    # 创建一颗子弹并将其加入编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """
    响应松开
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """
    响应按键和鼠标事件
    """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # 检测是否有按键输入
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
            # 检测是否松开按键
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """
    更新屏幕上的图像，并切换到新的屏幕
    """
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕对象可见
    # 在玩家移动游戏元素时，下面的函数将不断更新屏幕，以显示新元素的位置
    pygame.display.flip()

def update_bullets(bullets):
    """
    更新子弹的位置，并且删除已经消失的子弹
    """
    # 更新子弹的位置
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy(): # 创立副本，在副本中检查子弹的位置，如果超出屏幕，则在列表中删除
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """
    创建外星人群
    """
    # 创建一个外星人，并且计算一行可以容纳多少外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    """
    计算每行可以容纳多少外星人
    """
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(avaliable_space_x / (2 * alien_width))
    return number_alien_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """
    创建外星人并将其放在当前行
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width 
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """
    计算屏幕可以容纳多少行外星人
    """
    avaliable_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows



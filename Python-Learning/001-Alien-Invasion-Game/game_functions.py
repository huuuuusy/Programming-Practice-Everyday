""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

game_functions.py负责让游戏顺利运行的函数
"""

import sys
import pygame
from bullet import Bullet

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

def update_screen(ai_settings, screen, ship, bullets):
    """
    更新屏幕上的图像，并切换到新的屏幕
    """
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
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


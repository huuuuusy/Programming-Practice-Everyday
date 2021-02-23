""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
      pygame == 1.9.6
介绍： game_functions.py负责让游戏顺利运行的函数
"""

import sys
import pygame
from time import sleep
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

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
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

            # 检测是否点击play按钮
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """
    在玩家点击Play时开始游戏
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    # 如果鼠标点击范围在button内，则游戏开始
    if button_clicked and not stats.game_active:
        # 重置游戏
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人
        # 让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
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

    # 显示得分
    sb.show_score()

    # 如果处于非活动状态，则绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕对象可见
    # 在玩家移动游戏元素时，下面的函数将不断更新屏幕，以显示新元素的位置
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    更新子弹的位置，并且删除已经消失的子弹
    """
    # 更新子弹的位置
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy(): # 创立副本，在副本中检查子弹的位置，如果超出屏幕，则在列表中删除
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中外星人
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    响应子弹和外星人的碰撞
    """
    # 如果击中则删除相应的子弹和外星人
    # 函数遍历所有外星人和子弹，如果两种元素的rect重叠，则在返回的字典里添加键－值对
    # 第一个True表示删除子弹，第二个True表示删除外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 删除现有的子弹并且新建一群外星人，加快游戏节奏
        bullets.empty()
        ai_settings.increase_speed()

        # 提升等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

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

def check_fleet_edges(ai_settings, aliens):
    """
    有外星人撞到屏幕边缘时采取相应措施
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
    
def change_fleet_direction(ai_settings, aliens):
    """
    将整群外星人下移并改变方向
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    响应外星人撞击飞船
    """
    if stats.ships_left > 0:
        # 将ships_left减去1
        stats.ships_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    检查外星人是否到达屏幕底端
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞一样处理
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break 

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    检查是否有外星人位于屏幕边缘，更新外星人群中所有外星人的位置
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    """
    检查是否诞生最高分
    """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


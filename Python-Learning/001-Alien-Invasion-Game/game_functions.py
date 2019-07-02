""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

game_functions.py负责让游戏顺利运行的函数
"""

import sys
import pygame

def check_events(ship):
    """
    响应按键和鼠标事件
    """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # 检测是否有按键输入
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
            # 检测是否松开按键
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """
    更新屏幕上的图像，并切换到新的屏幕
    """
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
            
    # 让最近绘制的屏幕对象可见
    # 在玩家移动游戏元素时，下面的函数将不断更新屏幕，以显示新元素的位置
    pygame.display.flip()
""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

alien_invasion.py负责执行关于游戏的主要功能
运行本文件即可进行游戏

注意：在pygame中原点位于左上角，向右下方移动时，坐标值将增大
"""

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf 

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏主循环
    while True:
        # 检测事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船状态
        ship.update()
        # 更新子弹状态
        gf.update_bullets(bullets)
        # 绘制新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)

# 初始化游戏
run_game()

""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

alien_invasion.py负责执行关于游戏的主要功能
"""

import sys
import pygame
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
    ship = Ship(screen)

    # 开始游戏主循环
    while True:
        # 检测事件
        gf.check_events(ship)
        # 更新飞船的状态
        ship.update()
        # 在屏幕上绘制更新后的飞船
        gf.update_screen(ai_settings, screen, ship)

# 初始化游戏
run_game()

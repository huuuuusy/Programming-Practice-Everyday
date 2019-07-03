""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
      pygame == 1.9.6
介绍： settings.py负责存储游戏的设置
"""

class Settings():
    """
    存储Alien Invasion所有设置的类
    """

    def __init__(self):
        """
        初始化游戏设置
        """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        # fleet_drop_speed表示撞到屏幕边缘后向下移动的速度
        self.fleet_drop_speed = 100
        # fleet_direction=1表示撞到屏幕边缘后向右，-1表示向左
        self.fleet_direction = 1
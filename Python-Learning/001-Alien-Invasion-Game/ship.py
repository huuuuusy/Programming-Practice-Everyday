""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

ship.py负责管理飞船的大部分行为
"""

import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """
        初始化飞船并设置初始位置
        """
        # screen指定绘制飞船的位置
        self.screen = screen
        # ai_settings指定有关游戏的设置
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        # 下载飞船图像，并将其作为一个surface存入self.image中
        self.image = pygame.image.load('images/ship.png')
        # 获取surface的属性rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船属性center中存储小数值
        # 因为rect.centerx只能存储整数值，所以新建一个center属性用于存放中心位置的小数值
        # 飞船移动时对center进行更新，最后用center更新rect.centerx
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """
        根据移动标志调整飞船位置
        """
        # 更新飞船center，而非rect.centerx
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        # 使用if而非elif，以确保向左和向右具有相同的优先级
        # 使用elif则同时按下向左和向右后，飞船仍会向右移动
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """
        在指定位置绘制飞船
        """
        # 对于surface类的实例self.screen, blit完成在自身画图的动作
        # blit需要两个参数：要画图的图片，和具体绘图的位置
        # self.image是将要绘制的图片,即飞船
        # self.rect是具体位置，即屏幕下方居中
        self.screen.blit(self.image, self.rect)

# Alien Invasion Game

《Python编程从入门到实践》项目，利用Pygame开发一款游戏。

游戏通过键盘方向键左右移动飞船，通过空格键发射子弹攻击外星人。

屏幕右上方会显示当前得分和等级；屏幕中央显示最高分；屏幕左边显示剩余的飞船数目，当飞船数目为0时游戏结束。

![](images/start.png)


## 说明

### 1.1 安装Pygame

以Ubuntu18.04 + Anaconda3环境为例：

    conda list
    conda install pip
    pip install pygame

然后打开python，验证：

    import pygame

如果没有错误，说明安装正确。

### 1.2 运行

直接运行alien_invasion.py文件即可。

    python alien_invasion.py

## 开发环境

系统： Ubuntu 18.04

IDE:  VS Code 1.35.1

工具： python == 3.7.3, pygame == 1.9.6
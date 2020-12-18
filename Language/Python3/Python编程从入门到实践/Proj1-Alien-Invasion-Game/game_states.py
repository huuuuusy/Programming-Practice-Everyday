""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
      pygame == 1.9.6
介绍： game_states.py负责跟踪游戏统计信息
"""

class GameStates():
    """
    跟踪游戏统计信息
    """

    def __init__(self, ai_settings):
        """
        初始化统计信息
        """
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏启动时处于非活动状态
        self.game_active = False

        # 在任何情况下均不重置最高分
        self.high_score = 0
    
    def reset_stats(self):
        """
        初始化在游戏运行期间可能变化的信息
        """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

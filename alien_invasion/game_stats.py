class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
    #游戏启动时处于非活跃状态
        self.game_active = False

    #在任何时候都不应重置最高分
        self.high_score = 0


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        # 设置游戏初始分数
        self.score = 0
        self.level = 1

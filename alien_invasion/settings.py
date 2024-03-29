import pygame

class Settings():
    """存储外星人的游戏设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 900#设置游戏屏幕宽度
        self.screen_height = 506#设置游戏高度
        self.bg_color = (0,137,108)#纯色背景的颜色

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 5


        #外星人设置
        self.fleet_drop_speed = 10.5
        self.alien_points = 50

        #飞船设置
        self.ship_limit = 3


        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #外星人分数提高的速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 2
        self.fleet_direction = 1


    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

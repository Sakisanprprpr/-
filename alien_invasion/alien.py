import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
    #初始化外星人并设置外星人初始位置
    def __init__(self,ai_setting,screen):#初始化Alien类。
        super().__init__()#初始化父类Sprite。
        self.screen = screen
        self.ai_setting = ai_setting

        #加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/timg1.png')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)


    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """如果外星人触碰到了边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右移动外星人"""
        self.x += (self.ai_setting.alien_speed_factor *
                   self.ai_setting.fleet_direction)
        self.rect.x = self.x


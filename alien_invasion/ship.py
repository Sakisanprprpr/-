import pygame
from pygame.sprite import Sprite
class Ship(Sprite):#创建一个飞船的类，包含飞船的所有属性

    def __init__(self,screen,ai_settings):#添加两个形参
        """初始化飞船并设置初始位置"""
        super().__init__()
        self.screen = screen#初始化两个形参
        self.ai_settings = ai_settings

        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images\ship.png')#读取飞船的模型文件
        self.rect = self.image.get_rect()#读取飞船模型的矩形数据
        self.screen_rect = screen.get_rect()#读取游戏窗口的矩形数据

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx#将飞船自身的中心坐标设置成与屏幕中心相同
        self.rect.bottom = self.screen_rect.bottom#将飞船自身的下边缘坐标与屏幕下边缘对齐

        #移动标志
        self.moving_right = False#设置一个向右行的标志，默认为False
        self.moving_left = False#设置一个向左行的标志，默认为False
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        """"在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)#在指定的位置绘制飞船

    def update(self):#创建一个update函数，用于设置飞船
        if self.moving_right and self.rect.right < self.screen_rect.right:#
            #如果标志为True并且飞船矩形的右值小于屏幕的右值（意思是并未到达屏幕的最右边
            self.rect.centerx += self.ai_settings.ship_speed_factor
            #那么飞船的中心位置向右移动，数值为settings中的speed_factor

        if self.moving_left and self.rect.left > 0:
            #如果标志为True并且飞船矩形最左边大于0（意思是飞船未达到屏幕最左边，因为最左的坐标是0
            self.rect.centerx -= self.ai_settings.ship_speed_factor
            #那么飞船的中心位置向左边移动speed_factor

        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor




    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom




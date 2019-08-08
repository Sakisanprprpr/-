from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    """对飞船的子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()


        #在0，0处创建一个表示子弹的矩形，再设置正确的位置
        self.image = pygame.image.load(r"images\bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #用小数表示子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self,screen):
        """在屏幕上绘制子弹"""
        screen.blit(self.image,self.rect)




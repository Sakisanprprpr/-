import pygame
import sys
import music
class Ship():
    def __init__(self,screen,):
        self.screen = screen


        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):



        if self.rect.left > 0:

            self.rect.centerx -= 2


        if self.rect.top > 0:
            self.rect.centery -= 2

        if self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 2
    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx



def run():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    color = (230,230,230)
    pygame.display.set_caption("飞船测试")
    ship = Ship(screen)


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # 如果触发的按键是K_RIGHT(也就是右键
                    ship.rect.centerx += 20  # 那么将飞船右行的标志改为True

                elif event.key == pygame.K_LEFT:  # 如果触发的按键是K_LEFT(也就是左键
                    ship.rect.centerx -= 2  # 那么将飞船左行的标志改为True
                    ship.center_ship()
                elif event.key == pygame.K_UP:
                    ship.rect.centery -= 2

                elif event.key == pygame.K_DOWN:
                    ship.rect.centerx += 2

        screen.fill(color)
        ship.blitme()
        pygame.display.flip()


run()



import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats



def run_game():
    """初始化游戏并且创建一个屏幕对象"""
    pygame.init()#初始化游戏并且创建一个屏幕对象
    ai_settings = Settings()#调取模块Settings()，将游戏设置添加进来
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height) )#这里创建一个名为screen的游戏窗口，将实参
                                                         #传递给pygame.display.set_mode()
    pygame.display.set_caption("射击小游戏.saki")#设置游戏名字

    ship = Ship(screen,ai_settings)#调取Ship模块，添加实参screen和ai_sittings
    bullets = Group()#调用sprite中group编组，用于存储所有有效的子弹，以方便管理
    aliens = Group()#再用Sprite类创建一个外星人编组
    gf.create_fleet(ai_settings,screen,ship,aliens)
    stats = GameStats(ai_settings)#创建一个存储游戏统计信息的实例


    while 1:#开始游戏的主循环
        gf.check_events(ship,ai_settings,screen,bullets)#调用模块gf中的check_event函数，用于监视鼠标和键盘事件
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,aliens,ship,stats,screen,bullets)
        gf.update_screen(ai_settings,ship,screen,bullets,aliens)#调用模块gf中的update_screen函数，用于屏幕更新






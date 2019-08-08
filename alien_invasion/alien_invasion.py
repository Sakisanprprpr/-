# -*- coding:utf-8 -*-

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import music




def run_game():
    """初始化游戏并且创建一个屏幕对象"""
    pygame.init()#初始化游戏并且创建一个屏幕对象
    ai_settings = Settings()#调取模块Settings()，将游戏设置添加进来
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))#这里创建一个名为screen的游戏窗口，将实参
                                                         #传递给pygame.display.set_mode()
    pygame.display.set_caption("射击小游戏.saki")#设置游戏名字
    play_button = Button(ai_settings,screen,"Play")
    ship = Ship(screen,ai_settings)#调取Ship模块，添加实参screen和ai_sittings
    bullets = Group()#调用sprite中group编组，用于存储所有有效的子弹，以方便管理
    aliens = Group()#再用Sprite类创建一个外星人编组
    gf.create_fleet(ai_settings,screen,ship,aliens)
    stats = GameStats(ai_settings)#创建一个存储游戏统计信息的实例
    sb = Scoreboard(ai_settings,screen,stats)
    pygame.mixer.init()
    music.start_stop()

    while 1:#开始游戏的主循环
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb)#侦听键鼠活动
        if stats.game_active:#设置一个标志
            ship.update()#设置飞船的移动属性，使其可以操控
            #更新子弹的位置，并且删除消失的子弹，并且检查子弹是否击中了外星人，如果是将执行相应操作
            gf.update_bullets(ai_settings, screen, ship,aliens, bullets,stats,sb)
            #检查外星人是否被击中或者到达屏幕低端或者与飞船发生碰撞，并且执行相应操作
            gf.update_aliens(ai_settings,ship,screen,bullets,aliens,stats,sb)

        #将所有元素绘制到屏幕上
        gf.update_screen(ai_settings,ship,screen,bullets,aliens,stats,play_button,sb)  # 调用模块gf中的update_screen函数，用于屏幕更新


run_game()




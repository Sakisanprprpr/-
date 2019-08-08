import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard():

    """显示得分的类"""
    def __init__(self,ai_settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats


        #设置显示得分信息时使用的字体
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,36)

        #准备初始化得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        rouded_score = int(round(self.stats.score,-1))
        score_str = "Now:" + "{:,}".format(rouded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,(45,98,142))

        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def prep_high_score(self):
        """将最高分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "Max:" + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,(191,182,141))

        #将最高得分放在当前得分的上面
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ship.draw(self.screen)


    def prep_level(self):
        """将等级转换为图像"""
        self.level_image = self.font.render("Level:" + str(self.stats.level),True,
                                            self.text_color,(45,98,142))
        #将等级放在得分下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 5

    def prep_ships(self):
        """显示还剩多少艘飞船"""
        self.ship = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen,self.ai_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ship.add(ship)
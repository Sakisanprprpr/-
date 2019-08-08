import sys#调用sys用来退出游戏
import pygame#调用模块pygame
from bullet import Bullet
from alien import Alien
from time import sleep
import json
import music

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb):
    """响应按键和鼠标事件"""
    # 监视键盘和鼠标事件
    for event in pygame.event.get():  # 侦听事件，根据发生的事件执行相应的任务
        if event.type == pygame.QUIT:  # 如果点击了关闭窗口的按钮，将触发QUIT
            sys.exit()  # 将会调用sys.exit()来退出游戏
        elif event.type == pygame.KEYDOWN:#如果触发了按键keydown事件
            check_keydown_events(event,ai_settings,screen,ship,bullets,aliens,stats)#执行函数check_keydown_events()

        elif event.type == pygame.KEYUP:#如果触发了松开按键keyup事件
           check_keyup_events(event,ship)#执行函数check_keyup_events()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_buttom(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y,sb)

def check_play_buttom(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y,sb):
    """在玩家点击play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()

        #隐藏光标
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        #重置记分牌图像
        sb.prep_score()
        sb.prep_level()
        sb.prep_ships()
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def check_keydown_events(event,ai_settings,screen,ship,bullets,aliens,stats):#建立一个触发按键的函数
    if event.key == pygame.K_RIGHT:#如果触发的按键是K_RIGHT(也就是右键
        ship.moving_right = True#那么将飞船右行的标志改为True
    elif event.key == pygame.K_LEFT:#如果触发的按键是K_LEFT(也就是左键
        ship.moving_left = True#那么将飞船左行的标志改为True

    elif event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_u:
        ship.center_ship()
    elif event.key == pygame.K_p and not  stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        ai_settings.initialize_dynamic_settings()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()





def check_keyup_events(event,ship):#建立一个触发按键松开的函数
    if event.key == pygame.K_RIGHT:#如果触发松开的按键是K_RIGHT
        ship.moving_right = False#那么将飞船向右的标志改为False，也就是停止移动
    elif event.key == pygame.K_LEFT:#如果触发松开的按键是K_LEFT
        ship.moving_left = False#那么将飞船向左的标志改为False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
def update_screen(ai_settings,ship,screen,bullets,aliens,stats,play_button,sb):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    background = pygame.image.load(
        r'images\beijing-min.png').convert()#读取timg.jpg图片，存储到新变量中

    screen.blit(background, (0, 0))  # 将图片设置为背景，坐标0，0(最左上角)

    for bullet in bullets.sprites():
        bullet.draw_bullet(screen)
    aliens.draw(screen)
    ship.blitme()

    if not stats.game_active:
        play_button.draw_button()

    try:
        load_high_score(stats)
    except FileNotFoundError:
        save_high_socre(stats)
    sb.prep_high_score()
    sb.show_score()
    pygame.display.flip()#让最近绘制的屏幕可见,在While循环中从而不断更新屏幕，产生平滑的效果



def fire_bullet(ai_settings,screen,ship,bullets):
    """设置开火的规则,同屏只允许存在bullet_allowed(设置为5)发子弹"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可容纳多少个外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)



    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #创建一个外星人并将其加入到当前行
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def update_aliens(ai_settings,ship,screen,bullets,aliens,stats,sb):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #检测外星人与飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)

    #检查是否有外星人到达屏幕低端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """相应被外星人撞到的飞船"""
    #将ship_left减1
    if stats.ships_left > 0:
        stats.ships_left -= 1

    #更新飞船剩余数量
        sb.prep_ships()
    #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()


    #创建一群新的外星人，并将飞船放到屏幕低端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()


    #暂停
        sleep(0.5)
    else:
        # 更新飞船剩余数量

        stats.ships_left = 3
        sb.prep_ships()
        stats.score = 0
        sb.prep_score()
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_fleet_edges(ai_settings,aliens):
    """有外星人到达边缘时采取的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_bullets_aliens_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb):
    #检查是否有子弹击中了外星人
    #如果是这样，就删除相应的子弹和外星人
    #如果整群外星人被消灭，等级将提高1
    collisins = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisins:
        for aliens in collisins.values():
            stats.score += ai_settings.alien_points*len(aliens)
            sb.prep_score()

        check_high_score(stats,sb)
        save_high_socre(stats)

    if len(aliens) == 0:#检查外星人编组的数量是否为零
        #删除现有的子弹并且再创建一群外星人
        ai_settings.increase_speed()
        #提高一个等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)




def update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb):
    #更新子弹的位置，并且删除已经消失的子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullets_aliens_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb)



def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞到一样处理，重置飞船和外星人，并且减去一个飞船限制
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
            break

def check_high_score(stats,sb):
    """检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def save_high_socre(stats):
    file_name = "high.json"
    with open(file_name,"w") as value:
        json.dump(stats.high_score,value)


def load_high_score(stats):
    file_name = "high.json"
    with open(file_name) as key:
        stats.high_score = json.load(key)



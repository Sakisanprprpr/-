import pygame

def start_stop():
    file_name = ("images\start.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(-1)
import pygame
import os


PATH = os.path.dirname(__file__) + os.sep 

# Размер окна
WIN_WIDTH = 1200
WIN_HEIGHT = 768

FPS = 60

#Состояние игры
GAME_STATE = True

WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)

clock = pygame.time.Clock()

while GAME_STATE:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            GAME_STATE = False

    clock.tick(FPS)
    pygame.display.update()
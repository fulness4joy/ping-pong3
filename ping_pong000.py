import pygame
import os


PATH = os.path.dirname(__file__) + os.sep 

# Размер окна
WIN_WIDTH = 1200
WIN_HEIGHT = 768

FPS = 60

#Состояние игры
GAME_STATE = True

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, width, height, x, y, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.y = y
        self.rect.x = x

    def show(self):
        WINDOW.blit(self.image, (self.rect))

class Player(GameSprite):

    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] == True:
            self.rect.y -= 10
        if keys[pygame.K_DOWN] == True:
            self.rect.y += 10
        

WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)

clock = pygame.time.Clock()

rocket1 = Player(PATH + 'racket.png', 39, 136, 50, WIN_HEIGHT/2-68, 10)

while GAME_STATE:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            GAME_STATE = False

    WINDOW.fill((200, 200, 0))

    rocket1.move()
    rocket1.show()

    clock.tick(FPS)
    pygame.display.update()

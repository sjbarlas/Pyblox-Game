import math
import pygame

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Pyblox Game')
pygame.mouse.set_visible(0)
font = pygame.font.Font(None, 36)
background = pygame.Surface(screen.get_size())

c1 = (255, 255, 255)
c2 = (0, 0, 0)
c3 = (0, 0, 255)

b_width = 30
b_height = 30

class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super() .__init__()
        self.image = pygame.Surface([b_width, b_height])
        self.image.fill(color)
        self.rect = self.image.get_Rect()
        self.rect.x = x
        self.rect.y = y

class Ball(pygame.sprite.Sprite):
    speed = 10.0
    x = 0.0
    y = 180.0
    dire = 200
    w = 10
    h = 10

    def __intit__(self):
        super().__init__()
        self.image = pygame.Surface([self.w, self.h])
        self.image.fill(c1)
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

    def bouncer(self, diff):
        self.dire = (180 - self.dire) % 360
        self.dire -= diff

    def update(self):
        direction_radians = math.radians(self.direction)
         
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
         
        self.rect.x = self.x
        self.rect.y = self.y
         
        if self.y <= 0:
            self.bounce(0)
            self.y = 1
             
        if self.x <= 0:
            self.dire = (360 - self.dire) % 360
            self.x = 1
             
        if self.x > self.screenwidth - self.w:
            self.dire = (360 - self.direction) % 360
            self.x = self.screenwidth - self.w - 1
         
        if self.y > 600:
            return True
        else:
            return False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
         
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((white))
         
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

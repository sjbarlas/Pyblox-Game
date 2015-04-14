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

block_width = 30
block_height = 30

class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super() .__init__()
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
        self.rect = self.image.get_Rect()
        self.rect.x = x
        self.rect.y = y

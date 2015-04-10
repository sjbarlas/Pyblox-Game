# kuch likhna hai yahan

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((500, 500))
pygame.display.set_caption('GAME!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()

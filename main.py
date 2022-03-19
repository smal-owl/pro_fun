import pygame
import random
import obj
from obj import *
import settings
from pygame.sprite import Group
##------settengs----------
W, H = settings.W, settings.H
size = settings.size
fps = settings.FPS
hp = settings.hp
cannon_count = settings.cannon_count
##------pydame------------
pygame.init()
screen = pygame.display.set_mode((W, H))

all_objs = pygame.sprite.Group()

player = Cannon(cannon_count, (W/2, H-50), all_objs)

sprites_group = pygame.sprite.Group()
solids_objs = pygame.sprite.Group()



run = True
clock = pygame.time.Clock()

while run:
    circ = random.randint(0, 100)
    if circ > 98:
        Bomb(all_objs)
    screen.fill((255, 255, 255))
    m_pos = pygame.mouse.get_pos()
    hp_blit(screen)

    events = [event for event in pygame.event.get()]
    all_objs.draw(screen)



    for event in events:
        if event.type == pygame.QUIT:
            run = False
        all_objs.update(event)

    pygame.display.flip()
    clock.tick(60)


##screen.blit(bg_surf, (0, 0))
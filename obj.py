import settings
import pygame
import random
from pygame import transform

##------settengs----------
W, H = settings.W, settings.H
size = settings.size
fps = settings.FPS
hp = settings.hp
hp_0 = settings.hp


def hp_blit(screen):
    step = 20
    pygame.draw.rect(screen, (64, 128, 200),
                     (W - 2 * step, step, step, step * 5), 2)
    pygame.draw.rect(screen, (64, 128, 255),
                     (W - 2 * step, step + hp_0 - hp, step, hp))


def death():
    pass


def damag(b):
    global hp
    hp = hp - int(b / 10)
    if hp <= 0:
        death()


class Cannon(pygame.sprite.Sprite):
    def __init__(self, can_count, coords, *group):
        """Аргументы: coords - коордтнаты на поле"""
        super().__init__(*group)
        self.image = pygame.image.load("textures/cannon.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.coords = coords
        print(coords)
        self.rect.x, self.rect.y = coords
        self.rect.y = self.rect.y - 100
        self.speed = 50




def update(self, events, m_pos, keys,
           *args):
    """задел на будущее"""
    if keys[pygame.K_LEFT]:
        self.rect = self.rect.move(-self.speed, 0)

    if keys[pygame.K_RIGHT]:
        self.rect = self.rect.move(self.speed, 0)
    if keys[pygame.K_UP]:
        self.rect = self.rect.move(0, -self.speed)
    if keys[pygame.K_DOWN]:
        self.rect = self.rect.move(0, self.speed)


class Bomb(pygame.sprite.Sprite):
    image = pygame.image.load("textures/bomb.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.hp = random.randint(0, 100)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W-200)
        self.rect.y = random.randrange(40)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.image.load("textures/explo.jpg")
            self.image = pygame.transform.scale(self.image, (70, 70))
            clock = pygame.time.Clock
            self.hp = self.hp - 10
            if self.hp < 30:
                self.kill()
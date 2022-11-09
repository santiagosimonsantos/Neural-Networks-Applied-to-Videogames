import pygame
from pygame.locals import *
import sys
from random import randint

pygame.init()

vec = pygame.math.Vector2
HEIGHT = 450
WIDTH = 600
ACC = 2
FRIC = -0.12
FPS = 60
FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255,255,40))
        self.rect = self.surf.get_rect()
        self.pos = vec((75, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.rect.midbottom = self.pos

    def move(self):
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.acc.y = -ACC
        else:
            self.acc.y = ACC/5
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        self.rect.midbottom = self.pos

class plataform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.surf = pygame.Surface((50, HEIGHT))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        self.pos = pos
        self.rect.midbottom = self.pos
    def scroll(self, player, rand):
        self.pos.x -= 1
        if self.pos.x < 0:
            self.pos.x = WIDTH
            self.pos.y = rand
        #if plataform touches player, player dies
        # if self.rect.colliderect(player):
        #     pygame.quit()
        #     sys.exit()
        self.rect.midbottom = self.pos

class obstacle(pygame.sprite.Group):
    def __init__():
        super().__init__()
        self.plataforms1 = plataform(vec(WIDTH, randint(0, HEIGHT)))
            -
    def scroll(self, player, rand):
        self.pos.x -= 1
        if self.pos.x < 0:
            self.pos.x = WIDTH
            self.pos.y = rand
        self.plataforms1.rect.midbottom = self.pos
        self.pos.y += HEIGHT + 150
        self.plataforms2.rect.midbottom = self.pos + HEIGHT + 150

        #if plataform touches player, player dies
        # if self.rect.colliderect(player):
        #     pygame.quit()
        #     sys.exit()


posicion = randint(25, HEIGHT-25)
PT1 = plataform(vec((600, 25)))
PT2 = plataform(vec((600, 25)))
obstacle = obstacle([PT1, PT2], vec((600, 25)))

posicion = randint(25, HEIGHT-25)
PT3 = obstacle(vec((900, posicion)))
PT4 = obstacle(vec((900, posicion + 150 + HEIGHT)))
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(PT1)
all_sprites.add(PT2)
all_sprites.add(PT3)
all_sprites.add(PT4)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((0,0,0))
    P1.move()
    #generate random the number of 1 or -1
    posicion = randint(25, HEIGHT-25)
    PT1.scroll(P1,posicion)
    PT2.scroll(P1,posicion + 150 + HEIGHT)
    PT3.scroll(P1,posicion)
    PT4.scroll(P1,posicion + 150 + HEIGHT)

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
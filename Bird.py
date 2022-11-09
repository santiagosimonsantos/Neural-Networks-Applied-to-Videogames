import pygame
from pygame.locals import *
import  sys

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        self.pos = vec((75, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.acc.y = -ACC*1.5
        else:
            self.acc.y = ACC/8
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        self.rect.midbottom = self.pos
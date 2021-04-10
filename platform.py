
import pygame, random
from constants import *
import player
import random

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.width = 300
        self.height = 32
        self.speed = 2
        self.image = pygame.image.load("log.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)



    def move_left(self):
        self.rect = self.rect.move(self.speed, 0)

    def move_right(self):
        self.rect = self.rect.move(-self.speed, 0)

    # def update(self, player_group):
    #     player = pygame.sprite.spritecollide(self, player_group, False)
    #
    #     if player:
    #         if player[0].rect.left >= 500:
    #             self.rect = self.rect.move(self.speed, 0)
    #
    #         if player[0].rect.right >= 400:
    #             self.rect = self.rect.move(-self.speed, 0)

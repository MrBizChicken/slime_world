
import pygame, random
from constants import *
import player
import random


class Lava(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT - 28
        self.width = 1000
        self.height = 55
        self.speed = 5
        self.image = pygame.image.load("lava.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

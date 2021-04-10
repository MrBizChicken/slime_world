import pygame, random
from constants import *
import random
from pygame import mixer


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 64
        self.height = 64
        self.speed = 5
        self.x = GAME_WIDTH // 2 - self.width * 2
        self.y = 0
        self.lift = -3
        self.image = pygame.image.load("blob.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.grav = 0.3
        self.vel = 0
        self.max_vel = 8
        self.falling = True
        self.can_jump = True
        self.coin_score = 0



    def update(self, all_group, platform_group, lava_group, spike_platform_group):
        print(self.vel)
        if self.vel > self.max_vel:
            self.vel = self.max_vel

        self.rect.y += self.vel



        if self.vel < self.max_vel:
            self.can_jump = False



        self.key_input(all_group)
        self.collide(platform_group, lava_group, spike_platform_group)
        self.gravity()


    def gravity(self):
        if self.falling == True:


            self.vel += self.grav




    def collide(self, platform_group, lava_group, spike_platform_group):

        platforms = pygame.sprite.spritecollide(self, platform_group, False)

        if platforms:
            self.image = pygame.image.load("blob.png")
            if self.rect.bottom < platforms[0].rect.bottom:

                self.rect.bottom = platforms[0].rect.top
                self.vel = 0
                self.can_jump = True

        lava = pygame.sprite.spritecollide(self, lava_group, False)

        if lava:

            if self.rect.top < lava[0].rect.top:

                self.rect.bottom = 0



        if pygame.sprite.spritecollide(self, spike_platform_group, False):
            self.rect.bottom = 0












    def jump(self):


        if self.can_jump:
            self.vel += self.lift








    def key_input(self, all_group):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.image = pygame.image.load("blob.png")
            if self.rect.x > 400:
                self.rect.x += -self.speed
            else:
                for p in all_group:
                    p.move_left()


        if keys[pygame.K_RIGHT]:
            self.image = pygame.image.load("blob.png")
            if self.rect.left < 500:
                self.rect.x += self.speed
            else:
                for p in all_group:
                    p.move_right()

        if keys[pygame.K_SPACE]:
            self.jump()
            self.image = pygame.image.load("blob_jump.png")

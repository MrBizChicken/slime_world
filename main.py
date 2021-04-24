from constants import *
import pygame, random
import player
import platform
import spike_platform
import lava
pygame.init()
from pygame import mixer
mixer.init()

# states 0 menu, 1 running, 2 pause, 3 death
states= 0





pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
background_image = pygame.image.load("assests/images/slime_background.png").convert()

pygame.init()

platform_group = pygame.sprite.Group()
spike_platform_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()



all_group = pygame.sprite.Group()





player = player.Player()
lava = lava.Lava()



player_group.add(player)
lava_group.add(lava)


p1 = platform.Platform((500, 550))
sp1 = spike_platform.Spike_platform((100, 200))

platform_group.add(p1)
spike_platform_group.add(sp1)

# all_group.add(p1)
# all_group.add(sp1)






platform_group.add(platform.Platform((1000, 350)))
platform_group.add(platform.Platform((0, 350)))
platform_group.add(platform.Platform((GAME_WIDTH // 2, 150)))
platform_group.add(platform.Platform((GAME_WIDTH // 2 -300, 150)))

spike_platform_group.add(spike_platform.Spike_platform((800, 150)))
platform_group.add(platform.Platform((340, 213)))
platform_group.add(platform.Platform((468, 568)))
platform_group.add(platform.Platform((120, 460)))
platform_group.add(platform.Platform((GAME_WIDTH // 2, 569)))
platform_group.add(platform.Platform((GAME_WIDTH // 2 -123, 560)))
spike_platform_group.add(spike_platform.Spike_platform((340, 300)))
spike_platform_group.add(spike_platform.Spike_platform((190, 499)))


for p in platform_group:
    all_group.add(p)

for sp in spike_platform_group:
    all_group.add(sp)






def main():
    global states

    running = True

    while running:
        clock.tick(TICK_RATE)

        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()

                if event.key == pygame.K_p:

                    if states == 1:
                        states = 2

                    elif states == 2:
                        states = 1


                if event.key == pygame.K_SPACE:
                    if states == 0:
                        states = 1
                    if states == 1:
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound("assests/sounds/jump.mp3"))
                        mixer.music.set_volume(0.50)

                    if states == 3:
                        states = 1
                        player.is_dead = False    


                if event.key == pygame.K_LEFT:
                    if states == 1:
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound("assests/sounds/slither.mp3"))
                        mixer.music.set_volume(0.50)


                if event.key == pygame.K_RIGHT:
                    if states == 1:
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound("assests/sounds/slither.mp3"))
                        mixer.music.set_volume(0.50)















        draw()
        update()

    pygame.quit()




def draw():
    global states
    # main menu
    if states == 0:
        menu()

    # running
    if states == 1:
        surface.blit(background_image, [0, 0])
        player_group.draw(surface)
        lava_group.draw(surface)
        platform_group.draw(surface)
        spike_platform_group.draw(surface)

    # pause
    if states == 2:
        pause()

    # death
    if states == 3:
        pass







    pygame.display.flip()


def update():

    global states
    # main menu
    if states == 0:
        pass

    # running
    if states == 1:
        if player.is_dead == True:
            states = 3
        player_group.update(all_group, platform_group, lava_group, spike_platform_group)
        lava_group.update()
        platform_group.update(player_group)
        spike_platform_group.update(player_group)

    # pause
    if states == 2:
        pass

    # death
    if states == 3:
        surface.fill((100, 100, 100))




def menu():
    surface.fill((255, 200, 200))



def pause():
    surface.fill((200, 200, 255))


mixer.music.load("assests/sounds/song.mp3")
mixer.music.set_volume(50)

pygame.mixer.Channel(1).play(pygame.mixer.Sound("assests/sounds/song.mp3"))




if __name__ == "__main__":
    main()

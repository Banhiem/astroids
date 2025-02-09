# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    print("'Starting asteroids!'")
    print("Screen width: 1280")
    print("Screen height: 720")
    dt=0
    Clock=pygame.time.Clock()
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.draw(screen)
        pygame.display.flip()
        dt=Clock.tick(60)/1000

if __name__ == "__main__":
    main()

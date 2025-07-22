import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width:", SCREEN_WIDTH)
    print(f"Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill screen with black
        screen.fill((0,0,0))

        # Update game logic here
        
        # update the display
        pygame.display.flip()

        # cap the frame and get delta time in Asteroids
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField

def main():

    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width:", SCREEN_WIDTH)
    print(f"Screen height:", SCREEN_HEIGHT)

    # Groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    astroids = pygame.sprite.Group()

    # Group assignment
    Player.containers = (updatables, drawables)
    Asteroid.containers = (astroids, updatables, drawables)
    AsteroidField.containers = (updatables)

    # Instantiation
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astroid_field = AsteroidField()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill screen with black
        screen.fill((0,0,0))

        # Update game logic here
        updatables.update(dt)

        for drawable in drawables:
            drawable.draw(screen)

        # update the display
        pygame.display.flip()

        for astroid in astroids:
            if astroid.collision(player):
                print("Game Over!")
                return

        # cap the frame and get delta time in Asteroids
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()

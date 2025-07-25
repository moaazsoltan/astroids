import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, float(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt


def main():
    print("Hello from astroids")

    # quik tests
    astroid = Asteroid(0, 0, 2)
    print(astroid.velocity)


if __name__ == "__main__":
    main()

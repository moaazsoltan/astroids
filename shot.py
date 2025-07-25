import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, float(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt




def main():
    print("Hello from shot")


if __name__ == "__main__":
    main()

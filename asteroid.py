import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, float(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS :
            self.kill()
            return
        if self.radius > ASTEROID_MIN_RADIUS :
            # First Astroid
            angle = random.uniform(20,50)
            new_vector_1 = self.velocity.rotate(angle)
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_1.velocity = new_vector_1 * 1.2

            # Second Astroid
            new_vector_2 = self.velocity.rotate(-angle)
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_2.velocity = new_vector_2 * 1.2

            # Destroy big asteroid
            self.kill()




def main():
    print("Hello from astroids")

    # quik tests
    astroid = Asteroid(0, 0, 2)
    print(astroid.velocity)


if __name__ == "__main__":
    main()

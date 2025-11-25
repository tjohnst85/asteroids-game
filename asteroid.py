import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random




class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
             log_event("asteroid_split")
             random_angle = random.uniform(20, 50)
             new_angle_1 = self.velocity.rotate(random_angle)
             new_angle_2 = self.velocity.rotate(-random_angle)
             new_radius = self.radius - ASTEROID_MIN_RADIUS
             first_asteroid = Asteroid(self.position.x, self.position.y,new_radius)
             second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
             first_asteroid.velocity = (new_angle_1 * 1.2)
             second_asteroid.velocity = (new_angle_2 *1.2)
             return first_asteroid, second_asteroid


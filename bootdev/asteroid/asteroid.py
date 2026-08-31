import pygame
from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            angle1 = self.velocity.rotate(new_angle) * 1.2
            angle2 = self.velocity.rotate(-new_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            m1 = Asteroid(self.position.x, self.position.y, new_radius)
            m2 = Asteroid(self.position.x, self.position.y, new_radius)
            m1.velocity = angle1
            m2.velocity = angle2
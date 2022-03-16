import math

import pygame
from pygame import display

WHITE = (255, 255, 255)

class Bullet:
    def __init__(self, x, y, angle, window):
        self.x = x
        self.y = y

        self.window = window
        self.speed = 2
        self.radius = 5
        self.dx = math.cos(angle) * self.speed
        self.dy = -(math.sin(angle) * self.speed)

    def drawbullet(self):
        pygame.draw.circle(self.window, (255, 255, 255), (self.x, self.y), self.radius)

    def update(self):
        self.x += float(self.dx)
        self.y += float(self.dy)

import pygame, math

ball = pygame.image.load('sprites/NewProjectile.png')

class Bullet():
    def __init__(self, x, y, angle, window):
        self.x = x
        self.y = y

        self.window = window
        self.speed = 2
        self.radius = 5

        self.dx = math.cos(angle) * self.speed
        self.dy = -(math.sin(angle) * self.speed)

    def drawbullet(self, window):
        window.blit(ball, (self.x - 32 , self.y - 29))
        
    def update(self):
        self.x += float(self.dx)
        self.y += float(self.dy)

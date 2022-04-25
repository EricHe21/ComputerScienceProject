import pygame, math
from tiles import TileMap
screen_res = (1920,1088) #Resolution of the game screen

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/NewProjectile.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 

        self.speed = 2.5
        self.radius = 5

        self.dx = math.cos(angle) * self.speed
        self.dy = -(math.sin(angle) * self.speed)

    #Checks to see if the character has collided with a tile and returns a list of collided tiles
    def hits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits


    #Checks to see if the player has collided with a tile on the left or right side
    def checkCollisions(self, tiles):
        collisions = self.hits(tiles)
        for tile in collisions:
            if abs(self.rect.right - tile.rect.left) < 10:  # Hit tile moving right
                self.kill()
            if abs(self.rect.left - tile.rect.right) < 10:  # Hit tile moving left
                self.kill()  
            if abs(self.rect.bottom - tile.rect.top) < 10:  # Hit tile moving Down
                self.kill()  
            if abs(self.rect.top - tile.rect.bottom) < 10:  # Hit tile moving Up
                self.kill()   


    def update(self, tiles):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self.checkCollisions(tiles)
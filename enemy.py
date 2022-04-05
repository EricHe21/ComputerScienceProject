import pygame

"""finds the images from your file and allows vcs to access them""" 
slime = pygame.image.load("sprites/Slime01.png")

class Enemy():
    def __init__(self, x, y, width, height, window):
        """The x and y self values are there to allows you to place the images on the screen"""
        self.x = x
        self.y = y
        self.window = window
        self.width = width
        self.height = height

        """"How fast the enemy is moving"""
        self.speed= 250
        
        """defines the hitbox"""
        self.enemy_hitbox = (self.x, self.y , 110, 55)

        self.visible = True
        self.enemy_health = 3

    """sees if the bullets of the player has hit the enemy and wont work once the enemy is out of health """
    def enemy_hurt(self):
        if self.enemy_health > 1: 
            self.enemy_health -= 1
        else:
            self.visible = False

    """allows the enemy to follow the player"""
    def move(self, dt, player): 
        """"follows the player alonge the x axis"""
        if self.x > player.movement[0]:
            self.x -= self.speed * dt
        elif self.x < player.movement[0]:
            self.x += self.speed * dt

        """""follows the player on the y axis"""""
        if self.y < player.movement[1]:
            self.y += self.speed * dt
        elif self.y > player.movement[1]:
            self.y -= self.speed * dt

        """Draws the images on the screen with its x and y values"""
    def enemy_draw(self, window, dt, player):
        """alllows the images to move to the player"""
        self.move(dt, player)
        
        """"WIll only run when the enemy is not dead"""
        if self.visible == True:
            """"Draws the enemy on the screen"""
            window.blit(slime, (self.x, self.y))
            """We put the self.hitbox here because it allows the hitbox itself to move with the enmey"""
            self.enemy_hitbox = (self.x, self.y , 110, 55)
            

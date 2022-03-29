import pygame  



"""finds the images from your file and allows vcs to access them""" 
slime = pygame.image.load("sprites/Slime01.png")

class Enemy():
    def __init__(self, x, y, width, height, end, window):
        """The x and y self values are there to allows you to place the images on the screen"""
        self.x = x
        self.y = y
        self.window = window
        self.width = width
        self.height = height
        
        """defines the hitbox"""
        self.enemy_hitbox = (self.x, self.y , 110, 55)
        
        """This sets the end points of the enemy"""
        self.path = [x, end] 

        """How fast the images is moving"""
        self.vel = 200

        self.visible = True
        self.enemy_health = 3

    """sees if the bullets of the player has hit the enemy and wont work once the enemy is out of health """
    def hit(self):
        if self.enemy_health > 1: 
            self.enemy_health -= 1
        else:
            self.visible = False

    def move(self, dt):
        """handles the movemet of the enemy"""
        if self.vel > 0:
            """Checks if the enemy is moving past its right end point"""
            if self.x < self.path[1] + self.vel:
                self.x += self.vel * dt
            else:
                """Changes the direction of the enemy"""
                self.vel = self.vel * -1
                self.x += self.vel * dt
                self.walkCount = 0
        else:
            """Checks if the enemy is reaching the left end point"""
            if self.x > self.path[0] - self.vel:
                self.x += self.vel * dt
            else:
                self.vel = self.vel * -1
                self.x += self.vel  * dt
                self.walkCount = 0 


        """Draws the images on the screen with its x and y values"""
    def enemy_draw(self, window, dt):
        """alllows the images to move"""
        self.move(dt)
        
        """"WIll only run when the enemy is not dead"""
        if self.visible == True:
            """"Draws the enemy on the screen"""
            window.blit(slime, (self.x, self.y))
            """We put the self.hitbox here because it allows the hitbox itself to move with the enmey"""
            self.enemy_hitbox = (self.x, self.y , 110, 55)
            

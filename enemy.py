import pygame  
"""finds the images form your file and allows vcs to access them""" 
slime = pygame.image.load(r'C:\Users\Eric\Computer Science Game Project\sprite\Slime01.png').convert()

class Enemy():
    def __init__(self, x, y, width, height, end, win):
        """The x and y self values are there to allows you to place the images on the screen"""
        self.x = x
        self.y = y
        self.window = win
        self.width = width
        self.height = height

        """This sets the end points of the enemy"""
        self.path = [x, end] 
        
        """How fast the images is moving"""
        self.vel = .5


    """Draws the images on the screen with its x and y values"""
    def draw(self, win):
        win.blit(slime, (self.x, self.y))

        """alllows the images to move"""
        self.move()
        

    def move(self):
        """handles the movemet of the enemy"""
        if self.vel > 0:
            """Checks if the enemy is moving past its right end point"""
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                """Changes the direction of the enemy"""
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            """Checks if the enemy is reaching the left end point"""
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
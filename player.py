import pygame

player = pygame.image.load("sprites/NewGumbo.png")

class Player():
    """Responsible for the creation of the Character itself"""
    def __init__ (self, window, bounds):
        
        #Size of the Character
        self.x = player.get_width()
        self.y = player.get_height()
        
        #Movement Variable for the Character
        self.movement = [10,10]
        
        #Creates a rectangle out of the screens resolution and the bounds
        self.bounds = bounds
        self.window = window

        #Sets the default button presses to false
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
    
    
    def getPlayerWidth(self):
        return int(self.x)
    
    def getPlayerHeight(self):
        return int(self.y)

    def getPlayerPositionX(self):
        return int(self.movement[0])

    def getPlayerPositionY(self):
        return int(self.movement[1])
    
    """Draws the Character On Screen"""
    def draw(self, dt):
        """Checks the inputs of the user and responds accordingly"""
        if self.left_pressed and not self.right_pressed:
              self.movement[0] =  self.movement[0] - 500 * dt
        if self.right_pressed and not self.left_pressed:
             self.movement[0] = self.movement[0] + 500 * dt
        if self.up_pressed and not self.down_pressed:
            self.movement[1] = self.movement[1] - 500 * dt
        if self.down_pressed and not self.up_pressed:
            self.movement[1] = self.movement[1] + 500 * dt
        

        """Checks to see if the Player is moving out of bounds"""
        if self.movement[0] < 0:
            self.movement[0] = 0
        if self.movement[0] + self.x > self.bounds[0]:
            self.movement[0] = self.bounds[0] - self.x
        if self.movement[1] <= 0:
            self.movement[1] = 0
        if self.movement[1] + self.y >= self.bounds[1]:
            self.movement[1] = self.bounds[1] - self.y

        self.window.blit(player, (self.movement[0], self.movement[1]))
   



    

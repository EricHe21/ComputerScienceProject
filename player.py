import pygame

class Player():
    """Responsible for the creation of the Character itself"""
    def __init__ (self, x, y, window, bounds):
        
        #Size of the Character
        self.x = x
        self.y = y
        
        #Movement Variable for the Character
        self.movement = [10,10]
        
        #Creates a rectangle out of the screens resolution and the bounds
        self.bounds = bounds
        self.screen_rect = pygame.Rect(self.movement[0], self.movement[1], self.x, self.y)
        self.window = window
       
        #Stores the attributes requried for making the character
        self.rect = pygame.Rect(0, 0, self.x, self.y)
        self.color = (255, 255, 255)
        

        #Sets the default button presses to false
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
    
    
    def draw(self):
        """Draws the Character on the Screen """
        pygame.draw.rect(self.window,self.color,self.rect)
        
  
    
    def update(self):
        """Checks the inputs of the user and responds accordingly"""
        if self.left_pressed and not self.right_pressed:
              self.movement[0] =  self.movement[0] - 1
        if self.right_pressed and not self.left_pressed:
           self.movement[0] = self.movement[0] + 1
        if self.up_pressed and not self.down_pressed:
            self.movement[1] = self.movement[1] - 1
        if self.down_pressed and not self.up_pressed:
            self.movement[1] = self.movement[1] + 1
        """Checks to see if the Player is moving out of bounds"""
        if self.movement[0] < 0:
            self.movement[0] = 0
        if self.movement[0] + self.x > self.bounds[0]:
            self.movement[0] = self.bounds[0]  - self.x
        if self.movement[1] <= 0:
            self.movement[1] = 0
        if self.movement[1] + self.y >= self.bounds[1]:
            self.movement[1] = self.bounds[1] - self.y

        self.rect = pygame.Rect(self.movement[0], self.movement[1], self.x, self.y)
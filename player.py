import pygame
from spritesheet import Spritesheet
from tiles import TileMap


class Player(pygame.sprite.Sprite):
    """Responsible for the creation of the Character itself"""
    def __init__ (self, window):
        pygame.sprite.Sprite.__init__(self)
        
        #Initializes the players avatar via a spritesheet
        self.player = Spritesheet("Character Assets\Character Sprites.png").parse_sprite("NewGumbo.png")
        self.rect = self.player.get_rect() #Grabs the characters rectangle

        

        
        self.window = window 

        #Sets the characters Origin position to the center of the screen
        self.rect.x = (self.window.get_width() / 2) - 50 
        self.rect.y = (self.window.get_height() / 2) - 100

        #Control the characters speed and position
        self.position, self.velocity = pygame.math.Vector2(self.rect.x,self.rect.y), pygame.math.Vector2(self.rect.x,self.rect.y)

        #Button checks to see what button is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        #Directional Checks for the Player
        self.face_left = False
        self.face_right = False
        self.face_up = False 
        self.face_down = False
        
        

    #Checks to see if the character has collided with a tile and returns a list of collided tiles
    def hits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits

    #Checks to see if the player has collided with a tile on the left or right side
    def checkCollisionsx(self, tiles):
        collisions = self.hits(tiles)
        for tile in collisions:
            if abs(self.rect.right - tile.rect.left) < 10:  # Hit tile moving right
                self.position.x = tile.rect.left - self.rect.w
                self.rect.x = self.position.x
            elif abs(self.rect.left - tile.rect.right) < 10:  # Hit tile moving left
                self.position.x = tile.rect.right
                self.rect.x = self.position.x


    #Checks to see if the player has collided with a tile on the Upper or Bottom side
    def checkCollisionsy(self, tiles):
        collisions = self.hits(tiles)
        for tile in collisions:
            if abs(self.rect.bottom - tile.rect.top) < 10:  # Hit tile moving Down
                self.position.y = tile.rect.top - self.rect.h
                self.rect.y = self.position.y
            elif abs(self.rect.top - tile.rect.bottom) < 10:  # Hit tile moving Up
                self.position.y = tile.rect.h
                self.rect.y = self.position.y



    """Draws the Character On Screen"""
    def draw(self, window):    
        window.blit(self.player, (self.rect.x, self.rect.y))

    #Controls the player's velocity in the horizontal directions
    def horizontal_movement(self, dt):
        if self.left_pressed and not self.right_pressed:
            self.velocity.x -= 500 * dt
            self.limit_velocityX(500)
            self.position.x -= self.velocity.x * dt 
            self.rect.x = self.position.x  
        elif self.right_pressed and not self.left_pressed:
            self.velocity.x += 500 * dt
            self.limit_velocityX(500)
            self.position.x += self.velocity.x * dt 
            self.rect.x = self.position.x
            
    #Controls the player's velocity in the vertical directions
    def vertical_movement(self, dt):
        if self.up_pressed and not self.down_pressed:
            self.velocity.y -= 500 * dt
            self.limit_velocityY(500)
            self.position.y -= self.velocity.y * dt 
            self.rect.y = self.position.y
        elif self.down_pressed and not self.up_pressed:
            self.velocity.y += 500 * dt
            self.limit_velocityY(500)
            self.position.y += self.velocity.y * dt
            self.rect.y = self.position.y
    #Ensures the player's velocity isn't too fast (X - Direction)
    def limit_velocityX(self, max_vel):
        self.velocity.x = max(max_vel, min(self.velocity.x, max_vel))

    #Ensures the player's velocity isn't too fast (Y - Direction)
    def limit_velocityY(self, max_vel):
        self.velocity.y = max(max_vel, min(self.velocity.y, max_vel))

    #Responsible for updating the functions accordingly
    def update(self, dt, tiles):
        self.hits(tiles)
        self.horizontal_movement(dt)
        self.checkCollisionsx(tiles)
        self.vertical_movement(dt)
        self.checkCollisionsy(tiles)
    



    


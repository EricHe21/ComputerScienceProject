import pygame  
from spritesheet import Spritesheet
from tiles import TileMap
 


class Enemy(pygame.sprite.Sprite):
    """Responsible for making the Enemy itself"""
    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)

        #Initalizes the Enemy's avatar via a spritesheet
        self.entity = Spritesheet("Character Assets\Character Sprites.png").parse_sprite("Sprite-0001.png")
        self.rect = self.entity.get_rect() #Grabs the charatcers rectangle

        self.window = window

        #Sets the Enemy's initial position on the screen
        self.rect.x = int(self.window.get_width() / 3)
        self.rect.y = int(self.window.get_height() / 3)

    #Draws the Enemy on screen
    def draw(self, window):    
        window.blit(self.entity, (self.rect.x, self.rect.y))
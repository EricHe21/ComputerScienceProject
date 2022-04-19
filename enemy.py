import pygame, math, random
from spritesheet import Spritesheet
from tiles import TileMap

screen_res = (1920,1088)
class Enemy(pygame.sprite.Sprite):
    """Responsible for making the Enemy itself"""
    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)

        #Initalizes the Enemy's avatar via a spritesheet
        self.image = Spritesheet("Character Assets\Character Sprites.png").parse_sprite("Sprite-0001.png")
        self.rect = self.image.get_rect() #Grabs the charatcers rectangle

        self.window = window

        #Sets the Enemy's initial position on the screen
        self.rect.x = random.randrange(screen_res[0] - self.rect.w)
        self.rect.y = random.randrange(100, 800)

        self.speed = 1
    
        self.enemy_health = 3
        
    #stops the enemy from going inside of the player and crashing the game
    def enemyCollision(self, player):
                if self.rect.colliderect(player.rect):
                        if abs(self.rect.top - player.rect.bottom) < 10:
                            self.rect.y = (self.rect.y + self.rect.h) - 90

                        if abs(self.rect.bottom - player.rect.top) < 10:
                            self.rect.y = (player.rect.y - player.rect.h) + 15
                            
                        if abs(self.rect.right - player.rect.left) < 10:
                            self.rect.x = (self.rect.x - self.rect.w) + 95
                            
                        if abs(self.rect.left - player.rect.right) < 10:
                            self.rect.x = self.rect.x + 1
                        

    def move_towards_player(self, player):
                # Find direction vector (dx, dy) between enemy and player.
                dirvect = pygame.math.Vector2(player.rect.x - self.rect.x,
                                            player.rect.y - self.rect.y)
                dirvect.normalize()
                # Move along this normalized vector towards the player at current speed.
                dirvect.scale_to_length(self.speed)
                self.rect.move_ip(dirvect)

    def update(self, player):
        self.move_towards_player(player)
        self.enemyCollision(player)
        if self.enemy_health <= 0:
            self.kill() 
            del self 


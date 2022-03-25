import pygame
import math
from projectile import Bullet

player = pygame.image.load("sprites/NewGumbo.png")
bullets = []

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

        """defines the hitbox for collisions between player and enemy"""
        self.player_hitbox = (self.movement[0], self.movement[1] + 20, 90, 120)
        self.enemy_hitbox = (self.x, self.y , 110, 55)
 
        self.health = 5
        self.visible = True
    
    
    def getPlayerWidth(self):
        return int(self.x)
    
    def getPlayerHeight(self):
        return int(self.y)

    def getPlayerPositionX(self):
        return int(self.movement[0])

    def getPlayerPositionY(self):
        return int(self.movement[1])

    # def hurt(self, player): 
    #     if self.health > 0:
    #         self.health -= 1 
    #     else: 
    #         self.visible == False 
   
    # def heal(self):
    #     if self.health < self.max_health:
    #         self.health += 1

    def shoot(self, dt):
        pos = pygame.mouse.get_pos()
        x_dist = (pos[0] - self.movement[0])
        y_dist = -(pos[1] - self.movement[1])
        self.angle = float(math.atan2(y_dist, x_dist))

        if pygame.mouse.get_pressed()[0] and self.fire == False:
            self.fire = True
            bullet = Bullet((self.movement[0] + self.x/2), (self.movement[1] + self.y/2), self.angle, self.window)
            bullets.append(bullet)
        if pygame.mouse.get_pressed()[0] == False:
            self.fire = False

        for item in bullets:
            Bullet.drawbullet(item)
            Bullet.update(item)
    
     
    """used for collision detection"""
    def hit(self, enemy):
        collision_tolerance = 10

        """creates a rectange out of the enemy hitbox"""
        enemy_HitBoxRect = pygame.Rect(enemy.enemy_hitbox)
 
        """"creates a rectange out of the players hitbox"""
        self.player_HitBoxRect = pygame.Rect(self.player_hitbox)
 
        """when the players hitbox hits the enemy, it blocks the player from going through the enemy"""
        if self.player_HitBoxRect.colliderect(enemy_HitBoxRect):
            if enemy.visible == True:
                if abs(self.player_HitBoxRect.top - enemy_HitBoxRect.bottom) < collision_tolerance:
                    self.movement[1] = (enemy_HitBoxRect.y + enemy_HitBoxRect.height) + 100
    
                if abs(self.player_HitBoxRect.bottom - enemy_HitBoxRect.top) < collision_tolerance:
                    self.movement[1] = (self.player_HitBoxRect.y - self.player_HitBoxRect.height)  
    
                if abs(self.player_HitBoxRect.right - enemy_HitBoxRect.left) < collision_tolerance:
                    self.movement[0] = (enemy_HitBoxRect.x - enemy_HitBoxRect.width) - 150

                if abs(self.player_HitBoxRect.left - enemy_HitBoxRect.right) < collision_tolerance:
                    self.movement[0] = enemy_HitBoxRect.x + 250
        """"Sees if the bullet is inside of the enemy hitbox and will pop the bullet out of the list once they hit"""        
        if enemy.visible == True:
            for bullet in bullets:
                if bullet.y - bullet.radius < enemy_HitBoxRect[1] + enemy_HitBoxRect[3] and bullet.y + bullet.radius > enemy_HitBoxRect[1]:
                    if bullet.x + bullet.radius > enemy_HitBoxRect[0] and bullet.x - bullet.radius < enemy_HitBoxRect[0] + enemy_HitBoxRect[2]:
                        bullets.pop(bullets.index(bullet))
                        enemy.hit()
    

    """Draws the Character On Screen"""
    def player_draw(self,window, dt, enemy):
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
        
        self.hit(enemy)



        self.player_hitbox = (self.movement[0], self.movement[1] + 20, 90, 120)
        window.blit(player, (self.movement[0], self.movement[1]))
    
 
 
 
   


import pygame, math
from projectile import Bullet

player = pygame.image.load("sprites/NewGumbo.png")
player_hurt = pygame.image.load("sprites/GumboHurt.png")
shoot_delay = 0
bullets = []

class Player():
    """Responsible for the creation of the Character itself"""
    def __init__ (self, window, bounds):
        self.last = pygame.time.get_ticks()
        self.cooldown = 2000
        self.bullet_cooldown = 1000
    
        self.image = pygame.image.load("sprites/NewGumbo.png")

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
        self.max_health = 10
        self.visible = True

        self.score = 0
    
    def getPlayerWidth(self):
        return int(self.x)
    
    def getPlayerHeight(self):
        return int(self.y)

    def getPlayerPositionX(self):
        return int(self.movement[0])

    def getPlayerPositionY(self):
        return int(self.movement[1])

    """"this handles the players health and damage"""
    def hurt(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
    """"allows the player to heal"""
    def heal(self):
        if self.health < self.max_health:
            self.health += 1
 
       

    """used for collision detection"""
    def hit(self, enemy):
        collision_tolerance = 10


        """creates a rectange out of the enemy hitbox"""
        enemy_HitBoxRect = pygame.Rect(enemy.enemy_hitbox)
        ehb = enemy_HitBoxRect
 
        """"creates a rectange out of the players hitbox"""
        self.player_HitBoxRect = pygame.Rect(self.player_hitbox)
        phb = self.player_HitBoxRect
 
        """when the players hitbox hits the enemy, it blocks the player from going through the enemy"""
        if self.player_HitBoxRect.colliderect(enemy_HitBoxRect):
            if enemy.visible:
                now = pygame.time.get_ticks()

                if abs(phb.top - ehb.bottom) < collision_tolerance:
                    self.movement[1] = (ehb.y + ehb.height) + 100
    
                if abs(phb.bottom - ehb.top) < collision_tolerance:
                    self.movement[1] = (phb.y - phb.height)  
    
                if abs(phb.right - ehb.left) < collision_tolerance:
                    self.movement[0] = (ehb.x - ehb.width) - 150

                if abs(phb.left - ehb.right) < collision_tolerance:
                    self.movement[0] = ehb.x + 250
            
                """changes the players image to the hurt sprite and subtracts points from the score"""
                self.score -= 5 
                # self.hurt()
                self.image = pygame.image.load("sprites/GumboHurt.png")
                self.last = now


    def bullet_Collision(self, enemy):
        """creates a rectange out of the enemy hitbox"""
        enemy_HitBoxRect = pygame.Rect(enemy.enemy_hitbox)   
        ehb = enemy_HitBoxRect        
        """"Sees if the bullet is inside of the enemy hitbox and will pop the bullet out of the list once they hit"""        
        if enemy.visible == True:
            for bullet in bullets:
                if bullet.y - bullet.radius < ehb[1] + ehb[3] and bullet.y + bullet.radius > ehb[1]:
                    if bullet.x + bullet.radius > ehb[0] and bullet.x - bullet.radius < ehb[0] + ehb[2]:
                        bullets.pop(bullets.index(bullet))
                        self.score += 10
                        enemy.enemy_hurt()


    """"handles the shooting of the player by shooting to the mouse when clicked"""
    def shoot(self, window):
        pos = pygame.mouse.get_pos()
        x_dist = (pos[0] - self.movement[0]) 
        y_dist = -(pos[1] - self.movement[1])

        """"finds the angles at which bullet need to travel at to the mouse"""
        self.angle = float(math.atan2(y_dist + 56, x_dist - 45))

        if self.visible:
            if pygame.mouse.get_pressed()[0] and self.fire == False:
                self.fire = True
                bullet = Bullet((self.movement[0] + self.x/2) , (self.movement[1] + self.y/2) , self.angle, self.window)
                bullets.append(bullet)
            if pygame.mouse.get_pressed()[0] == False:
                self.fire = False

            for item in bullets:
                Bullet.drawbullet(item, window)
                Bullet.update(item)
        
    

    """Draws the Character On Screen"""
    def player_draw(self, window, dt, enemy):
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
            
        """Will only work if the player is alive and handles all of the collision on the player"""
        if self.visible:
            self.hit(enemy)
            self.bullet_Collision(enemy)
            self.player_hitbox = (self.movement[0], self.movement[1] + 20, 90, 120)
            window.blit(self.image, (self.movement[0], self.movement[1]))


        if self.last > self.last + 2000: 
            self.image = pygame.image.load('sprites/NewGumbo.png')


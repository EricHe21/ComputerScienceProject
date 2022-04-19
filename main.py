import pygame, time, math
from pygame.locals import *
from player import Player
from enemy import Enemy
from tiles import *
from spritesheet import *
from projectile import Bullet


pygame.init() #Initializes pygame
font = pygame.font.SysFont('comicsans', 30, True)
screen_res = (1920,1088) #Resolution of the game screen

#sets the display for the game window and the desired background
screen = pygame.display.set_mode(screen_res, pygame.RESIZABLE)
bg = pygame.image.load("Stage1 Assets\Stage1Floor.png").convert_alpha()

#Runs Game for as long as the user wants
clock = pygame.time.Clock()
previousTime = time.time()

#Game Spritesheet Initialization
S1spritesheet = Spritesheet("Stage1 Assets\Stage1 Spritesheet.png")
player = Player(screen)
map = TileMap("Stage1 Assets\Stage1Starting.csv", S1spritesheet)

allGroup = pygame.sprite.Group()
allGroup.add(player)

playerGroup = pygame.sprite.Group()
playerGroup.add(player)

bulletGroup = pygame.sprite.Group()

enemyGroup = pygame.sprite.Group()
for i in range(1):
    enemy = Enemy(screen)
    allGroup.add(enemy)
    enemyGroup.add(enemy)
    
"""handles the shooting of the player by shooting to the mouse when clicked"""
def shoot():
        pos = pygame.mouse.get_pos()
        x_dist = (pos[0] -  player.rect.x) 
        y_dist = -(pos[1] - player.rect.y)
        """"finds the slop/radians at which the bullet need to travel"""
        angle = (math.atan2(y_dist + 60, x_dist - 30))  

        if pygame.mouse.get_pressed()[0] and player.fire == False:
            player.fire = True
            bullet = Bullet((player.rect.x) , (player.rect.y + 40) ,angle)  
            bulletGroup.add(bullet)      
                
        if pygame.mouse.get_pressed()[0] == False:
            player.fire = False



#Responsible for Drawing items onto the sdcreen (Use the Function for Drawings)d
def redrawGameWindow():
        screen.blit(bg, (0,0))
        map.draw_map(screen)
        allGroup.draw(screen)
        bulletGroup.draw(screen)
        player.drawHealth(screen)

        playerGroup.update(dt, map.tiles, playerGroup, enemyGroup, enemy)
        enemyGroup.update(player)
        bulletGroup.update(map.tiles)



        text = font.render('Score: ' + str(player.score), 1, (255,255,255))
        screen.blit(text, (10,1000))
        shoot()
        pygame.display.flip() #Updates the entirety of all the contents on the screen
        pygame.display.update()


# Controls the main events of the game (i.e. Movement, shooting, etc.)
while True:
    clock.tick()
    currentTime = time.time()
    dt = currentTime - previousTime
    previousTime = currentTime

    for event in pygame.event.get():
        #Quits the game when the user presses the quit button
        if event.type == QUIT:
            pygame.quit()

        hits = pygame.sprite.groupcollide(enemyGroup, bulletGroup, False, True)
        for enemy in hits:
            enemy.enemy_health -= 1 
            player.score += 10

        #Detects whenever the user presses down on a key
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player.left_pressed = True
                        player.face_left = True
                        player.face_right = False
                        player.face_up = False 
                        player.face_down = False 
                    if event.key == pygame.K_d:
                        player.right_pressed = True
                        player.face_left = False
                        player.face_right = True
                        player.face_up = False 
                        player.face_down = False               
                    if event.key == pygame.K_w:
                        player.up_pressed = True
                        player.face_left = False
                        player.face_right = False
                        player.face_up = True
                        player.face_down = False
                    if event.key == pygame.K_s:
                        player.down_pressed = True
                        player.face_left = False
                        player.face_right = False
                        player.face_up = False 
                        player.face_down = True
       
        #Detects whenever the user pressed up on a key
        if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player.left_pressed = False
                    if event.key == pygame.K_d:
                        player.right_pressed = False
                    if event.key == pygame.K_w:
                        player.up_pressed = False
                    if event.key == pygame.K_s:
                        player.down_pressed = False 



    redrawGameWindow() #Redraws window Tiles, Player, and Enemy
    clock.tick() #Tracks time (FPS) of the game
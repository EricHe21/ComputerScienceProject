import pygame, time, math, sys
from pygame.locals import *
from player import Player
from enemy import Enemy
from tiles import *
from spritesheet import *
from projectile import Bullet
from buttons import Button
from pygame import mixer
from cProfile import run
from pickle import FALSE
from turtle import width

pygame.init() #Initializes pygame
font = pygame.font.SysFont('comicsans', 50, True)
screen_res = (1920,1088) #Resolution of the game screen

pygame.mixer.init()
projectile_sound = pygame.mixer.Sound('projectilesound.mp3')


#sets the display for the game window and the desired background
screen = pygame.display.set_mode(screen_res, pygame.RESIZABLE)
bg = pygame.image.load("Stage1 Assets\Stage1Floor.png").convert_alpha()

#image for the button
setting_image = pygame.image.load('sprites\setting-2.png').convert_alpha()
setting_button = Button(100, 200,setting_image, 2)

#Runs Game for as long as the user wants
clock = pygame.time.Clock()
previousTime = time.time()

#Game Spritesheet Initialization
S1spritesheet = Spritesheet("Stage1 Assets\Stage1 Spritesheet.png")
player = Player(screen)
map = TileMap("Stage1 Assets\Stage1Starting.csv", S1spritesheet)

# Loads the game music
music = pygame.mixer.music.load('gamemusic.mp3')
pygame.mixer.music.play(-1)

#groups for the sprites
allGroup = pygame.sprite.Group()
allGroup.add(player)
playerGroup = pygame.sprite.Group()
playerGroup.add(player)
bulletGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()

#handles the score, waves, and eneies on screen
limit = 1
wave = 0



def draw_text(text, color, surface, x, y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    textobj = font.render(text, True, color)
    textRect = textobj.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textobj, textRect)

#loads the menu back ground image
background_img = pygame.image.load('sprites\gamebackground.png').convert()
back_ground= pygame.transform.scale(background_img,(screen_res))

#loads the main menu buttons
mainmenu_button_img = pygame.image.load('sprites\Menu Button.png').convert_alpha()
mainmenu_button1 = Button(210,45,mainmenu_button_img, 0.4)
mainmenu_button2 = Button(210,245, mainmenu_button_img, 0.4)
mainmenu_button3 = Button(210,445, mainmenu_button_img, 0.4)

# Creates the main menu
def main_menu():
    clock.tick()
    WHITE = (255,255,255)
    i = 0
    run = True
    text_button1 = 'PLAY'
    text_button2 = 'SETTINGS'
    text_button3 = 'HOW TO PLAY'
    width = 1920
    while run:

        for event in pygame.event.get():
        # Quits the game when the user presses the quit button
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        
        screen.blit(back_ground,(i,0))
        screen.blit(back_ground,(width+i,0))
        if i == -width:
            screen.blit(back_ground,(width+i,0))
            i = 0

        i -= 1

        mainmenu_button1.drawbutton(screen)
        if mainmenu_button1.action1 == True:
            break
        mainmenu_button2.drawbutton2(screen)
        if mainmenu_button2.action2 == True:
            settings_screen()
        mainmenu_button3.drawbutton3(screen)
        #if mainmenu_button3.action3 == True:
           # break
        draw_text(text_button1, WHITE, screen, 359, 225)
        draw_text(text_button2, WHITE, screen, 319, 425)
        draw_text(text_button3, WHITE, screen, 294,625)

        pygame.display.update()
        clock.tick()


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

        text = font.render("Score: " + str(player.score), 1, (255,255,255))
        waves = font.render("Wave: " + str(wave), 1, (255,255,255))
        screen.blit(text, (10,980))
        screen.blit(waves, (1700, 980))
 
            
            
        shoot()
        pygame.display.flip() #Updates the entirety of all the contents on the screen
        pygame.display.update()

def settings_screen():
    clock.tick()
    screen.fill((255, 0, 0))
    
    run = True
    while run:
        for event in pygame.event.get():
        # Quits the game when the user presses the quit button
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.flip()
    pygame.display.update()
    clock.tick()

"""handles the shooting of the player by shooting to the mouse when clicked"""
def shoot():
        pos = pygame.mouse.get_pos()
        x_dist = (pos[0] -  player.rect.x) 
        y_dist = -(pos[1] - player.rect.y)
        """"finds the slop/radians at which the bullet need to travel"""
        angle = (math.atan2(y_dist + 60, x_dist - 30))  

        if pygame.mouse.get_pressed()[0] and player.fire == False:
            # projectile_sound.play()
            player.fire = True
            bullet = Bullet((player.rect.x) , (player.rect.y + 40) ,angle)  
            bulletGroup.add(bullet)      
                
        if pygame.mouse.get_pressed()[0] == False:
            player.fire = False

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

        #handles the bullet collision with the enemy class
        hits = pygame.sprite.groupcollide(enemyGroup, bulletGroup, False, True)
        for enemy in hits:
            enemy.enemy_health -= 1 
            player.score += 10

        #checks if the enemy group is empty and then adds one to the wave and redraws new enemies
        if len(enemyGroup) == 0:
            wave += 1
            limit += 1
            if player.score >= 30:
                player.heal() 
                player.score -= 30
            for i in range(limit):
                enemy = Enemy(screen)
                allGroup.add(enemy)
                enemyGroup.add(enemy)




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


    main_menu()
    redrawGameWindow() #Redraws window Tiles, Player, and Enemy
    clock.tick() #Tracks time (FPS) of the game
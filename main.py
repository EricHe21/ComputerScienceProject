import pygame
from pygame.locals import *
from player import Player
import time
from enemy import Enemy
from tiles import *
from spritesheet import *


pygame.init() #Initializes pygame

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
enemy = Enemy(screen)
map = TileMap("Stage1 Assets\Stage1Starting.csv", S1spritesheet)

#Responsible for Drawing items onto the Screen (Use the Function for Drawings)
def redrawGameWindow():
        screen.blit(bg, (0,0))
        player.update(dt,map.tiles)
        map.draw_map(screen)
        player.draw(screen)
        enemy.draw(screen)
        pygame.display.flip() #Updates the entirety of all the contents on the screen


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
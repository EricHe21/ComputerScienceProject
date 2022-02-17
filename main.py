import pygame
from pygame.locals import *
import sys
from player import Player
from enemy import Enemy




pygame.init() #Initializes pygame

#gets the size of the current monitor that is being used
monitor_res = [pygame.display.Info().current_w,pygame.display.Info().current_h]

#Sets the size of the game window
screen = pygame.display.set_mode((monitor_res[0],monitor_res[1]), pygame.FULLSCREEN) 

#Runs Game for as long as the user wants
clock = pygame.time.Clock()

#Player Initialization
player = Player(40, 40, screen, monitor_res)
enemy = Enemy(40, 40, 32, 32, 500, screen)


# Controls the main events of the game (i.e. Movement, shooting, etc.)
while True:
    for event in pygame.event.get():
        #Quits the game when the user presses the quit button
        if event.type == QUIT:
            pygame.quit()
        #Detects whenever the user presses down on a key
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.left_pressed = True
                    if event.key == pygame.K_RIGHT:
                        player.right_pressed = True
                    if event.key == pygame.K_UP:
                        player.up_pressed = True
                    if event.key == pygame.K_DOWN:
                        player.down_pressed = True
        #Detects whenever the user pressed up on a key
        if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.left_pressed = False
                    if event.key == pygame.K_RIGHT:
                        player.right_pressed = False
                    if event.key == pygame.K_UP:
                        player.up_pressed = False
                    if event.key == pygame.K_DOWN:
                        player.down_pressed = False
                    
   
    screen.fill((0,0,0)) #Constantly refreshes the screen with the color black
    player.draw(screen) #Constantly draws the user on screen
    enemy.draw(screen)
    player.update() #Detects button inputs of the user as well as its position on screen 
    pygame.display.flip() #Updates the entirety of all the contents on the screen

    clock.tick() #Tracks time (FPS) of the game



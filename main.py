import pygame
from pygame.locals import *
from player import Player
import time
from enemy import Enemy
import sys

pygame.init()  # Initializes pygame

# gets the size of the current monitor that is being used
monitor_res = [pygame.display.Info().current_w, pygame.display.Info().current_h]

# Sets the size of the game window
screen = pygame.display.set_mode((monitor_res[0], monitor_res[1]), pygame.FULLSCREEN)

# Runs Game for as long as the user wants
clock = pygame.time.Clock()
previousTime = time.time()

# Player and Enemy Initialization
player = Player(screen, monitor_res)
enemy = Enemy(40, 40, 32, 32, 500, screen)


# Responsible for Drawing items onto the Screen (Use the Function for Drawings)
def redrawGameWindow(bullets=None):
    screen.fill((0, 0, 0))  # Constantly refreshes the screen with the color black

    player.shoot(dt)
    enemy.draw(screen, dt)
    player.draw(dt)  # Detects button inputs of the user as well as its position on screen
    pygame.display.flip()  # Updates the entirety of all the contents on the screen


# Controls the main events of the game (i.e. Movement, shooting, etc.)
while True:
    clock.tick()
    currentTime = time.time()
    dt = currentTime - previousTime
    previousTime = currentTime

    playerX = player.getPlayerPositionX()
    playerY = player.getPlayerPositionY()
    playerW = player.getPlayerWidth()
    playerH = player.getPlayerHeight()

    for event in pygame.event.get():
        # Quits the game when the user presses the quit button
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        # Detects whenever the user presses down on a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        # Detects whenever the user pressed up on a key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

    redrawGameWindow()
    clock.tick()  # Tracks time (FPS) of the game

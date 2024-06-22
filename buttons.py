from email.mime import image
import pygame, math, sys

class Button(object):
    def __init__(self, x, y, image, scale):
        self.x = x
        self.y = y
        # Gets the width of the image
        self.width = image.get_width()
        # Gets the height of the image
        self.height = image.get_height()
        # Scales the image to the disired sized
        self.image = pygame.transform.scale(image,(int(self.width * scale), int(self.height * scale)))
        # Turns the image into 
        self.rect = self.image.get_rect()
        # Sets the top left of the image to the disired place on screen
        self.rect_topleft = (x,y)
        # Sets mouse click to False by defult
        self.clicked = False
        
        self.action1 = False
        self.action2 = False
        self.action3  = False


    def drawbutton(self, window):
        #get mouse position
        action = False
        poss = pygame.mouse.get_pos()

        # checks if the mause is clicked
        if self.rect.collidepoint(poss):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.action1 = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Draws button on the creen
        window.blit(self.image, (self.x, self.y))
        return self.action1




    def drawbutton2(self, window):
        #get mouse position
        action = False
        poss = pygame.mouse.get_pos()

        # checks if the mause is clicked
        if self.rect.collidepoint(poss):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.action2 = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Draws button on the creen
        window.blit(self.image, (self.x, self.y))
        return self.action2



    def drawbutton3(self, window):
        #get mouse position
        action = False
        poss = pygame.mouse.get_pos()

        # checks if the mause is clicked
        if self.rect.collidepoint(poss):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.action3 = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Draws button on the creen
        window.blit(self.image, (self.x, self.y))
        return self.action3
    

    #this is a test
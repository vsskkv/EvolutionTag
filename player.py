#Date Created: 12/11/2020
#Author: Vikram Singh Kainth
#Title: Main file
#About: To be the main file where the program will initially run from

# Imports
import random
import pygame

# player object
class player(object):
    def __init__(self, x, y, width, height, heightScreen, widthScreen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velx = 5
        self.vely = 5
        self.heightScreen = heightScreen
        self.widthScreen = widthScreen

    def draw(self, win):
        self.move()
        self.rect = pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))
    
    # Move the chaser around randomly     
    def move(self):
        rand = random.randint(1,4)
        if(rand == 1 and self.vely + self.y < self.heightScreen - 11):
            self.y += self.vely
        if(rand == 2 and self.velx + self.x < self.widthScreen - 11):
            self.x += self.velx
        if(rand == 3 and self.y - self.vely > 0):
            self.y -= self.vely
        if(rand == 4 and self.x - self.velx > 0):
            self.x -= self.velx
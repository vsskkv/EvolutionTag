#Date Created: 12/11/2020
#Author: Vikram Singh Kainth
#Title: Main file
#About: To be the main file where the program will initially run

#Imports
import random
import pygame
pygame.init()

# Set window size + caption
widthScreen = 500
heightScreen = 500
win = pygame.display.set_mode((heightScreen, widthScreen))
pygame.display.set_caption("First game")

# Clock
clock = pygame.time.Clock()

# chaser object 
class player(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velx = 3
        self.vely = 3
        self.end = end
        self.path = [self.x, self.end]

    def draw(self, win):
        self.move()
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))
    
    # Move the     
    def move(self):
        if(RandMVMT() == 1 and self.vely > 0):
            if self.y + self.vely < self.path[1]:
                self.y += self.vely
            else:
                self.vely = self.vely * -1
        if(RandMVMT() == 2 and self.velx > 0):
            if self.x + self.velx < self.path[1]:
                self.x += self.velx
            else:
                self.velx = self.velx * -1
        if(RandMVMT() == 3 and self.vely < heightScreen):
            if self.y-self.vely > self.path[0]:
                self.y += self.vely
            else:
                self.vely = self.vely * -1
        if(RandMVMT() == 4 and self.velx < widthScreen):
            if self.x-self.velx > self.path[0]:
                self.x += self.velx
            else:
                self.velx = self.velx * -1
                    

# Rand number between 1-4
# 1=up, 2=right, 3=down, 4=left
def RandMVMT():
    return random.randint(1,4)
            

# Start state 
run = True

# Instaniate player(Chaser)
chaser = player(20, 20, 10, 10, widthScreen)

# Instaniate player(Runner)
runner = player(40, 40, 10, 10, 460)

# Event loop to track game 
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # List of keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and chaser.x > chaser.vel:
        chaser.x -= chaser.vel
    if keys[pygame.K_RIGHT] and chaser.x < (widthScreen - chaser.width - chaser.vel):
        chaser.x += chaser.vel
    if keys[pygame.K_UP] and chaser.y > chaser.vel:
        chaser.y -= chaser.vel
    if keys[pygame.K_DOWN] and chaser.y < (heightScreen - chaser.width - chaser.vel):
        chaser.y += chaser.vel

    # Fill screen in black  
    win.fill((0,0,0))
    # Draw rect
    pygame.draw.rect(win, (255, 0, 0), (chaser.x, chaser.y, chaser.width, chaser.height))
    runner.draw(win)
    pygame.display.update()

#End 
pygame.quit()

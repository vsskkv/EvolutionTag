#Date Created: 12/11/2020
#Author: Vikram Singh Kainth
#Title: Main file
#About: To be the main file where the program will initially run

#Imports
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
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

# Start state 
run = True

# Instaniate player(Chaser)
chaser = player(20, 20, 10, 10)

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
    pygame.display.update()

#End 
pygame.quit()

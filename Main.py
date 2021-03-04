#Date Created: 12/11/2020
#Author: Vikram Singh Kainth
#Title: Main file
#About: To be the main file where the program will initially run

#Imports
import pygame
pygame.init()

# Set window size + caption
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First game")

# Set player attributes 
x = 50
y = 50
width = 40
height = 60
vel = 5

# Start state 
run = True

# event loop to track game 
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #List
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    # Fill screen in black  
    win.fill((0,0,0))
    # Draw rect
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

#End 
pygame.quit()

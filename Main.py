#Date Created: 12/11/2020
#Author: Vikram Singh Kainth
#Title: Main file
#About: To be the main file where the program will initially run from

# Imports classes
import random
import pygame

# Import files
import runner
import chaser
import writeToExcel

# Start Pygames
pygame.init()

# Set window size + caption
widthScreen = 500
heightScreen = 500
win = pygame.display.set_mode((heightScreen, widthScreen))
pygame.display.set_caption("FYP")

# Timer
counter = 0

# lives
myLives = 100

# Arrays for counter
listCounter = []
            
# Start state 
run = True

# Instaniate player(Chaser)
# Starts at top left
chaser1 = chaser.chaserPlayer(40, 40, 10, 10, heightScreen, widthScreen)
# Start from bottom right 
# Instaniate player(Runner)
runner1 = runner.runnerPlayer(widthScreen - 40, heightScreen - 40, 10, 10, heightScreen, widthScreen)

# Main event loop to track game 
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill screen in black  
    win.fill((0,0,0))
    # Draw rect
    chaser1.draw(win)
    runner1.draw(win)

    # First pathfinding algorithum
    """ def SmartRandMove():
        if runner1.getX() < chaser1.x:
            chaser1.x -= chaser1.x
        else:
            chaser1.x += chaser1.x
        if runner1.getY() < chaser1.y:
            chaser1.y -= chaser1.y
        else:
            chaser1.x += chaser1.y """

    # Time
    counter = counter + 1

    if chaser1.rect.colliderect(runner1) and myLives > 0:
        # Instaniate player(Chaser)
        chaser1 = chaser.chaserPlayer(40, 40, 10, 10, heightScreen, widthScreen)
        # Instaniate player(Runner)
        runner1 = runner.runnerPlayer(widthScreen - 40, heightScreen - 40, 10, 10, heightScreen, widthScreen)
        # remove 1 life
        myLives = myLives - 1
        # add time to list
        listCounter.append(counter)
        counter = 0
        print(myLives) #remain
    if myLives == 0:
        print("Done!")
        run = False
        # make excel file
        writeToExcel.makeExcelFile(listCounter)

    pygame.display.update()

#End 
pygame.quit()
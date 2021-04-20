#Date Created: 12/11/2020
#Author: Vikram Singh Kainth
#Title: Main file
#About: To be the main file where the program will initially run from

# Imports classes
import random
import pygame

# Import files
import player
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
chaser1 = player.player(widthScreen - 40, heightScreen - 40, 10, 10, heightScreen, widthScreen, 0, 255, 0)

# Instaniate player(Runner)
runner = player.player(40, 40, 10, 10, heightScreen, widthScreen, 255, 0, 0)



# Event loop to track game 
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill screen in black  
    win.fill((0,0,0))
    # Draw rect
    chaser1.draw(win)
    runner.draw(win)

    # Time
    counter = counter + 1

    if chaser1.rect.colliderect(runner) and myLives > 0:
        print(counter)
        # Instaniate player(Chaser)
        chaser1 = player.player(widthScreen - 40, heightScreen - 40, 10, 10, heightScreen, widthScreen, 0, 255, 0)

        # Instaniate player(Runner)
        runner = player.player(40, 40, 10, 10, heightScreen, widthScreen, 255, 0, 0)
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
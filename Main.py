#Date Created: 12/11/2020
#Author: Vikram Singh Kainth
#Title: Main file
#About: To be the main file where the program will initially run

#Imports
import random
import pygame
import xlwt
pygame.init()

# Set window size + caption
widthScreen = 300
heightScreen = 300
win = pygame.display.set_mode((heightScreen, widthScreen))
pygame.display.set_caption("FYP")

# timer
counter = 0

# lives
myLives = 100

# Arrays for counter
listCounter = []

# player object 
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velx = 5
        self.vely = 5

    def draw(self, win):
        self.move()
        self.rect = pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))
    
    # Move the chaser around randomly     
    def move(self):
        rand = random.randint(1,4)
        if(rand == 1 and self.vely + self.y < heightScreen - 11):
            self.y += self.vely
        if(rand == 2 and self.velx + self.x < widthScreen - 11):
            self.x += self.velx
        if(rand == 3 and self.y - self.vely > 0):
            self.y -= self.vely
        if(rand == 4 and self.x - self.velx > 0):
            self.x -= self.velx

# chaser object 
class chaser(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velx = 5
        self.vely = 5

    def draw(self, win):
        self.move()
        self.rect = pygame.draw.rect(win, (255, 255, 0), (self.x, self.y, self.width, self.height))
    
    # Move the chaser around randomly     
    def move(self):
        rand = random.randint(1,4)
        if(rand == 1 and self.vely + self.y < heightScreen - 11):
            self.y += self.vely
        if(rand == 2 and self.velx + self.x < widthScreen - 11):
            self.x += self.velx
        if(rand == 3 and self.y - self.vely > 0):
            self.y -= self.vely
        if(rand == 4 and self.x - self.velx > 0):
            self.x -= self.velx
            
# Start state 
run = True

# Instaniate player(Chaser)
chaser1 = chaser(widthScreen - 40, heightScreen - 40, 10, 10)

# Instaniate player(Runner)
runner = player(40, 40, 10, 10)

book = xlwt.Workbook()
sheet1 = book.add_sheet("Random")

# Event loop to track game 
while run:
    #pygame.time.delay(100)

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
        chaser1 = chaser(widthScreen - 40, heightScreen - 40, 10, 10)
        # Instaniate player(Runner)
        runner = player(40, 40, 10, 10)
        # remove 1 life
        myLives = myLives - 1
        listCounter.append(counter)
        counter = 0
        print(myLives) #remain
    if myLives == 0:
        print("Over")
        run = False
        print(listCounter)
        

    pygame.display.update()

#End 
pygame.quit()
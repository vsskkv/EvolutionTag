# Author: Vikram Singh Kainth   
# Date: 11/12/2020
# Title: Main.py
# Descirption: displays the runs, all files converge here 

# import pygames libary 
import pygame

# import other py files in thie folder
from config import *
from player import *
from strategy import *
from time import sleep
#from pygame.constants import K_a, K_d, K_s, K_w

# class for the display screen
class Window():

    # chaser and player(runner) set to none
    chaser = None
    player = None

    # delay to see the motion play out, set 60 for real time
    delay_counter = 0
    # draw objects
    drawing = False

    # fucntions to initiate code
    # @parm self, width of screen, height of screen, title of project
    def __init__(self, width, height, title = "FYP"):
        #self initiate var to parameters 
        self.title = title
        self.width = width
        self.height = height
        # start pygames
        pygame.init()
        # set screen height and title
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        # set player and chaser objects to correct size and colour
        self.player = Player(self.win, 15*CUBE_SIZE, 15*CUBE_SIZE, CUBE_SIZE, CHASER_COLOR)
        self.chaser = Player(self.win, 2*CUBE_SIZE, 2*CUBE_SIZE, CUBE_SIZE, PLAYER_COLOR)
        # here you can change the alghoritm (change name only)
        self.chaser.strategy = Astar(self.win, self.chaser, self.player)
        #self.chaser.strategy = None # non stagergy 
        self.chaser.retarget()

    # function open events
    # @param self 
    def open(self):
        # run set to true to play game loop 
        run = True
        while run:
            pygame.time.Clock().tick(180)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if  not PLAYER_SPAWNS_RANDOMLY:
                    self.on_keys(event)
                    self.on_mouse(event)

            if PLAYER_SPAWNS_RANDOMLY:  
                if self.player.move_to_random_position():
                    self.chaser.retarget()
                
            if PLAYER_MOVES_RANDOMLY:
                if self.player.move_randomly():
                    self.chaser.retarget()

            if CHASER_MOVES_RANDOMLY:
                if self.chaser.move_randomly():
                    self.chaser.retarget()

            if CHASER_SPAWNS_RANDOMLY:
                if self.chaser.move_to_random_position():
                    self.chaser.retarget()
            self.render()

    def on_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_d:
                self.player.move_right()
                self.chaser.retarget()
            elif event.key == K_a:
                self.player.move_left()
                self.chaser.retarget()
            elif event.key == K_s:
                self.player.move_down()
                self.chaser.retarget()
            elif event.key == K_w:
                self.player.move_up()
                self.chaser.retarget()

    def on_mouse(self, event):
        LEFT = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT:
                self.drawing = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == LEFT:
                    self.drawing = False
                
        if event.type == pygame.MOUSEMOTION and self.drawing:
            x = event.pos[0] // self.chaser.size
            y = event.pos[1] // self.chaser.size
            self.chaser.strategy.obstacle[(x * self.chaser.size, y * self.chaser.size)] = 0

    def check_collision(self):
        chaser_rect = pygame.Rect(self.chaser.pos_x, self.chaser.pos_y, self.chaser.size, self.chaser.size)
        player_rect = pygame.Rect(self.player.pos_x, self.player.pos_y, self.player.size, self.player.size)
        if chaser_rect.colliderect(player_rect):
            mgr.capture()
            self.player.move_to_random_position(True)
    def render(self):
        self.win.fill((0, 0, 0))
        self.chaser.render(SHOW_SHORTEST_PATH)
        self.player.render()
        if self.chaser.strategy == None:
            self.check_collision()
        pygame.display.update()

if __name__ == "__main__":
    Window(500, 500).open()
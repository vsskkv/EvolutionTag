import pygame

from config import *
from random import randint, randrange

class Player():

    def __init__(self, win, x, y, size, color = (0, 0, 255), strategy = None):
        self.win = win
        self.pos_x = x
        self.pos_y = y
        self.size  = size
        self.color = color
        self.strategy = strategy

        self.delay_counter = 0

    def retarget(self):
        if self.strategy != None:
            self.strategy.retarget()
            self.strategy.find()

    def chase(self):
        if self.delay_counter >= DELAY:
            if len(self.strategy.path) != 0:
                path_cell = self.strategy.path.pop()
                if path_cell not in self.strategy.obstacle:
                    self.pos_x = path_cell[0]
                    self.pos_y = path_cell[1]
                    self.delay_counter = 0
                    mgr.runs += 1
                else:
                    self.retarget()
            else:
                self.strategy.player.move_to_random_position(True)
                self.retarget()
                mgr.capture()

        self.delay_counter += 1

    def move_up(self, by = VELOCITY):
        by = CUBE_SIZE * by
        if self.pos_y - by > 0:
            self.pos_y -= by
        else:
            self.pos_y = 0
        mgr.runs += 1

    def move_down(self, by = VELOCITY):
        by = CUBE_SIZE * by
        if self.pos_y + by < pygame.display.get_surface().get_height():
            self.pos_y += by
        else:
            self.pos_y = pygame.display.get_surface().get_height() - CUBE_SIZE
        mgr.runs += 1

    def move_right(self, by = VELOCITY):
        by = CUBE_SIZE * by
        if self.pos_x + by < pygame.display.get_surface().get_width():
            self.pos_x += by
        else:
            self.pos_x = pygame.display.get_surface().get_width()
        mgr.runs += 1

    def move_left(self, by = VELOCITY):
        by = CUBE_SIZE * by
        if self.pos_x - by > 0:
            self.pos_x -= by
        else:
            self.pos_x = 0
        mgr.runs += 1

    def move_to_random_position(self, without_delay = False):
        if self.delay_counter >= DELAY or without_delay:
            max_x = pygame.display.get_surface().get_width()  / CUBE_SIZE
            max_y = pygame.display.get_surface().get_height() / CUBE_SIZE
            self.pos_x = randint(0, max_x) * CUBE_SIZE
            self.pos_y = randint(0, max_y) * CUBE_SIZE
            self.delay_counter = 0
            mgr.runs += 1
            return True
        return False

    def move_randomly(self, without_delay = False):
        if self.delay_counter >= DELAY / 10 or without_delay:
            rand = randint(1,4)
            if(rand == 1 and VELOCITY + self.pos_y < pygame.display.get_surface().get_width()  - CUBE_SIZE):
                self.pos_y += VELOCITY * CUBE_SIZE
            if(rand == 2 and VELOCITY + self.pos_x < pygame.display.get_surface().get_height() - CUBE_SIZE):
                self.pos_x += VELOCITY* CUBE_SIZE
            if(rand == 3 and self.pos_y - VELOCITY > 0):
                self.pos_y -= VELOCITY* CUBE_SIZE
            if(rand == 4 and self.pos_x - VELOCITY > 0):
                self.pos_x -= VELOCITY* CUBE_SIZE
            self.delay_counter = 0
            mgr.runs += 1
            return True
        return False

    def render(self, with_path = False):
        if self.strategy != None:
            self.chase()
            self.strategy.render_blocked()
            if with_path:
                self.strategy.render_path()

        self.delay_counter += 1
        pygame.draw.rect(self.win, self.color, (self.pos_x, self.pos_y, self.size, self.size))

if __name__ == "__main__":
    print("Try main.py...")
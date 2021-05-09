# Author:
# Date:
# Title:
# Descirption: 
import pygame

from config import *
from c_queue import PriorityQueue

#This is the base strategy class, which contains the similar code for all pathfinding-algs
class Strategy():

    def __init__(self, win, chaser, player):
        self.win = win
        self.player = player
        self.chaser = chaser
        self.primitive_size = player.size
        self.goal  = (player.pos_x, player.pos_y)
        self.start = (chaser.pos_x, chaser.pos_y) 

        self.path = []
        self.obstacle = {}

    def find(self):
        raise NotImplementedError()

    def restore_path(self, current, came_from):
        path = []
        while not self.start == current:
            path.append(current)
            current = came_from[current]
        return path

    # Manhattan distance
    def heuristic(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def render_path(self, color = PATH_COLOR):
        for a in self.path:
            pygame.draw.rect(self.win, color, (a[0], a[1], CUBE_SIZE, CUBE_SIZE))

    def render_blocked(self, color = OBSTACLE_COLOR):
        for a in self.obstacle.keys():
            pygame.draw.rect(self.win, color, (a[0], a[1], CUBE_SIZE, CUBE_SIZE))

    def retarget(self):
        self.goal  = (self.player.pos_x, self.player.pos_y)
        self.start = (self.chaser.pos_x, self.chaser.pos_y) 

class Astar(Strategy):
   
    def __init__(self, win, chaser, player):
        super().__init__(win, chaser, player)

    def find(self):
        frontier = PriorityQueue()
        frontier.put(self.start, 0)

        came_from   = {}
        cost_so_far = {}

        came_from[self.start] = None
        cost_so_far[self.start] = 0

        self.path = []

        while not frontier.empty():
            current = frontier.get()

            if current == self.goal:
                self.path = self.restore_path(current, came_from)
                break

            for next in get_nears(current[0] // CUBE_SIZE, current[1] // CUBE_SIZE, CUBE_SIZE):
                if next not in self.obstacle:
                    new_cost = cost_so_far[current] + (1.4 if is_diagonal(next, current, CUBE_SIZE) else 1)
                    if next not in cost_so_far or new_cost < cost_so_far[next]:
                        cost_so_far[next] = new_cost
                        frontier.put(next, new_cost + self.heuristic(next, self.goal))
                        came_from[next] = current

# Jump point search - modification for A*
class JPS(Strategy):

    def __init__(self, win, chaser, player):
        self.width  = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        super().__init__(win, chaser, player)

    def find(self):
        self.path = []

        self.f = { self.start : 0 }
        self.g = { self.start : 0 }
        self.h = { self.start : 0 }

        self.opened = { self.start : 0}
        self.parent = { self.start : None}

        self.frontier = PriorityQueue()
        self.frontier.put(self.start, self.g[self.start] - self.f[self.start])

        while not self.frontier.empty():
            current = self.frontier.get()
            #del self.opened[current]

            if current == self.goal:
                self.path = self.restore_path(self.goal, None)

            self.identify_successors(current)

    def identify_successors(self, node):
        for near in self.find_neighbors(node):
            jump_point = self.jump(near, node)
            if jump_point:
                jx = jump_point[0]
                jy = jump_point[1]

                jump_node = (jx, jy)
                if jump_node not in self.opened:
                    next_g = self.g[node] + self.heuristic(jump_node, node)
                    if jump_node not in self.opened or next_g < self.g[jump_node]:
                        self.g[jump_node] = next_g
                        self.h[jump_node] = self.heuristic(jump_node, self.goal)
                        self.f[jump_node] = self.g[jump_node] + self.h[jump_node]
                        self.parent[jump_node] = node
                        
                        if jump_node not in self.opened:
                            self.frontier.put(jump_node, self.g[jump_node] - self.f[jump_node])
                            self.opened[jump_node] = 0
                        else:
                            for opened in self.frontier.data:
                                if opened[2] == jump_node:
                                    self.opened = (self.g[jump_node] - self.f[jump_node], jump_node)

    def jump(self, jump_to, jump_from):
        x = jump_to[0]
        y = jump_to[1]
        dx = x - jump_from[0]
        dy = y - jump_from[1]

        if not self.is_inside(jump_to):
            return None

        if self.is_obstacle(jump_to):
            return None

        if jump_to == self.goal:
            return jump_to

        # check for forced neighbors
        # along the diagonal
        if dx != 0 and dy != 0:
            if (self.is_inside((x - dx, y + dy)) and self.is_inside((x - dx, y)) or 
               (self.is_inside((x + dx, y - dy)) and self.is_inside((x, y - dy)))):
                return jump_to
            # when moving diagonally, must check for vertical/horizontal jump points
            if self.jump((x + dx, y), (x, y) or self.jump((x, y + dy), (x, y))):
                return jump_to
        # horizontally/vertically
        else:
            if dx != 0:
                if (self.is_inside((x + dx, y + CUBE_SIZE)) and self.is_inside((x, y + CUBE_SIZE)) or
                   (self.is_inside((x + dx, y - CUBE_SIZE)) and self.is_inside((x, y - CUBE_SIZE)))):
                    return jump_to
            if dy != 0:
                if (self.is_inside((x + CUBE_SIZE, y + dy)) and self.is_inside((x + CUBE_SIZE, y)) or
                   (self.is_inside((x - CUBE_SIZE, y + dy)) and self.is_inside((x - CUBE_SIZE, y)))):
                    return jump_to

        return self.jump((x + dx, y + dy), (x, y))

    def is_obstacle(self, node):
        return True if node in self.obstacle else False

    def is_inside(self, node):
        return True if possible_coordinate(self.width, node[0]) and possible_coordinate(self.height, node[1]) else False

    def restore_path(self, current, came_from):
        path = []
        while current != self.start:
            path.append(current)
            current = self.parent[current]
        return path

    def find_neighbors(self, node):
        parent = self.parent[node]
        x = node[0]
        y = node[1]
        neighbors = []

        # directed pruning: can ignore most neighbors, unless forced.
        if parent:
            px = parent[0]
            py = parent[1]

            # get the normalized direction of travel
            dx = int((x - px) / max(abs(x - px), CUBE_SIZE)) * CUBE_SIZE
            dy = int((y - py) / max(abs(y - py), CUBE_SIZE)) * CUBE_SIZE

            # search diagonally
            if dx != 0 and dy != 0:
                if self.is_inside((x, y + dy)):
                    neighbors.append((x, y + dy))

                if self.is_inside((x + dx, y)):
                    neighbors.append((x + dx, y))

                if self.is_inside((x + dx, y + dy)):
                    neighbors.append((x + dx, y + dy))

                if not self.is_inside((x - dx, y)):
                    neighbors.append((x - dx, y + dy))

                if not self.is_inside((x, y - dy)):
                    neighbors.append((x + dx, y - dy))

            # search horizontally/vertically
            else:
                if dx == 0:
                    if self.is_inside((x, y + dy)):
                        neighbors.append((x, y + dy))

                    if not self.is_inside((x + CUBE_SIZE, y)):
                        neighbors.append((x + CUBE_SIZE, y + dy))

                    if not self.is_inside((x - CUBE_SIZE, y)):
                        neighbors.append((x - CUBE_SIZE, y + dy))
                if dy == 0:
                    if self.is_inside((x + dx, y)):
                        neighbors.append((x + dx, y))

                    if not self.is_inside((x, y + CUBE_SIZE)):
                        neighbors.append((x + dx, y + CUBE_SIZE))

                    if not self.is_inside((x, y - CUBE_SIZE)):
                        neighbors.append((x + dx, y - CUBE_SIZE))

        # return all neighbors
        else:
            for near in get_nears(node[0] // CUBE_SIZE, node[1] // CUBE_SIZE, CUBE_SIZE):
                neighbors.append(near)

        return neighbors

class Dijkstra(Strategy):

    def __init__(self, win, chaser, player):
        super().__init__(win, chaser, player)

    def find(self):
        frontier = PriorityQueue()
        frontier.put(self.start, 0)

        came_from   = {}
        cost_so_far = {}

        came_from[self.start] = None
        cost_so_far[self.start] = 0

        self.path = []
        while not frontier.empty():
            current = frontier.get()

            if current == self.goal:
                self.path = self.restore_path(current, came_from)
                break

            for next in get_nears(current[0] // CUBE_SIZE, current[1] // CUBE_SIZE, CUBE_SIZE):
                if next not in self.obstacle:
                    new_cost = cost_so_far[current] + (1.4 if is_diagonal(next, current, CUBE_SIZE) else 1)
                    if next not in cost_so_far or new_cost < cost_so_far[next]:
                        cost_so_far[next] = new_cost
                        frontier.put(next, new_cost)
                        came_from[next] = current

def is_diagonal(first, second, size):
    return True if abs(first[0] - second[0]) + abs(first[1] - second[1]) == 2*size else False

#gets the nearest coordinates (x & y applied to grid) of the specified coordinates
def get_nears(x, y, size):
    width  = pygame.display.get_surface().get_width()
    height = pygame.display.get_surface().get_height()
    
    nears = []

    if possible_coordinate(width, (x-1)*size) and possible_coordinate(height, (y-1)*size):
        nears.append(((x-1)*size, (y-1)*size))

    if possible_coordinate(height, (y-1)*size):
        nears.append((x*size, (y-1)*size))
    
    if possible_coordinate(width, (x+1)*size) and possible_coordinate(height, (y-1)*size):
        nears.append(((x+1)*size,(y-1)*size))

    if possible_coordinate(width, (x+1)*size):
        nears.append(((x+1)*size,y*size))

    if possible_coordinate(width, (x+1)*size) and possible_coordinate(height, (y+1)*size):
        nears.append(((x+1)*size,(y+1)*size))

    if possible_coordinate(height, (y+1)*size):
        nears.append((x*size,(y+1)*size))

    if possible_coordinate(width, (x-1)*size) and possible_coordinate(height, (y+1)*size):
        nears.append(((x-1)*size, (y+1)*size))

    if possible_coordinate(width, (x-1)*size):
        nears.append(((x-1)*size,y*size))

    return nears

#screen_scale - width/height of the window
#checks if the current coordinate is invalid (in bounds of screen)
def possible_coordinate(screen_scale, coordinate):
    return True if coordinate >= 0 and coordinate < screen_scale else False

if __name__ == "__main__":
    print("Try main.py...")
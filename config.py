# Author: Vikram singh kainth  
# Date: 30/03/2021
# Title: config.py
# Descirption: config the file to the user usecase 

#import excel file
import excel
# !!! If you want to change the strategy (alg), open main.py, and look at 27th line !!!

# the delay with which the chaser takes one step (each N screen redrawings)
# also used for delay between different random jumps
DELAY = 0
# player's velocity (in CUBE_SIZES)
VELOCITY  = 1 
CUBE_SIZE = 20
 
# 255 bit colour
PLAYER_COLOR   = (255, 0, 0)
CHASER_COLOR   = (0, 255, 0)
PATH_COLOR     = (255, 255, 0)
OBSTACLE_COLOR = (32, 32, 32)

# set to true if you want the player & chase to spawn randomly
PLAYER_SPAWNS_RANDOMLY = False
CHASER_SPAWNS_RANDOMLY = False

#for full random also set the None strategy
PLAYER_MOVES_RANDOMLY = True
CHASER_MOVES_RANDOMLY = True

# shows the shortest path between chaser and player 
SHOW_SHORTEST_PATH = True

mgr = excel.Manager() 

# incase user runs this file
if __name__ == "__main__":
    print("Try main.py...")
#Date Created: 12/11/2020
#Author: Vikram Singh Kainth
#Title: Main file
#About: To be the main file where the program will initially run

# define the row = 10 and cols = 10, so 100 square grid
rows, cols = (10, 10)

# make grid
grid = [[" " for i in range(cols)] for j in range(rows)]

# Add the Tagger
grid[0][0] = "T"

# Add Runner
grid[9][9] = "R"

#display grid in terminal
for row in grid:
    print(row)
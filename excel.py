# Author:
# Date:
# Title:
# Descirption: 
import xlwt

from datetime import datetime

class Manager():

    def __init__(self):
        self.data = []
        self.lifes = 100
        self.reset()

    def reset(self):
        self.runs = 0
        self.time = datetime.now()
        self.lifes -= 1
        if self.lifes <= 0:
            write(self.data)
            exit()

    def capture(self):
        self.data.append((self.runs, datetime.now() - self.time))
        self.reset()

def write(data):
    workbook = xlwt.Workbook()
    main_sheet = workbook.add_sheet("Main", cell_overwrite_ok=True)
    main_sheet.write(0, 0, "  N  ")
    main_sheet.write(0, 1, "Runs")
    main_sheet.write(0, 2, "Time")

    for i in range(len(data)):
            main_sheet.write(1+i, 0, str(i+1))
            main_sheet.write(1+i, 1, data[i][0])
            main_sheet.write(1+i, 2, str(round(data[i][1].total_seconds()))+".s")

    workbook.save('Runs.xls')
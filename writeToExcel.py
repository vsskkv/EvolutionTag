#Date Created: 12/11/2020
#Author: Vikram Singh Kainth
#Title: Main file
#About: To be the main file where the program will initially run from

# Import
import xlwt

# Make and write to excel file 
class main(object):
    def makeExcelFile(listcounter):
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet("Random", cell_overwrite_ok=True)
        row = 2
        sheet1.write(1, 1, "Run number")
        sheet1.write(1, 2, "Time")
        while(row < 100):
            col = 0
            sheet1.write(row, col, "col")
            col = col + 1
            sheet1.write(row, col, listcounter[row])
            row = row + 1
        workbook.save('Runs.xls')
        

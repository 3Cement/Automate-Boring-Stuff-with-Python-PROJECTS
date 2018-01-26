#! python3
# spreadsheet_cell_iverter.py - Open spreadsheet and invert row and column of the cells in the spreadsheet.

import time, openpyxl, os

start_time = time.time()
os.chdir("C:\\Users\\JOHN\\MYPYTHONSCRIPTS")

print('Opening workbook...')
fileName = "example1.xlsx"
wb = openpyxl.load_workbook('example1.xlsx')
sheet = wb.get_active_sheet()

newFileName = "example1Inverted.xlsx"
output = openpyxl.Workbook()
outputsheet = output.get_active_sheet()
print('Inverting columns and rows...')
for x in range(1, sheet.max_row+1):
	for y in range(1, sheet.max_column+1):
		outputsheet.cell(row=y, column=x).value = sheet.cell(row=x, column=y).value

output.save(newFileName)
print('File saved!')

try:
	print('Oppening excel file...')
	file = os.startfile(newFileName)
except Exception as exc:
	print('There was a problem: %s' % (exc))

end_time = time.time()
print("\n--- %s seconds ---" % round((end_time - start_time),2))

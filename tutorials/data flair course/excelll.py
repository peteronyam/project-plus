# from openpyxl import workbook, load_workbook, Workbook
#
# # wb = load_workbook('students docs.xlsx')
# # ws = wb.active
# # print(ws['A3'].value)
# # # to edit a value inside a cell
# # ws['A2'].value = 1
# # ws['B1'].value = "S.NAMES"
# # # wb.save('students docs.xlsx')
# # # accessing a specific sheet
# # ws = wb['students docs']
# # print(wb['students docs'])
# # # to add sheets to an excel file
# # wb.create_sheet("assignment")
# # print(wb.sheetnames)
# # creating a new workbook
# from openpyxl import workbook
# wb = Workbook()
# ws = wb.active
# ws.title = "Time"
#
# ws.append(['tin', 'is', 'kind'])
# ws.append(['tin', 'is', 'kind'])
# ws.append(['tin', 'is'])
# ws.append(['tin', 'is', 'kind'])
# ws.append(['tin', 'is', 'kind', 'tin', 'is', 'kind'])
# ws.append(['tin', 'is', 'kind'])
# ws.append(['tin', 'is', 'kind', 'tin', 'is', 'kind'])
#
# wb.save('Time.xlsx')

# looping through a cell
from openpyxl import load_workbook
# from openpyxl.utils import get_column_letter
# from tabulate import tabulate

wb = load_workbook('students doc.xlsx')
ws = wb.active
# for row in range(1,11):
#     for col in range(1, 4):
#         # char = chr(65 + col)
#         char = get_column_letter(col)
#         ws[char + str(row)] = char + str(row)
# to insert rows and col
ws.insert_rows(3)

ws['C3'].value = "teams coad"
ws['D3'].value = 68
ws['E3'].value = "B"
wb.save('student doc.xlsx')
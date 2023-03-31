from openpyxl import workbook
from openpyxl import load_workbook

wb = load_workbook('sample offset table.xlsx')
worksheet = wb.active
stations = []
offsetTable = []

for i, row in enumerate(worksheet['A'][1:]):
    stations.append(row.value)
    offsetTable.append([])
    for column in worksheet[i+2][1:]:
        offsetTable[i].append(column.value)

print(stations)
print(offsetTable)

wb.close()


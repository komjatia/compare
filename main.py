import csv
from openpyxl import load_workbook

workbook = load_workbook('Missing L1 FA.xlsx')
sheet = workbook.active
rows = sheet.rows
headers = [cell.value for cell in next(rows)]
data = []
exported = []
with open('export.csv', 'r', encoding='utf-8', newline='') as export:
    reader = csv.reader(export, delimiter=';')
    header = next(reader)
    index_of = header.index('Serial Number')
    for line in reader:
        exported.append(line[index_of])
    for row in rows:
        for title, cell in zip(headers, row):
            if cell.value not in exported and title == 'FAIL CT':
                if cell.value is not None:
                    print(f"not found {cell.value}")

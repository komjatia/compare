import csv
from openpyxl import load_workbook

missing_L1 = "Missing L1 FA.xlsx"
export_x="export.csv"

workbook = load_workbook(missing_L1)
sheet = workbook.active
rows = sheet.rows
headers = [cell.value for cell in next(rows)]
data = []
exported = []
with open(export_x, 'r', encoding='utf-8', newline='') as export:
    reader = csv.reader(export)
    header = next(reader)
		# print("dsa")
    index_of = header.index('Serial number')
    for line in reader:
        exported.append(line[index_of])
    for row in rows:
        for title, cell in zip(headers, row):
            if cell.value not in exported and title == 'FAIL CT':
                if cell.value is not None:
                    print(f"not found {cell.value}")

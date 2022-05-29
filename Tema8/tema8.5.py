import xlsxwriter
import catalog

ctlg = catalog.citeste_catalogul('note.txt')
# print(ctlg)

workbook = xlsxwriter.Workbook('medii.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 50)

bold = workbook.add_format({'bold': True})

right = workbook.add_format()
right.set_align('right')

bold_right = workbook.add_format({'bold': True})
bold_right.set_align('right')

worksheet.write('A1', 'Elev', bold)
worksheet.write('B1', 'Media', bold_right)

row = 1

for k, v in sorted(ctlg.items()):
    worksheet.write(row, 0, k)
    med = f"{catalog.media(v):.2f}"
    worksheet.write(row, 1, med, right)
    row += 1

workbook.close()

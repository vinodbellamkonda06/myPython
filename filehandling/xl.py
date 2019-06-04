import xlrd

book = xlrd.open_workbook(r"C:\Users\Jagadeesh\Desktop\Book2.xlsx")
sheet = book.sheet_by_index(0)
for i in range(sheet.nrows):
    data = sheet.row_values(i)
    print(data)


#print(data)
#print(sheet)
#print(sheet.nrows)
#print(sheet.ncols)

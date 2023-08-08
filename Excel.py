# Excel.py
import os
import win32com.client as win32

excel = win32.Dispatch("Excel.Application")
excel.Visible = True

workbook = excel.Workbooks.Add()
workbook.SaveAs(os.path.join(os.getcwd(), "file.xlsx"))
ws = workbook.Sheets("Sheet1")

excel.ActiveWorkbook.Save()
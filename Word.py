# Word.py
import os
import win32com.client as win32

word = win32.Dispatch('Word.Application')
word.Visible = True

# Create a new document
doc = word.Documents.Add()

# Add a table with 5 rows and 9 columns
num_rows = 9
num_columns = 5
table = doc.Tables.Add(doc.Range(0, 0), num_rows, num_columns)

# Set table style and format
table.Style = 'Table Grid'
table.Borders.Enable = True  # Enable borders for the table

# Set the header row title
header_row = table.Rows[1]  # First row is the header row
header_row.Cells[1].Merge(header_row.Cells[num_columns])
header_row.Cells[1].Range.Text = "Table Header Title"
header_row.Cells[1].Range.ParagraphFormat.Alignment = win32.constants.wdAlignParagraphCenter

# Populate the table cells
for row in range(num_rows):
    for col in range(num_columns):
        cell = table.Cell(row + 2, col + 1)  # Rows shifted by 1 due to header
        cell.Range.Text = f"Row {row+1}, Col {col+1}"


# Save a new document
doc.SaveAs('test.docx')
import camelot
import pandas as pd

def pdf_to_excel(pdf_path, output_excel_path):
    # Read tables from PDF
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')

    # Process each table
    processed_data = [table.df for table in tables]

    # Concatenate all tables
    full_data = pd.concat(processed_data, ignore_index=True)

    # Add a 'Status' column based on marks
    def determine_status(row):
        for col in row.index:
            if col != 'Name':
                try:
                    mark = float(row[col])
                    if mark < 40:
                        return 'Fail'
                except ValueError:
                    continue
        return 'Pass'
    
    full_data['Status'] = full_data.apply(determine_status, axis=1)

    # Save to Excel
    full_data.to_excel(output_excel_path, index=False)
    return full_data

# Placeholder paths (replace with actual paths)
pdf_path = 'path_to_pdf.pdf'
output_excel_path = 'output.xlsx'

# Convert PDF to Excel
result_df = pdf_to_excel(pdf_path, output_excel_path)
result_df.head()


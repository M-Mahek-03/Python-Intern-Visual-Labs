import pdfplumber
import pandas as pd

def extract_pdf_to_dataframe(pdf_path):
    data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    data.append(row)
    df = pd.DataFrame(data[1:], columns=data[0])  # Assuming the first row is the header
    return df

if __name__ == "__main__":
    pdf_path = 'path_to_your_pdf.pdf'
    df = extract_pdf_to_dataframe(pdf_path)
    df.to_excel('output.xlsx', index=False)

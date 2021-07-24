import pandas as pd

first_sheet = 'Sheet1'
practice_file = "/Users/jenniferwang/data-ingestion/PracticeData.xlsx"

df = pd.read_excel(practice_file, sheet_name = first_sheet)

print(df.head())
# imports (aka deps)
import pandas as pd
import sqlite3

# global variables
practice_file = "/Users/jenniferwang/data-ingestion/PracticeData.xlsx"

def readSheet(file, sheet='Sheet1'):
    excel = pd.read_excel(practice_file, sheet_name = sheet)
    return excel.head()

print(readSheet(practice_file))

# Write to sqlite

#    Title   Id   shape
# 0    Red  1.0  circle
# 1  Green  2.0  circle
# 2   Blue  3.0  circle
# 3    Red  4.0  circle
# 4  Green  5.0  circle

con = sqlite3.connect('data-integration.db')

# Create Table

create_table_sql_statement = """CREATE TABLE IF NOT EXISTS shapes (
	id integer PRIMARY KEY,
	title text NOT NULL,
	shape text NOT NULL
);"""

def executeSql(conn, statement):
    c = conn.cursor()
    c.execute(statement)

executeSql(con, create_table_sql_statement)
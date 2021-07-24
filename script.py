# imports (aka deps)
import pandas as pd
import sqlite3

# global variables
practice_file = "/Users/jenniferwang/data-ingestion/PracticeData.xlsx"

def readSheet(file, sheet='Sheet1'):
    excel = pd.read_excel(practice_file, sheet_name = sheet)
    rows = []
    for _, row in excel.iterrows():
        rows.append(row)
    return rows


# Write to sqlite

#    Title   Id   shape
# 0    Red  1.0  circle
# 1  Green  2.0  circle
# 2   Blue  3.0  circle
# 3    Red  4.0  circle
# 4  Green  5.0  circle

con = sqlite3.connect('data-integration.db')

# Create Table

create_table_sql_statement = """CREATE TABLE IF NOT EXISTS example (
	id integer PRIMARY KEY,
	title text NOT NULL
);"""

def executeSql(conn, statement):
    try:
        c = conn.cursor()
        c.execute(statement)
        conn.commit()
    except Exception as exception:
        print(exception)

executeSql(con, create_table_sql_statement)

# Read Each line from excel, then insert into our db
def insertRows(rows, conn):
    for row in rows:
        insert_row_sql_statement = "INSERT INTO example (id, title) VALUES ({id}, \"{title}\");".format(id=row.Id, title=row.Title)
        print(insert_row_sql_statement)
        executeSql(conn, insert_row_sql_statement)

all_rows = readSheet(practice_file)
insertRows(all_rows, con)
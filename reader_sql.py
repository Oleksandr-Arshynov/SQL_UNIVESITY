import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('/Users/oleksandrarshinov/Desktop/Documents/Repository/SQL_UNIVESITY/university.db')
cursor = conn.cursor()

with open('query_addition_1.sql', 'r') as file:
    sql_query = file.read()

cursor.execute(sql_query)

results = cursor.fetchall()

for row in results:
    print(row)

conn.close()

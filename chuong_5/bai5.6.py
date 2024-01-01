import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM example_table")
rows = cursor.fetchall()
for row in rows:
    print(row)
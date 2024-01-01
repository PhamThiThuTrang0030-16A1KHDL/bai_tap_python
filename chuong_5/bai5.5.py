# hiển thị các bản ghi
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
# cursor.execute('INSERT INTO example_table (id, name, age) VALUES (2, "Sam", 27)')
cursor.execute("SELECT * FROM example_table")
conn.commit()
result = cursor.fetchall()
for row in result:
    print(row)
cursor.close()
conn.close()
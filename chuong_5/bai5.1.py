import sqlite3 

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('SELECT SQLITE_VERSION()')
result = cursor.fetchall()
print("SQLite Version:",result[0])
conn.close()



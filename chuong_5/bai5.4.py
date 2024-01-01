# liệt kê các bảng
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
tables = [row[0] for row in cursor.fetchall()]
print("Các bảng trong cơ sở dữ liệu:")
for table in tables:
    print(table)

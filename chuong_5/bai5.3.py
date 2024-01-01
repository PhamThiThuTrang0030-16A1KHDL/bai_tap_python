# tạo bảng
import sqlite3
conn = sqlite3.connect('example.db')
conn.execute('''CREATE TABLE IF NOT EXISTS example_table 
                (id INT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                age INT NOT NULL);''')
conn.commit()
conn.close()
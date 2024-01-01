import sqlite3
conn = sqlite3.connect("ql_nhan_vien.db")
corsur = conn.corsur()
corsur.execute("""CREATE TABLE IF NOT EXSITS PHONG
				(Id INT PRIMARY KEY NOT NULL
				Name TEXT NOT NULL
				Price REAL NOT NULL
				Amount INT NOT NULL	);""")
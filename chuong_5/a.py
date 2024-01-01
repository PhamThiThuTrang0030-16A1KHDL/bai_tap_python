import sqlite3
conn = sqlite3.connect("product.db")
cursor = conn.cursor()
cursor.execute("""SELECT * FROM product_table""")
a = cursor.fetchall()
for i in a:
    print(a)
print(len(a))
conn.commit()
conn.close()

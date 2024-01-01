import sqlite3


def delete(database_name, table_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    delete_row = f"DELETE FROM {table_name} WHERE id = {int(input('Nhập id muốn xóa:'))}"
    cursor.execute(delete_row)
    conn.commit()
delete('example.db', 'example_table')

import sqlite3


def update_table(database_name, table_name, column_name, new_value):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    update_query = f"UPDATE {table_name} SET {column_name} = ?"
    cursor.execute(update_query, (new_value,))
    conn.commit()
    conn.close()


update_table('example.db', 'example_table', 'age', 20)

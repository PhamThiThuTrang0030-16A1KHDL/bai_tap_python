import sqlite3
def show_menu():
    print("Main Menu")
    print("------------------------------------------")
    print("|1. Hiển thị danh sách sản phẩm          |")
    print("|2. Thêm sản phẩm                        |")
    print("|3. Tìm kiếm thông tin sản phẩm theo tên |")
    print("|4. Cập nhập sản phẩm                    |")
    print("|5. Xóa sản phẩm                         |")
    print("------------------------------------------")

def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    choice = int(choice)
    return choice

def show_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_product(conn):
    cursor = conn.cursor()
    cursor.execute("Select * from product_table")
    rows = cursor.fetchall()
    id = len(rows) +1
    name = input("Nhập tên sản phẩm muốn thêm:")
    price = float(input("Nhập giá cho sản phẩm:"))
    amount = int(input("nhập số lượng sản phẩm:"))
    cursor.execute("INSERT INTO product_table VALUES (?,?,?,?)",(id,name,price,amount))
    conn.commit()
    
def search_by_name(conn):
    cursor = conn.cursor()
    name = input('Nhập tên sản phẩm muốn tìm: ')
    cursor.execute("Select * from product_table where name = ?", (name,))
    rows = cursor.fetchall()
    print(rows)

def update_product(conn):
    cursor = conn.cursor()
    id = int(input("Nhập id muốn sửa: "))
    price = float(input("Nhập đơn giá mới: "))
    amount = int(input("Nhập số lượng của sản phẩm: "))
    cursor.execute("UPDATE product_table SET price = ?, amount = ? where id = ?",(price,amount,id))
    conn.commit()

def delete_product(conn):
    cursor = conn.cursor()
    id = int(input("Nhập id muốn xóa: "))
    cursor.execute("DELETE FROM product_table where id = ?",(id,))
    conn.commit()

def main():
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.fetchall()
    while True:
        show_menu()
        choice = select_in_range("Select an option(1-5): ", 1, 5)
        if choice == 1:
            show_products(conn)
            input("\nPress Enter to continue.\n")
        elif choice == 2:
            add_product(conn)
            input("\nPress Enter to continue.\n")
        elif choice == 3:
            search_by_name(conn)
            input("\nPress Enter to continue.\n")
        elif choice == 4:
            update_product(conn)
            input("\nPress Enter to continue.\n")
        elif choice == 5:
            delete_product(conn)
            input("\nPress Enter to continue.\n")
main()

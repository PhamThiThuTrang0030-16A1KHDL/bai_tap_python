class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, a, b):
        super().__init__(0, 0)
        self.a = a
        self.b = b

    def dien_tich(self):
        return 3.14159265359 * self.a * self.b

class DuongTron(Elip):
    def __init__(self, r):
        super().__init__(r, r)

a = float(input("Nhập chiều dài trục lớn của elip: "))
b = float(input("Nhập chiều dài trục nhỏ của elip: "))
r = float(input('nhập cạnh hình tròn:'))


elip = Elip(a, b)
duong_tron = DuongTron(r)
print(f"Diện tích của elip là {elip.dien_tich()}")
print(f"Diện tích của đường tròn là {duong_tron.dien_tich()}")

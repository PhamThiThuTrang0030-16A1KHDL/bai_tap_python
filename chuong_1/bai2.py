class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm môn Toán: "))
        self.diem_ly = float(input("Nhập điểm môn Lý: "))
        self.diem_hoa = float(input("Nhập điểm môn Hoá: "))

    def in_thong_tin(self):
        print(f"Họ tên thí sinh: {self.ho_ten}")
        print('tổng điểm:',self.tinh_tong_diem())
        # print(f"Điểm môn Toán: {self.diem_toan}")
        # print(f"Điểm môn Lý: {self.diem_ly}")
        # print(f"Điểm môn Hoá: {self.diem_hoa}")

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

n = int(input("Nhập số lượng thí sinh: "))
danh_sach_thi_sinh = []
for i in range(n):
    ts = TS("", 0, 0, 0)
    ts.nhap_thong_tin()
    danh_sach_thi_sinh.append(ts)

print("\nDanh sách thí sinh trúng tuyển:")
danh_sach_trung_tuyen = []
for ts in danh_sach_thi_sinh:
    if ts.tinh_tong_diem() >= 20:
        danh_sach_trung_tuyen.append(ts)

danh_sach_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)

for ts in danh_sach_trung_tuyen:
    ts.in_thong_tin()





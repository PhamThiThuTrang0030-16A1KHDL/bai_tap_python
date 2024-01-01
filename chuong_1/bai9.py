class da_giac:
    def __init__(self, so_canh):
        self.so_canh = so_canh

class hinh_binh_hanh(da_giac):
    def __init__(self, canh_day, chieu_cao):
        super().__init__(4)
        self.canh_day = canh_day
        self.chieu_cao = chieu_cao

    def chu_vi(self):
        return (self.canh_day + self.chieu_cao) * 2

    def dien_tich(self):
        return self.canh_day * self.chieu_cao

class hinh_chu_nhat(hinh_binh_hanh):
    def __init__(self, canh_day, chieu_cao):
        super().__init__(canh_day, chieu_cao)

class hinh_vuong(hinh_chu_nhat):
    def __init__(self, canh):
        super().__init__(canh, canh)


canh_day = float(input("Nhập chiều dài cạnh đáy của hình bình hành: "))
chieu_cao = float(input("Nhập chiều cao của hình bình hành: "))
chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
canh = float(input("Nhập chiều dài cạnh của hình vuông: "))


binh_hanh = hinh_binh_hanh(canh_day, chieu_cao)
chu_nhat = hinh_chu_nhat(chieu_dai, chieu_rong)
vuong = hinh_vuong(canh)


print(f"Chu vi của hình bình hành là {binh_hanh.chu_vi()}")
print(f"Diện tích của hình bình hành là {binh_hanh.dien_tich()}")
print(f"Chu vi của hình chữ nhật là {chu_nhat.chu_vi()}")
print(f"Diện tích của hình chữ nhật là {chu_nhat.dien_tich()}")
print(f"Chu vi của hình vuông là {vuong.chu_vi()}")
print(f"Diện tích của hình vuông là {vuong.dien_tich()}")


        
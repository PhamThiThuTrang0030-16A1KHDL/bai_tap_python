class TamGiac:
    def __init__(self, canh_1, canh_2, canh_3):
        self.canh_1 = canh_1
        self.canh_2 = canh_2
        self.canh_3 = canh_3

    def chu_vi(self):
        return self.canh_1 + self.canh_2 + self.canh_3

    def dien_tich(self):
        p = self.chu_vi() / 2
        return (p * (p - self.canh_1) * (p - self.canh_2) * (p - self.canh_3)) ** 0.5


class TamGiacVuong(TamGiac):
    def __init__(self, canh_1, canh_2,):
        super().__init__(canh_1, canh_2, (canh_1**2 + canh_2**2) ** 0.5)


class TamGiacCan(TamGiac):
    def __init__(self, canh):
        super().__init__(canh, canh, canh)


class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh)

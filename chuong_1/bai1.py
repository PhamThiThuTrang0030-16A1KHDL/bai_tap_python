class HinhChuNhat:

    def __init__(self):
        self.dai = float(input('nhập cạnh dài: '))
        self.rong = float(input('nhập cạnh rộng: '))

    def chuVi(self):
        self.chuVi = (self.dai + self.rong) * 2

    def dienTich(self):
        self.dienTich = self.dai * self.rong

    def Out(self):
        print('chu vi của hình chữ nhật: ',self.chuVi)
        print('diện tích của hình chữ nhật: ',self.dienTich)

obj1 = HinhChuNhat()
obj1.chuVi()
obj1.dienTich()
obj1.Out()

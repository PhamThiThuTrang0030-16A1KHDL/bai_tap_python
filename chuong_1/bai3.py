class PS:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input('nhập tử số: '))
        self.mau_so = int(input('nhập mẫu số: '))

    def in_phan_so(self):
        print(str(self.tu_so),'/',str(self.mau_so))

ps = PS(0, 0)
ps.nhap_phan_so()

if ps.kiem_tra_hop_le():
    ps.in_phan_so()
else:
    print('phân số không hợp lệ')

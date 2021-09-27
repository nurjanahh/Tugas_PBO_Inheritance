class hewan:
    def __init__(self, warna, umur, berat):
        self.warna = warna
        self.umur = umur
        self.berat = berat
        
    def printname(self):
        print(self.warna)
        print(self.umur)
        print(self.berat)

class kucing(hewan):
    def __init__(self, warna, umur, berat):
          hewan.__init__(self, warna, umur, berat)
          self.jenis = "Anggora"

    def tampilankucing(self):
        print("Jenis kucing  : ", self.jenis)
        print("Warna         : ", self.warna)
        print("Umur          : ", self.umur)
        print("Berat         : ", self.berat)

class kelinci(hewan):
    def __init__(self, warna, umur, berat):
          hewan.__init__(self, warna, umur, berat)
          self.jenis = "lokal"

    def tampilankelinci (self):
        print("Jenis kelinci : ", self.jenis)
        print("Warna         : ", self.warna)
        print("Umur          : ", self.umur)
        print("Berat         : ", self.berat)

x = kucing("putih", "1,2 bulan", "1,5 kg")
y = kelinci("coklat", "3 bulan", "2 kg")
z = kucing("hitam", "3 bulan", "4 kg")

x.tampilankucing()
print("========================")
y.tampilankelinci()
print("========================")
z.tampilankucing()

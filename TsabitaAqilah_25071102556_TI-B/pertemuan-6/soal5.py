class Film:
    def tampilkan(self, judul, harga):
        self.judul = judul
        self.harga = harga
        print(f'{judul}, - Rp {harga}')

class Transaksi (Film):
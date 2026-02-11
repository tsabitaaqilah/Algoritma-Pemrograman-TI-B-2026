import myOOP 

tv = myOOP.ProdukElektronik("TV", "3.000.000", 2)
roti = myOOP.ProdukMakanan("Roti", "15.000", "12-12-2026")

print(tv.info_produk())
print(roti.info_produk())

notifikasi_email = myOOP.Email()
notifikasi_sms = myOOP.SMS()

print(notifikasi_email.kirim())
print(notifikasi_sms.kirim())

mahasiswa = myOOP.Mahasiswa()

mahasiswa.set_nilai(100)
print("Nilai Mahasiswa:", mahasiswa.get_nilai())

print(mahasiswa.set_nilai(200))  
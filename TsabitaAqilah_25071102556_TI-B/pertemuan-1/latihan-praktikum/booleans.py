# Boolean = tipe data logika
# Hanya punya dua nilai: True dan False
# Tapi penggunaannya LUAS banget di Python

# BOOLEAN ITU SEBENARNYA TURUNAN DARI INTEGER
# True bernilai 1, False bernilai 0 dalam operasi matematika

print(True + True)     # 2  -> 1 + 1
print(True + False)    # 1  -> 1 + 0
print(False * 10)      # 0

# Bisa dipakai dalam perhitungan (tapi jarang dipakai sengaja)
nilai = 95
bonus = True  # dianggap 1
print(nilai + bonus)  # 96

# PERBANDINGAN BERANTAI (CHAINED COMPARISON)
# Python bisa membandingkan banyak nilai sekaligus
umur = 18

print(18 <= umur <= 60)  # True  -> umur di antara 18 dan 60
print(umur < 10 < 30)    # False -> 20 < 10 itu sudah False

# PERBEDAAN == DAN is
# == membandingkan NILAI
# is membandingkan IDENTITAS OBJEK (lokasi memori)
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True  -> isinya sama
print(a is b)  # False -> objek berbeda di memori

c = a
print(a is c)  # True  -> menunjuk ke objek yang sama

# TRUTHY vs FALSY (lebih dalam)
# Truthy = dianggap True
# Falsy  = dianggap False
data = [1, 2, 3]

if data:  # tidak perlu tulis if len(data) > 0
    print("List ada isinya")  # karena list tidak kosong = True

data_kosong = []

if not data_kosong:
    print("List kosong")  # karena list kosong = False

# SHORT-CIRCUIT LOGIC (PENTING BANGET)
# Python berhenti mengevaluasi kalau sudah tahu hasilnya
def halo():
    print("Fungsi dijalankan")
    return True

print(True or halo())  
# halo() TIDAK dijalankan karena True or apapun = True

print(False and halo())
# halo() TIDAK dijalankan karena False and apapun = False

print(True and halo())
# halo() dijalankan karena perlu cek sisi kanan

# BOOLEAN DENGAN STRING & ANGKA
nama = "Bita"

if nama:  # sama seperti if bool(nama)
    print("Nama tersedia")

saldo = 0
if not saldo:
    print("Saldo kosong")

# OPERATOR PERBANDINGAN LENGKAP
print(5 != 3)   # True  -> tidak sama dengan
print(5 >= 5)   # True
print(4 <= 2)   # False

# MEMBERSHIP OPERATOR (HASILNYA BOOLEAN)
buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)        # True
print("pisang" in buah)      # False
print("pisang" not in buah)  # True

# BOOLEAN PADA FUNGSI DENGAN RETURN KONDISI
def is_genap(angka):
    return angka % 2 == 0  # langsung True/False

print(is_genap(4))  # True
print(is_genap(7))  # False

# MENGGUNAKAN BOOLEAN UNTUK FILTER DATA
angka_list = [1, 2, 3, 4, 5, 6]

# Simpan hanya angka genap
genap = []
for a in angka_list:
    if a % 2 == 0:   # kondisi boolean
        genap.append(a)

print(genap)  # [2, 4, 6]

# BOOLEAN DI LIST COMPREHENSION
# Lebih ringkas dari loop biasa
genap_lagi = [a for a in angka_list if a % 2 == 0]
print(genap_lagi)

# BOOLEAN SEBAGAI FLAG
login = True

if login:
    print("Akses diberikan")
else:
    print("Silakan login dulu")

# VALIDASI INPUT MENGGUNAKAN BOOLEAN
password = "12345"

valid = len(password) >= 8
print(valid)  # False karena kurang dari 8 karakter

# BOOLEAN DARI PERBANDINGAN STRING
print("apel" == "apel")   # True
print("Apel" == "apel")   # False (case-sensitive)



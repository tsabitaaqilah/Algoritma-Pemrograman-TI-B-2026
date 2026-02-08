# PYTHON VARIABLES
# Variabel adalah tempat untuk menyimpan data
nama = "Bita"
umur = 18

print(nama)
print(umur)

# PYTHON TIDAK PERLU DEKLARASI TIPE DATA
# Tipe data ditentukan otomatis saat diberi nilai

x = 10        # x bertipe int
x = "Halo"    # sekarang x berubah jadi string
print(x)

# CASTING (MENENTUKAN TIPE DATA SECARA MANUAL)
a = str(25)     # jadi string "25"
b = int(25)     # jadi integer 25
c = float(25)   # jadi float 25.0

print(a, b, c)

# ASSIGN BANYAK VARIABEL SEKALIGUS
buah1, buah2, buah3 = "Apel", "Mangga", "Jeruk"
print(buah1, buah2, buah3)

# SATU NILAI UNTUK BANYAK VARIABEL
a = b = c = 50
print(a, b, c)

# UNPACK COLLECTION
warna = ["Merah", "Hijau", "Biru"]
w1, w2, w3 = warna
print(w1, w2, w3)

# OUTPUT VARIABEL
bahasa = "Inggris"
selama = 2

print("Saya belajar bahasa", bahasa)
print("dalam waktu:", selama, "tahun")

# Gabung pakai +
kata1 = "Belajar "
kata2 = "bahasa"
print(kata1 + kata2)

# Untuk angka, + berarti penjumlahan
angka1 = 5
angka2 = 10
print(angka1 + angka2)

# Tidak bisa gabung string + angka langsung
# print("Umur " + 20)  # ERROR

print("Umur", 20)  # Cara yang benar

# GLOBAL VARIABLES
# Variabel di luar fungsi = global
pesan = "Aku keren"

def tampilkan():
    print(pesan)  # Bisa mengakses variabel global

tampilkan()

# LOCAL VARIABLE (VARIABEL LOKAL)
# Variabel di dalam fungsi hanya berlaku di dalam fungsi
status = "Global"

def ubah_status():
    status = "Local"
    print("Di dalam fungsi:", status)

ubah_status()
print("Di luar fungsi:", status)

# KEYWORD global
# Digunakan untuk mengubah variabel global dari dalam fungsi
nilai = 100

def ubah_nilai():
    global nilai
    nilai = 200

ubah_nilai()
print("Nilai sekarang:", nilai)




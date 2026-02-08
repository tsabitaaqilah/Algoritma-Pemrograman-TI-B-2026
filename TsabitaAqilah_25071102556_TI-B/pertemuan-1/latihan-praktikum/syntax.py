# PYTHON INDENTATION (INDENTASI)
# Indentasi = spasi di awal baris
# Di Python, indentasi WAJIB karena menunjukkan blok kode
umur = 18

if umur >= 17:
    print("Kamu sudah punya KTP")  # Baris ini termasuk blok if karena menjorok

# CONTOH TANPA INDENTASI (AKAN ERROR)
# Kalau jalankan ini (SyntaxError)
# if umur >= 17:
# print("Kamu sudah punya KTP")   # Tidak menjorok → ERROR

# JUMLAH SPASI BEBAS, TAPI HARUS KONSISTEN
# Contoh pakai 2 spasi
if umur >= 17:
  print("Boleh ikut pemilu")   # Ini valid (2 spasi)

# Contoh pakai 4 spasi (paling umum dipakai programmer)
if umur >= 17:
    print("Boleh membuat SIM")  # Ini juga valid (4 spasi)

# TIDAK BOLEH CAMPUR JUMLAH SPASI DALAM SATU BLOK
# Ini contoh yang SALAH (jangan dijalankan)
# if umur >= 17:
#   print("Baris pertama benar")
#     print("Baris kedua beda spasi → ERROR")

# INDENTASI DI DALAM BLOK BERSARANG (NESTED)
nilai = 85

if nilai >= 75:
    print("Kamu lulus")
    if nilai >= 90:
        print("Nilai kamu sangat memuaskan!")  # Lebih menjorok karena di dalam if kedua
    else:
        print("Nilai kamu sudah bagus!")       # Sejajar dengan if kedua

# CONTOH LAIN BLOK KODE: LOOP
# Semua yang menjorok ke dalam adalah bagian dari perulangan
for i in range(3):
    print("Perulangan ke-", i)
    print("Ini masih di dalam loop")

print("Ini di luar loop karena tidak menjorok")

# PYTHON STATEMENTS (PERNYATAAN / INSTRUKSI)
# Program komputer terdiri dari kumpulan instruksi yang dijalankan berurutan.
# Di Python, instruksi ini disebut STATEMENT.
# Contoh statement sederhana:
print("Aku sedang belajar Python!")  # Ini satu statement

# SETIAP BARIS 
# Di Python, statement biasanya berakhir saat baris berakhir
# Tidak perlu tanda titik koma (;) seperti di Java/C
print("Baris pertama dijalankan dulu")
print("Baris kedua dijalankan setelahnya")
print("Baris ketiga dijalankan terakhir")

# URUTAN EKSEKUSI STATEMENT
# Python membaca dari atas ke bawah
print("Langkah 1")
print("Langkah 2")
print("Langkah 3")

# Output akan muncul sesuai urutan penulisan

# BANYAK STATEMENT DALAM SATU PROGRAM
nama = "Bita"
umur = 18

print("Nama:", nama)
print("Umur:", umur)
print("Tahun depan umur:", umur + 1)

# TITIK KOMA (;) DI PYTHON
# Titik koma SEBENARNYA boleh dipakai untuk memisahkan statement
# Tapi jarang digunakan karena bikin kode sulit dibaca
print("Aku"); print("sedang"); print("belajar"); print("Python")

# Semua di atas tetap dijalankan dari kiri ke kanan

# CONTOH YANG SALAH (TANPA PEMISAH)
# Ini akan ERROR kalau dijalankan, karena ada 2 statement dalam 1 baris tanpa pemisah
# print("Halo") print("semua")   # SyntaxError

# STATEMENT BISA BERUPA BANYAK HAL
# 1. Statement mencetak output
print("Ini orang")

# 2. Statement membuat variabel
angka = 10

# 3. Statement percabangan
if angka > 5:
    print("Angka lebih dari lima")

# 4. Statement perulangan
for i in range(2):
    print("Loop ke-", i)




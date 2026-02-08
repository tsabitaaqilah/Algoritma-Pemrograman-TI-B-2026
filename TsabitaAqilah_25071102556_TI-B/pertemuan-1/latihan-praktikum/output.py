# PYTHON OUTPUT (MENAMPILKAN TEKS / NILAI)
# Untuk menampilkan sesuatu ke layar, Python menggunakan fungsi print()
print("Selamat datang kembali!")  # Menampilkan teks

# PRINT BISA DIPAKAI BERKALI-KALI
# Setiap print() otomatis pindah ke baris baru
print("Baris pertama")
print("Baris kedua")
print("Baris ketiga")

# MENGGUNAKAN TANDA KUTIP
# Teks di Python WAJIB di dalam tanda kutip
# Bisa pakai kutip dua "..." atau kutip satu '...'
print("Aku suka kamu")
print('Kamu suka aku')

# Kalau lupa pakai tanda kutip → ERROR
# print(Aku suka kamu)   # SyntaxError

# PRINT ANGKA DAN TIPE DATA LAIN
print(100)          # Angka
print(3.14)         # Float
print(True)         # Boolean

# MENGGABUNGKAN TEKS DAN VARIABEL
nama = "Bita"
umur = 18

print("Nama saya", nama)
print("Umur saya", umur, "tahun")

# PRINT TANPA PINDAH BARIS (end=)
# Secara default, print() diakhiri dengan newline (\n)
# Kita bisa ubah pakai parameter end=
print("Halo", end=" ")
print("semuanya!")  # Akan tampil di baris yang sama

# Bisa juga pakai simbol lain
print("Loading", end="...")
print("Selesai!")

# PRINT DENGAN FORMAT (F-STRING)
# Cara modern dan paling rapi untuk gabung teks + variabel
nama = "Bita"
nilai = 95

print(f"Nama saya {nama} dan nilai saya {nilai}")

# PRINT NUMBERS (MENAMPILKAN ANGKA)
# Angka TIDAK perlu tanda kutip
# Kalau pakai kutip, Python menganggapnya sebagai teks (string)
print(7)
print(2026)
print(123456789)

# OPERASI MATEMATIKA DI DALAM print()
# Python bisa langsung menghitung di dalam print()

print(10 + 5)   # Penjumlahan
print(20 - 8)   # Pengurangan
print(6 * 7)    # Perkalian
print(15 / 3)   # Pembagian
print(17 % 5)   # Sisa bagi
print(2 ** 4)   # Pangkat

# MENAMPILKAN HASIL PERHITUNGAN DARI VARIABEL
a = 12
b = 4

print(a + b)
print(a * b)

# MENGGABUNGKAN TEKS DAN ANGKA
# Gunakan koma (,) untuk menggabungkan teks dan angka
# Python otomatis memberi spasi di antaranya
umur = 18
tinggi = 156

print("Umur saya", umur, "tahun")
print("Tinggi badan saya", tinggi, "cm")

# PERBEDAAN ANGKA DAN TEKS ANGKA
print(10 + 5)     # Hasil = 15 (perhitungan matematika)
print("10" + "5") # Hasil = 105 (digabung sebagai teks)


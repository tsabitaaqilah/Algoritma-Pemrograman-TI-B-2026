# PYTHON CASTING (MENGUBAH TIPE DATA)
# Casting = proses mengubah satu tipe data ke tipe data lain
# Dilakukan menggunakan fungsi bawaan seperti int(), float(), str()

# CASTING KE INTEGER (int)
# Bisa dari float atau string yang berisi angka bulat
a = int(9.9)      # Desimal dibuang → 9
b = int("15")     # String angka → 15
c = int(True)     # Boolean True = 1

print(a, type(a))
print(b, type(b))
print(c, type(c))

# Tidak bisa mengubah string bukan angka
# int("halo")  # ERROR

# CASTING KE FLOAT (float)
# Bisa dari int atau string angka desimal
d = float(7)        # 7 → 7.0
e = float("8.5")    # "8.5" → 8.5
f = float("12")     # "12" → 12.0

print(d, type(d))
print(e, type(e))
print(f, type(f))

# CASTING KE STRING (str)
# Hampir semua tipe data bisa diubah ke string
g = str(100)       # int → "100"
h = str(3.14)      # float → "3.14"
i = str(True)      # bool → "True"

print(g, type(g))
print(h, type(h))
print(i, type(i))

# CONTOH PENGGUNAAN DI KEHIDUPAN NYATA
umur = 18

# Tidak bisa gabung string + int langsung
# print("Umur saya " + umur)  # ERROR

# Harus diubah dulu ke string
print("Umur saya " + str(umur))

# For loop digunakan untuk mengulang data yang berbentuk urutan (sequence)
# seperti: list, tuple, string, set, dictionary, range

# FOR PALING DASAR (LIST)
buah = ["apel", "jeruk", "mangga"]

for item in buah:  # ambil setiap isi list satu per satu
    print("Buah:", item)

# LOOPING STRING
for huruf in "PYTHON":
    print("Huruf:", huruf)

# MENGGUNAKAN BREAK
buah = ["apel", "jeruk", "mangga", "pisang"]

for item in buah:
    if item == "mangga":
        print("Ketemu mangga, loop dihentikan")
        break  # menghentikan loop
    print(item)

# MENGGUNAKAN CONTINUE
buah = ["apel", "jeruk", "mangga", "pisang"]

for item in buah:
    if item == "jeruk":
        continue  # lewati jeruk
    print("Dicetak:", item)

# MENGGUNAKAN RANGE()
# range(5) → menghasilkan angka 0 sampai 4
for i in range(5):
    print("Angka:", i)

# range(start, stop)
for i in range(2, 6):  # 2 sampai 5
    print("Range 2-5:", i)

# range(start, stop, step)
for i in range(0, 10, 2):  # lompat 2 angka
    print("Kelipatan 2:", i)

# ELSE PADA FOR
for i in range(3):
    print("Loop ke-", i)
else:
    print("Loop selesai normal (tanpa break)")

# else TIDAK dijalankan jika ada break
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("Ini tidak akan tampil")

# NESTED FOR (FOR DI DALAM FOR)
warna = ["merah", "biru"]
buah = ["apel", "mangga"]

for w in warna:
    for b in buah:
        print(w, b)

# FOR DENGAN INDEX (ENUMERATE)
buah = ["apel", "jeruk", "mangga"]

for index, nama in enumerate(buah):
    print("Index", index, "=", nama)

# FOR PADA DICTIONARY
data = {"nama": "Budi", "umur": 20}

# ambil key
for key in data:
    print("Key:", key)

# ambil value
for value in data.values():
    print("Value:", value)

# ambil key dan value
for key, value in data.items():
    print(key, "=", value)

# FOR PADA SET
angka_set = {1, 2, 3, 4}

for angka in angka_set:
    print("Isi set:", angka)

# PASS (LOOP KOSONG)
for i in range(3):
    pass  # tidak melakukan apa-apa

# LIST COMPREHENSION (FOR VERSI SINGKAT)
kuadrat = [x**2 for x in range(5)]
print("List kuadrat:", kuadrat)

# dengan kondisi
genap = [x for x in range(10) if x % 2 == 0]
print("Bilangan genap:", genap)

# FOR + STRING FORMAT
nama = ["Ani", "Budi", "Citra"]

for n in nama:
    print(f"Halo {n}, selamat belajar Python!")

# PERBEDAAN FOR vs WHILE
# FOR → jumlah perulangan sudah jelas
for i in range(3):
    print("FOR ke-", i)

# WHILE → berhenti tergantung kondisi
i = 0
while i < 3:
    print("WHILE ke-", i)
    i += 1



# While loop digunakan untuk mengulang kode
# SELAMA kondisi bernilai True

# WHILE PALING DASAR
i = 1  # variabel awal (counter)

while i <= 5:  # selama kondisi True, loop terus jalan
    print("Perulangan ke-", i)
    i += 1  # penting! kalau tidak, loop jadi tak terbatas (infinite loop)

# CONTOH INFINITE LOOP (HATI-HATI!)
# while True:
#     print("Ini tidak akan berhenti")
# Loop ini akan berjalan selamanya kecuali dihentikan manual (CTRL+C)

# BREAK = MENGHENTIKAN LOOP LANGSUNG
angka = 1

while angka <= 10:
    print("Angka:", angka)

    if angka == 5:
        print("Loop dihentikan pakai break")
        break  # keluar dari loop walaupun kondisi masih True

    angka += 1

# CONTINUE = MELEWATI 1 ITERASI
angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        print("Angka 3 dilewati")
        continue  # lompat ke iterasi berikutnya

    print("Dicetak:", angka)

# ELSE PADA WHILE
# else dijalankan jika loop BERHENTI NORMAL (bukan karena break)
x = 1

while x <= 3:
    print("x =", x)
    x += 1
else:
    print("Loop selesai tanpa break")


# Contoh else TIDAK dijalankan karena ada break

y = 1

while y <= 3:
    print("y =", y)
    if y == 2:
        break  # loop berhenti pakai break
    y += 1
else:
    print("Ini tidak akan tampil")

# WHILE DENGAN KONDISI MATEMATIKA
# menghitung jumlah total sampai melebihi 50
total = 0
n = 1

while total <= 50:
    total += n
    print("Tambah", n, "total jadi", total)
    n += 1

# WHILE DENGAN LIST
buah = ["apel", "jeruk", "mangga"]
index = 0

while index < len(buah):
    print("Buah:", buah[index])
    index += 1

# NESTED WHILE (WHILE DI DALAM WHILE)
i = 1

while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# PERBEDAAN WHILE vs FOR
# WHILE → dipakai kalau jumlah perulangan BELUM PASTI
# FOR   → dipakai kalau jumlah perulangan SUDAH JELAS

# Contoh while (tidak tahu berhenti kapan)
# selama password salah, terus ulang

# Contoh for (sudah jelas 5 kali)
for i in range(5):
    print("Perulangan for ke-", i)




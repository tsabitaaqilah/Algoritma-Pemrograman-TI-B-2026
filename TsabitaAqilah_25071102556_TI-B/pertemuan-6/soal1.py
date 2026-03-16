film = [
    ["Danur", 50000],
    ["Inside Out", 45000],
    ["Avatar", 75000],
    ["Spiderman", 70000],
    ["Frozen", 60000]
]

print("Daftar Film:")
for i in range (len(film)):
    print(f"{i+1}. {film[i][0]} - Rp{film[i][1]}")

nomor_film = int(input("Masukkan nomor film yang dipilih: "))

if 1 <= nomor_film <= len(film):
    film_terpilih = film[nomor_film - 1]
    print(f"Anda memilih '{film_terpilih[0]}' dengan harga Rp{film_terpilih[1]}")
else:
    print("Nomor film tidak valid!")
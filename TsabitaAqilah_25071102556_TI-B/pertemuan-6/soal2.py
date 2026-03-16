film = [
    ["Danur", 50000],
    ["Inside Out", 45000],
    ["Avatar", 75000],
    ["Spiderman", 70000],
    ["Frozen", 60000]
]

daftar_pembelian = []

while True:
    print("\nDaftar Film:")
    for i in range (len(film)):
        print(f"{i+1}. {film[i][0]} - Rp{film[i][1]}")
    print("0. Selesai")

    nomor_film = int(input("Pilih nomor film: "))
    if nomor_film == 0:
        break
    elif 1 <= nomor_film <= len(film):
        jumlah_tiket = int(input(f"Jumlah tiket untuk '{film[nomor_film-1][0]}': "))
        daftar_pembelian.append([film[nomor_film-1][0], film[nomor_film-1][1], jumlah_tiket])
    else:
        print("Nomor film tidak valid!")

total_bayar = 0
print("\nDaftar Pembelian:")
for item in daftar_pembelian:
    subtotal = item[1] * item[2]
    total_bayar += subtotal
    print(f"{item[0]} x{item[2]} = Rp{subtotal}")
print(f"Total Harga: Rp{total_bayar}")
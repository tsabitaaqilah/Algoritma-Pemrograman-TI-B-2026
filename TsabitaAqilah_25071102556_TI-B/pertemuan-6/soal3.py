total_bayar = int(input("Masukkan total pembelian: Rp"))

while True:
    uang_dibayar = int(input("Masukkan uang yang dibayarkan: Rp"))
    if uang_dibayar < total_bayar:
        print("Uang yang dibayarkan kurang!")
    else:
        break

kembalian = uang_dibayar - total_bayar

print(f"Total Pembelian: Rp{total_bayar}")
print(f"Uang Dibayar: Rp{uang_dibayar}")
if kembalian == 0:
    print("Uang pas, tidak ada kembalian")
else:
    print(f"Kembalian Anda: Rp{kembalian}")
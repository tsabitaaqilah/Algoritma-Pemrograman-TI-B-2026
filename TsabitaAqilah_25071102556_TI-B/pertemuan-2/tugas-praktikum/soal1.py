def rata_rata(nilai):
    if len(nilai) == 0:
        return "Data kosong"
    
    total = 0
    for n in nilai:
        total += n   
    return total / len(nilai)

data_nilai = [80, 80, 90, 90, 85]
hasil = rata_rata(data_nilai)
print("Rata-rata nilai:", hasil)


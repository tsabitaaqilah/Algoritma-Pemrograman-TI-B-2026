def bilangan_prima(n):
    daftar_prima = []
    
    for angka in range(2, n + 1):
        pembagi = 0
        
        for i in range(1, angka + 1):
            if angka % i == 0:
                pembagi += 1
        
        if pembagi == 2:  
            daftar_prima.append(angka)
    
    return daftar_prima

print("Bilangan prima sampai 50:", bilangan_prima(50))



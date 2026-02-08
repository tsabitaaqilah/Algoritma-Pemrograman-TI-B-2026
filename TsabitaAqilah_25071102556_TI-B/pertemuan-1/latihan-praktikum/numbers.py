# PYTHON NUMBERS
# Python punya 3 tipe angka utama:
# int, float, dan complex

# MEMBUAT VARIABEL NUMERIC
x = 10       # int (bilangan bulat)
y = 3.5      # float (desimal)
z = 2j       # complex (bilangan kompleks)

print(type(x))
print(type(y))
print(type(z))

# INTEGER (int)
# Bilangan bulat, bisa positif atau negatif, tanpa desimal
a = 7
b = -150
c = 12345678901234567890  # Bisa sangat besar

print(type(a))
print(type(b))
print(type(c))

# FLOAT (BILANGAN DESIMAL)
d = 4.75
e = -0.25
f = 1.0

print(type(d))
print(type(e))
print(type(f))

# FLOAT DENGAN NOTASI ILMIAH (e / E)
g = 5e3      # 5 × 10^3 = 5000.0
h = 9E2      # 9 × 10^2 = 900.0
i = -2.5e4   # -25000.0

print(g, h, i)
print(type(g))

# COMPLEX NUMBERS
# Menggunakan huruf j sebagai bagian imajiner
j = 4 + 3j
k = 7j
l = -2j

print(type(j))
print(type(k))
print(type(l))

# KONVERSI TIPE ANGKA (TYPE CONVERSION)
m = 8        # int
n = 6.9      # float
o = 1j       # complex

# int to float
p = float(m)

# float to int (desimal dihapus, bukan dibulatkan)
q = int(n)

# int to complex
r = complex(m)

print(p, type(p))
print(q, type(q))
print(r, type(r))

# Tidak bisa mengubah complex ke int atau float
# int(o)   # ERROR
# float(o) # ERROR

# ANGKA ACAK (RANDOM NUMBER)
import random  # Mengimpor modul random

acak = random.randrange(1, 11)  # Angka acak dari 1 sampai 10
print("Angka acak:", acak)


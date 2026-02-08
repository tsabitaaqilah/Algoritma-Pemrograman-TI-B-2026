# ARITHMETIC OPERATORS (OPERATOR MATEMATIKA)
x = 15
y = 4

print(x + y)   # Penjumlahan -> 19
print(x - y)   # Pengurangan -> 11
print(x * y)   # Perkalian   -> 60
print(x / y)   # Pembagian (float) -> 3.75
print(x % y)   # Modulus / sisa bagi -> 3
print(x ** y)  # Pangkat -> 15^4 = 50625
print(x // y)  # Floor division (dibulatkan ke bawah) -> 3

# PERBEDAAN / DAN //
a = 12
b = 5

print(a / b)   # 2.4  -> hasil selalu float
print(a // b)  # 2    -> dibulatkan ke bawah

# ASSIGNMENT OPERATORS
n = 10
n += 5   # n = n + 5
print(n)  # 15

n -= 3   # n = n - 3
print(n)  # 12

n *= 2   # n = n * 2
print(n)  # 24

n /= 4   # n = n / 4
print(n)  # 6.0

n %= 4   # n = n % 4
print(n)  # 2.0

n **= 3  # n = n ** 3
print(n)  # 8.0

n //= 3  # floor division assignment
print(n)  # 2.0

# WALRUS OPERATOR (:=)
# Bisa assign variabel di dalam ekspresi

if (panjang := len("python")) > 5:
    print("Panjang kata:", panjang)

# COMPARISON OPERATORS
a = 5
b = 3

print(a == b)  # False -> sama dengan
print(a != b)  # True  -> tidak sama
print(a > b)   # True
print(a < b)   # False
print(a >= 5)  # True
print(b <= 2)  # False

# CHAINED COMPARISON
x = 7
print(1 < x < 10)  # True
print(1 < x and x < 10)  # Sama hasilnya

# LOGICAL OPERATORS

print(True and False)  # False
print(True or False)   # True
print(not True)        # False


# Short-circuit (evaluasi berhenti lebih awal)
def tes():
    print("Fungsi dipanggil")
    return True

print(True or tes())   # tes() tidak dipanggil
print(False and tes()) # tes() tidak dipanggil

# IDENTITY OPERATORS
a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # True  -> isi sama
print(a is b)  # False -> objek beda
print(a is c)  # True  -> referensi sama

# MEMBERSHIP OPERATORS

buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)       # True
print("pisang" not in buah) # True

teks = "Hello Python"
print("Python" in teks)     # True
print("java" in teks)       # False

# BITWISE OPERATORS (OPERASI BINARY)
# Angka 6  = 0110
# Angka 3  = 0011

print(6 & 3)   # AND  -> 0010 = 2
print(6 | 3)   # OR   -> 0111 = 7
print(6 ^ 3)   # XOR  -> 0101 = 5
print(~6)      # NOT  -> -(6+1) = -7
print(6 << 1)  # Shift kiri  -> 1100 = 12
print(6 >> 1)  # Shift kanan -> 0011 = 3

# OPERATOR PRECEDENCE (URUTAN PRIORITAS)
print(2 + 3 * 4)     # 14 -> kali dulu
print((2 + 3) * 4)   # 20 -> kurung dulu

print(5 + 4 - 7 + 3) # Dievaluasi dari kiri ke kanan

# OPERATOR PADA STRING
print("Py" + "thon")  # Gabung string
print("Ha" * 3)       # Ulang string -> HaHaHa

# OPERATOR PADA LIST
a = [1, 2]
b = [3, 4]

print(a + b)   # Gabung list
print(a * 2)   # Ulang list

# OPERATOR DENGAN BOOLEAN
print(True + True)   # 2
print(False * 10)    # 0

# PRIORITAS LOGIKA
print(True or False and False)  
# and dievaluasi dulu -> False
# True or False -> True

# TERNARY OPERATOR
umur = 17
status = "Dewasa" if umur >= 18 else "Belum Dewasa"
print(status)

# OPERATOR PADA SET
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
print(a ^ b)  # Symmetric difference

# OPERATOR KHUSUS UNTUK NONE
data = None
print(data is None)     # Cara paling benar cek None
print(data is not None)

# GABUNGAN BANYAK OPERATOR
nilai = 95
lulus = nilai >= 85 and nilai <= 100
print("Lulus:", lulus)


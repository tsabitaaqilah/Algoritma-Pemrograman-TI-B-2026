# IF DASAR (PENGKONDISIAN)
a = 33
b = 200

# Jika kondisi True, blok di dalam if dijalankan
if b > a:
    print("b lebih besar dari a")

# CARA KERJA IF
angka = 15

# Python mengevaluasi kondisi -> hasilnya True/False
if angka > 0:
    print("Angka positif")  # dijalankan karena True

# PENTINGNYA INDENTASI
# Indentasi menentukan blok kode
umur = 18
if umur >= 18:
    print("Sudah dewasa")
    print("Boleh membuat KTP")
    print("Punya hak pilih")
# Kalau tidak sejajar, akan error

# BOOLEAN LANGSUNG DI IF
is_logged_in = True

if is_logged_in:  # tidak perlu == True
    print("Selamat datang kembali!")

# TRUTHY & FALSY DI IF
nama = ""
if not nama:
    print("Nama kosong dianggap False")

saldo = 100
if saldo:
    print("Saldo ada isinya dianggap True")

# ELIF (ELSE IF)
a = 33
b = 33

if b > a:
    print("b lebih besar")
elif a == b:
    print("a sama dengan b")  # dijalankan

# BANYAK ELIF
nilai = 75

if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")  # dijalankan
elif nilai >= 60:
    print("Nilai D")
else:
    print("Nilai E")

# ELSE (KONDISI CADANGAN)
umur = 15

if umur >= 18:
    print("Boleh masuk")
else:
    print("Belum cukup umur")  # dijalankan

# RANTAI IF-ELIF-ELSE LENGKAP
suhu = 22

if suhu > 30:
    print("Panas")
elif suhu > 20:
    print("Hangat")  # dijalankan
elif suhu > 10:
    print("Sejuk")
else:
    print("Dingin")

# SHORTHAND IF (SATU BARIS)
a = 5
b = 2
if a > b: print("a lebih besar")

# TERNARY OPERATOR (IF ELSE SATU BARIS)
umur = 17
status = "Dewasa" if umur >= 18 else "Anak-anak"
print(status)

# BEBERAPA KONDISI DALAM SATU BARIS
a = 10
b = 10
print("A") if a > b else print("Sama") if a == b else print("B")

# LOGICAL OPERATORS DI IF
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Kedua kondisi benar")

if a > b or a > c:
    print("Salah satu kondisi benar")

if not a > b:
    print("a tidak lebih besar dari b")

# PRIORITAS LOGIKA
# not > and > or
usia = 25
is_student = False
punya_kode_diskon = True

if (usia < 18 or usia > 65) and not is_student or punya_kode_diskon:
    print("Dapat diskon")

# NESTED IF (IF DI DALAM IF)
x = 41

if x > 10:
    print("Lebih dari 10")
    if x > 20:
        print("Dan juga lebih dari 20")
    else:
        print("Tapi tidak lebih dari 20")

# NESTED IF UNTUK LOGIKA BERLAPIS
umur = 25
punya_sim = True

if umur >= 17:
    if punya_sim:
        print("Boleh mengemudi")
    else:
        print("Harus buat SIM dulu")
else:
    print("Belum cukup umur")

# NESTED IF VS LOGICAL OPERATOR
suhu = 25
cerah = True

# Versi nested
if suhu > 20:
    if cerah:
        print("Cuaca bagus")

# Versi ringkas
if suhu > 20 and cerah:
    print("Cuaca bagus (versi singkat)")

# PASS STATEMENT
nilai = 85

if nilai > 90:
    pass  # placeholder, tidak melakukan apa-apa

print("Program tetap jalan")

# VALIDASI INPUT
username = "Bita"

if len(username) > 0:
    print("Selamat datang,", username)
else:
    print("Username tidak boleh kosong")

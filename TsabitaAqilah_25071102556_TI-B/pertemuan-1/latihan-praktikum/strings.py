# PYTHON STRINGS
# String adalah teks yang diapit tanda kutip satu atau dua

teks1 = "Halo semua"
teks2 = 'Ayo belajar bersama'

print(teks1)
print(teks2)

# KUTIP DI DALAM KUTIP
print("It's a beautiful day")      # Kutip satu di dalam kutip dua
print('Dia berkata "Suka!"')       # Kutip dua di dalam kutip satu

# MULTILINE STRING
paragraf = """Ini adalah contoh
string yang terdiri
dari beberapa baris"""
print(paragraf)

# STRING ADALAH ARRAY KARAKTER
kata = "Suka"
print(kata[0])  # S
print(kata[3])  # a

# LOOPING STRING
for huruf in "Kode":
    print(huruf)

# PANJANG STRING
kalimat = "Aku suka kamu"
print(len(kalimat))

# CEK TEKS DALAM STRING
pesan = "Belajar bersamaku itu menyenangkan"

print("belajar" in pesan)        # True
print("melelahkan" not in pesan)      # True

# SLICING STRING
teks = "Informatika"

print(teks[0:4])   # Info
print(teks[:5])    # Infor
print(teks[5:])    # matika
print(teks[-4:])   # tika

# MENGUBAH STRING
a = " hello semua "

print(a.upper())    # HELLO SEMUA
print(a.lower())    # hello semua
print(a.strip())    # hapus spasi depan belakang
print(a.replace("semua", "dunia"))
print(a.split())    # pisah jadi list

# MENGGABUNGKAN STRING (CONCATENATION)
depan = "Belajar"
belakang = "bersama"

gabung = depan + " " + belakang
print(gabung)

# FORMAT STRING (F-STRING)
nama = "Bita"
nilai = 95

print(f"Nama saya {nama} dan nilai saya {nilai}")
print(f"Setengah dari nilai adalah {nilai/2}")

# ESCAPE CHARACTER
print("Dia berkata \"hidup itu mudah\"")
print("Baris pertama\nBaris kedua")
print("Kolom1\tKolom2")

# BEBERAPA STRING METHODS PENTING
contoh = "Dia proplayer"

print(contoh.capitalize())
print(contoh.title())
print(contoh.count("p"))
print(contoh.find("pro"))
print(contoh.startswith("Dia"))
print(contoh.endswith("yer"))

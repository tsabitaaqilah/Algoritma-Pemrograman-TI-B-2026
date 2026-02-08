# 1. MEMBUAT FUNCTION DASAR
def sapa():
    # isi function HARUS menjorok ke dalam (indentasi)
    print("Halo dari dalam function!")

# Memanggil function
sapa()

# FUNCTION BISA DIPANGGIL BERKALI-KALI
def salam():
    print("Selamat belajar Python!")

salam()
salam()
salam()

# FUNCTION DENGAN PARAMETER
# Parameter = variabel yang menerima nilai saat function dipanggil
def sapa_nama(nama):
    print("Halo", nama)

sapa_nama("Budi")
sapa_nama("Ani")

# PARAMETER vs ARGUMEN
def contoh(x):  # x = parameter
    print(x)

contoh(10)      # 10 = argumen

# FUNCTION DENGAN LEBIH DARI 1 PARAMETER
def tambah(a, b):
    print("Hasil:", a + b)

tambah(5, 3)

# RETURN (MENGEMBALIKAN NILAI)
def kali(a, b):
    return a * b  # function berhenti di sini

hasil = kali(4, 5)
print("Hasil perkalian:", hasil)

# Tanpa return → hasilnya None
def tanpa_return():
    print("Saya hanya mencetak")

print(tanpa_return())  # None

# DEFAULT PARAMETER
def sapa_default(nama="Teman"):
    print("Halo", nama)

sapa_default("Rina")
sapa_default()  # pakai nilai default

# POSITIONAL ARGUMENT
def data_diri(nama, umur):
    print("Nama:", nama)
    print("Umur:", umur)

data_diri("Andi", 20)  # urutan harus benar

# KEYWORD ARGUMENT
data_diri(umur=25, nama="Budi")  # urutan bebas

# CAMPUR POSITIONAL + KEYWORD

def hewan(jenis, nama, umur):
    print(jenis, nama, umur)

hewan("Kucing", nama="Oyen", umur=2)

# MENGIRIM LIST KE FUNCTION
def cetak_list(data):
    for item in data:
        print("Isi:", item)

cetak_list(["apel", "jeruk", "mangga"])

# MENGIRIM DICTIONARY KE FUNCTION
def cetak_dict(person):
    print("Nama:", person["nama"])
    print("Umur:", person["umur"])

cetak_dict({"nama": "Sari", "umur": 22})

# RETURN BANYAK NILAI (TUPLE)
def operasi(a, b):
    return a + b, a - b

jumlah, kurang = operasi(10, 5)
print("Jumlah:", jumlah)
print("Kurang:", kurang)

# FUNCTION KOSONG (PASS)
def nanti_disi():
    pass  # placeholder

# GABUNGAN SEMUA JENIS PARAMETER
def lengkap(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

lengkap(1, 2, 3, 4, e=5, f=6)


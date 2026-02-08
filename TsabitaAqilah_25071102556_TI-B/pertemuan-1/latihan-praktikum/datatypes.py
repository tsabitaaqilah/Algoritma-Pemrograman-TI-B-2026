# PYTHON DATA TYPES (TIPE DATA)
# Setiap data di Python punya tipe.
# Kita bisa cek tipe data dengan fungsi type()
x = 10
print(type(x))  # <class 'int'>

# TEXT TYPE (str)
teks = "Belajar bersama"
print(teks)
print(type(teks))

# 2. NUMERIC TYPES (int, float, complex)
a = 25        # integer
b = 3.14      # float/desimal
c = 2 + 3j    # complex number

print(type(a))
print(type(b))
print(type(c))

# SEQUENCE TYPES (list, tuple, range)
# LIST (bisa diubah)
buah = ["apel", "mangga", "jeruk"]
print(buah)
print(type(buah))

# TUPLE (tidak bisa diubah)
warna = ("merah", "hijau", "biru")
print(warna)
print(type(warna))

# RANGE (urutan angka otomatis)
angka = range(5)
print(list(angka))  # diubah ke list supaya terlihat isinya
print(type(angka))

# MAPPING TYPE (dict)
# Dictionary menyimpan data dalam bentuk key : value

siswa = {
    "nama": "Bita",
    "umur": 18,
    "jurusan": "Teknik Informatika"
}
print(siswa)
print(type(siswa))

# SET TYPES (set, frozenset)
# SET (tidak berurutan & tidak duplikat)
angka_set = {1, 2, 3, 3, 2}
print(angka_set)
print(type(angka_set))

# FROZENSET (set yang tidak bisa diubah)
angka_frozen = frozenset({4, 5, 6})
print(angka_frozen)
print(type(angka_frozen))

# BOOLEAN TYPE (bool)
lulus = True
gagal = False
print(type(lulus))

# NONE TYPE
kosong = None
print(kosong)
print(type(kosong))

# MENENTUKAN TIPE DATA SECARA LANGSUNG (CONSTRUCTOR)
# Kita bisa memaksa tipe data saat membuat variabel

x = str("Halo")
y = int(10)
z = float(9.5)
a = list(("apel", "jeruk"))
b = tuple(("A", "B"))
c = dict(nama="Bita", umur=18)
d = set(("x", "y", "z"))
e = bool(1)

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


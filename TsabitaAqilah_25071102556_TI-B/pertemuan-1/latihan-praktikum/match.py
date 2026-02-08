# MATCH DASAR (MIRIP SWITCH-CASE)
hari = 4

match hari:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case 4:
        print("Kamis")  # dijalankan
    case 5:
        print("Jumat")
    case 6:
        print("Sabtu")
    case 7:
        print("Minggu")

# match mengevaluasi nilai sekali, lalu dibandingkan dengan tiap case
# DEFAULT CASE DENGAN _
angka = 10

match angka:
    case 1:
        print("Satu")
    case 2:
        print("Dua")
    case _:
        print("Tidak dikenal")  # dijalankan kalau tidak ada yang cocok

# _ artinya "apapun" (wildcard)
# HARUS ditaruh paling bawah karena selalu cocok

# MENGGABUNGKAN BEBERAPA NILAI (|)
day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Hari kerja")
    case 6 | 7:
        print("Akhir pekan")  # dijalankan

# MATCH DENGAN GUARD (IF DI DALAM CASE)
bulan = 5
tanggal = 4

match tanggal:
    case 1 | 2 | 3 | 4 | 5 if bulan == 4:
        print("Hari kerja di April")
    case 1 | 2 | 3 | 4 | 5 if bulan == 5:
        print("Hari kerja di Mei")  # dijalankan
    case _:
        print("Tidak cocok")

# MATCH DENGAN STRING
perintah = "start"

match perintah:
    case "start":
        print("Mesin dinyalakan")
    case "stop":
        print("Mesin dimatikan")
    case "pause":
        print("Mesin dijeda")
    case _:
        print("Perintah tidak dikenal")

# MATCH DENGAN TIPE DATA BERBEDA
data = 3.14

match data:
    case int():
        print("Ini integer")
    case float():
        print("Ini float")  # dijalankan
    case str():
        print("Ini string")
    case _:
        print("Tipe tidak diketahui")

# MATCH DENGAN LIST / SEQUENCE PATTERN
data = [1, 2]

match data:
    case [a, b]:
        print("List dengan dua elemen:", a, b)  # menangkap nilai
    case [a, b, c]:
        print("List dengan tiga elemen")
    case _:
        print("Bentuk list tidak dikenali")

# MATCH DENGAN TUPLE
titik = (0, 5)

match titik:
    case (0, y):
        print("Titik di sumbu Y, y =", y)  # dijalankan
    case (x, 0):
        print("Titik di sumbu X, x =", x)
    case (x, y):
        print("Titik biasa:", x, y)

# MATCH DENGAN DICTIONARY
user = {"nama": "Qila", "umur": 20}

match user:
    case {"nama": nama, "umur": umur}:
        print(f"User {nama} berumur {umur}")  # menangkap value
    case _:
        print("Format tidak cocok")

# MATCH DENGAN OBJEK (CLASS PATTERN)
class Hewan:
    def __init__(self, nama, kaki):
        self.nama = nama
        self.kaki = kaki

h = Hewan("Kucing", 4)

match h:
    case Hewan(nama="Kucing", kaki=4):
        print("Ini kucing berkaki empat")  # dijalankan
    case Hewan(nama=nama, kaki=kaki):
        print(f"Hewan {nama} dengan {kaki} kaki")
    case _:
        print("Bukan hewan yang dikenali")

# MATCH DENGAN WILDCARD *
data = [1, 2, 3, 4, 5]

match data:
    case [1, *sisa]:
        print("Dimulai dengan 1, sisanya:", sisa)
    case _:
        print("Tidak cocok")

# MATCH VS IF-ELIF
# Match lebih rapi kalau banyak pilihan tetap
kode = 404

match kode:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Kode tidak diketahui")

# MATCH BERSIFAT FIRST MATCH
nilai = 85

match nilai:
    case n if n >= 80:
        print("Nilai tinggi")  # ini dijalankan dulu
    case n if n >= 70:
        print("Nilai cukup")
    case _:
        print("Nilai rendah")

# Hanya case pertama yang cocok yang dijalankan

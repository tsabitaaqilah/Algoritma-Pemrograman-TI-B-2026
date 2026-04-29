struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

#Tugas A — Hitung Total Ukuran
def total_ukuran(folder):
    total = 0
    for item in folder.values():
        if type(item) == dict:  # folder
            total += total_ukuran(item)
        else:  # file
            total += item
    return total

#Tugas B — Hitung Jumlah File
def hitung_file(folder):
    jumlah = 0
    for item in folder.values():
        if type(item) == dict:
            jumlah += hitung_file(item)
        else:
            jumlah += 1
    return jumlah

#Tugas C — Cari File Terbesar
def cari_terbesar(folder):
    nama_file = ""
    ukuran_max = 0

    for nama, item in folder.items():
        if type(item) == dict:
            hasil = cari_terbesar(item)
            if hasil[1] > ukuran_max:
                nama_file, ukuran_max = hasil
        else:
            if item > ukuran_max:
                nama_file = nama
                ukuran_max = item

    return (nama_file, ukuran_max)

#Tugas D — Cetak Struktur Folder
def tampilkan_tree(folder, nama="root", level=0):
    indent = "   " * level

    if level == 0:
        print(f"{nama}")

    for key, item in folder.items():
        if type(item) == dict:
            print(f"{indent}{key}")
            tampilkan_tree(item, key, level + 1)
        else:
            print(f"{indent}{key} ({item} KB)")

print("=== ANALISIS FOLDER SKRIPSI ===\n")
print("Total ukuran skripsi:", total_ukuran(struktur), "KB")
print("Jumlah file:", hitung_file(struktur), "file")

nama, ukuran = cari_terbesar(struktur)
print(f"File terbesar: {nama} ({ukuran} KB)\n")

print("Struktur Folder:\n")
tampilkan_tree(struktur, "Skripsi_Aqil")
class Car:
    def __init__(self, brand, price):
        if not brand:
            raise ValueError("Merk tidak boleh kosong!")
        self.brand = brand
        self.price = price

    def move(self):
        print("Drive!")

try:
    mobil = Car(
        input("Masukkan merk mobil: "),
        int(input("Masukkan harga mobil: "))
    )

    print(f"Mobil {mobil.brand} berhasil dibuat.")
    mobil.move()

except ValueError as e:
    print("Input salah:", e)

finally:
    print("Program selesai.")


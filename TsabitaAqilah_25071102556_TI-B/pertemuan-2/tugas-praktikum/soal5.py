
def jarak(x1, y1, x2, y2):
    selisih_x = x2 - x1
    selisih_y = y2 - y1
    hasil = ((selisih_x ** 2) + (selisih_y ** 2)) ** 0.5
    return hasil

print("Jarak =", jarak(1, 2, 4, 6))



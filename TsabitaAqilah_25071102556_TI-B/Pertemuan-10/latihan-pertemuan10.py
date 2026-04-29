n = int(input("Masukkan jumlah elemen: "))
arr = []
i = 0

while i < n:
    try:
        angka = int(input(f"Angka ke-{i+1}: "))
        if angka < 0:
            print("Jangan negatif!")
        else:
            arr.append(angka)
            i += 1
    except:
        print("Input harus angka!")

#RadixSort
def radixSort(arr):
    mylist = arr.copy()
    radixArray = [[], [], [], [], [], [], [], [], [], []]

    maxVal = max(mylist)
    exp = 1

    while maxVal // exp > 0:

        while len(mylist) > 0:
            val = mylist.pop()
            index = (val // exp) % 10
            radixArray[index].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                mylist.append(val)

        exp *= 10

    return mylist

hasil_radix = radixSort(arr.copy())
print("Sebelum:", arr)
print("Sesudah:", hasil_radix)

#MergeSort
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    hasil = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            hasil.append(left[i])
            i += 1
        else:
            hasil.append(right[j])
            j += 1

    hasil.extend(left[i:])
    hasil.extend(right[j:])

    return hasil

hasil_merge = mergeSort(arr.copy())
print("==============================")
print("Sebelum:", arr)
print("Sesudah:", hasil_merge)

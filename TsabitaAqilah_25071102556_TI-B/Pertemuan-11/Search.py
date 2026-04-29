data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print("Data:", data)

x = int(input("Nilai yang mau dicari: "))

hasil_linear = linear_search(data, x)
if hasil_linear != -1:
    print(f"Linear Search: Data ditemukan di index {hasil_linear}")
else:
    print("Linear Search: Data tidak ditemukan")

sorted_data = sorted(data)
print("Data setelah diurutkan:", sorted_data)

hasil_binary = binary_search(sorted_data, x)
if hasil_binary != -1:
    print(f"Binary Search: Data ditemukan di index {hasil_binary}")
else:
    print("Binary Search: Data tidak ditemukan")
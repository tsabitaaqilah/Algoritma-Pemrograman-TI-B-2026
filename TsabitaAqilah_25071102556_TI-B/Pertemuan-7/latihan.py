data = [918, 336, 637, 814, 507, 685, 854, 933, 970, 461, 26, 884, 684, 47, 922, 246, 431, 985, 412, 679, 708, 354, 369, 396, 406, 882, 119, 682, 378, 578, 208, 899, 344, 436, 153, 835, 836, 985, 117, 619, 225, 345, 210, 606, 313, 998, 681, 989, 212, 163, 762, 389, 906, 423, 204, 627, 430, 568, 430, 71, 429, 492, 817, 577, 621, 914, 500, 783, 872, 992, 498, 477, 34, 570, 113, 2, 58, 844, 464, 293, 302, 183, 711, 777, 71, 441, 261, 713, 544, 528, 759, 193, 163, 272, 389, 979, 608, 977, 721, 508, 619, 875, 948, 750, 991, 711, 855, 111, 555, 608, 535, 603, 538, 753, 190, 441, 85, 200, 193, 577, 774, 578, 405, 306, 256, 926, 433, 444, 459, 368, 187, 671, 701, 714, 411, 940, 603, 736, 665, 947, 517, 19, 365, 165, 514, 133, 491, 642, 636, 957]

def bubbleSort(arr):
    n = len(arr)
    swap = 0

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
                swapped = True

        if swapped == False:
            break

    return arr, swap

def selectionSort(arr):
    n = len(arr)
    swap = 0

    for i in range(n):
        max = i
        for j in range(i+1, n):
            if arr[j] > arr[max]:
                max = j

        if max != i:
            arr[i], arr[max] = arr[max], arr[i]
            swap += 1

    return arr, swap


bubble_data = data.copy()
selection_data = data.copy()

bubble_result, bubble_swap = bubbleSort(bubble_data)
selection_result, selection_swap = selectionSort(selection_data)


print("Bubble Sort (kecil --> besar):")
print(bubble_result)
print("Jumlah swap Bubble Sort:", bubble_swap)
print("==========================================")
print("Selection Sort (besar --> kecil):")
print(selection_result)
print("Jumlah swap Selection Sort:", selection_swap)
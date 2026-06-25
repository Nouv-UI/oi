import os
os.system("cls")

def binary_search(data_list, target):

    low = 0                          # Indeks awal (Awal)
    high = len(data_list) - 1        # Indeks akhir (Akhir)
    
    while low <= high:
        mid = (low + high) // 2
        # Kasus 1: Target ditemukan di tengah
        if data_list[mid] == target:
            return mid
        # Kasus 2: Target lebih besar dari elemen tengah, cari di paruh kanan
        elif data_list[mid] < target:
            low = mid + 1
        # Kasus 3: Target lebih kecil dari elemen tengah, cari di paruh kiri
        else: # data_list[mid] > target
            high = mid - 1
    # Jika loop selesai, target tidak ada dalam list
    else:
        print("data tak ditemukan")

daftar_terurut = [1, 4, 8, 10, 25, 33] 
target_1 = 10
target_2 = 7

# Cari target 1 ]
hasil_1 = binary_search(daftar_terurut, target_1)
print(f"Pencarian {target_1}: Ditemukan pada indeks {hasil_1}")

# Cari target 2 
hasil_2 = binary_search(daftar_terurut, target_2)
print(f"Pencarian {target_2}: Ditemukan pada indeks {hasil_2}")
import os
os.system("cls")

def quicksort(arr):
    """
    Mengurutkan daftar menggunakan algoritma Quick Sort.

    Args:
        arr: Daftar (list) angka yang akan diurutkan.

    Returns:
        Daftar yang sudah diurutkan.
    """
    # Kasus dasar: Daftar dengan 0 atau 1 elemen sudah diurutkan
    if len(arr) <= 1:
        return arr

    # 1. Pilih Pivot
    # Kita akan memilih elemen pertama sebagai pivot, tapi 
    # Anda bisa memilih pivot secara acak atau median-of-three 
    # untuk kinerja yang lebih baik.
    pivot = arr[0]

    # 2. Partisi (Partition)
    # Bagi daftar menjadi tiga bagian:
    # - less: Semua elemen yang lebih kecil dari pivot
    # - equal: Semua elemen yang sama dengan pivot
    # - greater: Semua elemen yang lebih besar dari pivot
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]

    # 3. Panggil Quick Sort secara rekursif dan Gabungkan
    # Hasil akhir adalah penggabungan dari: 
    # (Quick Sort pada 'less') + ('equal' list) + (Quick Sort pada 'greater')
    return quicksort(less) + equal + quicksort(greater)

# --- Contoh Penggunaan ---
data = [10, 7, 8, 9, 1, 5]
print(f"Daftar sebelum diurutkan: {data}")

data_terurut = quicksort(data)
print(f"Daftar setelah diurutkan: {data_terurut}")
import os
os.system("cls")

list_a = [3, 2, 4, 6, 5, 11, 8, 9]
n = 5 #misal nilai 5 yang dicari

for i in range(len(list_a)):
    if list_a[i] == n:
        print(f"data {n} ditemukan pada indeks {i}")
        break
else:
    print("tidak ditemukan")
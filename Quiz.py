import os
os.system("cls")

data = input("masukkan angka baris 1 : ").split()
data1 = input("masukkan angka baris 2 : ").split()
print()
data2 = input("masukkan angka baris 3 : ").split()
data3 = input("masukkan angka baris 4 : ").split()
data_int = list(map(int,data))
data1_int = list(map(int,data1))
data2_int = list(map(int,data2))
data3_int = list(map(int,data3))

angka1 = data_int[0]                        #Matriks 1
angka2 = data_int[1]                        #|angka1 angka2|
angka3 = data1_int[0]                       #|angka3 angka4|
angka4 = data1_int[1] 
ng1 = data2_int[0]                          #Matriks 2
ng2 = data2_int[1]                          #|ng1 ng2|
ng3 = data3_int[0]                          #|ng3 ng4|
ng4 = data3_int[1]         
baris1 = (angka1*ng1)+(angka2*ng3)          #operasi matriks
baris2 = (angka1*ng2)+(angka2*ng4)          #|baris1 baris2|
baris3 = (angka3*ng1)+(angka4*ng3)          #|baris3 baris4|
baris4 = (angka3*ng2)+(angka4*ng4)
print()
print("hasil perkalian kedua matriks diatas adalah :")
print(baris1, baris2)
print(baris3, baris4)
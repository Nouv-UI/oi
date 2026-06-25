import os
os.system("cls")
#Fungsi Rekurens dan Basis dari QuickSort

def quick(a):
    if len(a) <= 1:
        return a
    
    pivot = a[len(a)//2]
    # print(f"pivot {pivot}")
    left = [x for x in a if x < pivot]
    # print(f"left {left}")
    mid = [x for x in a if x == pivot]
    # print(f"mid {mid}")
    right = [x for x in a if x > pivot]
    # print(f"right {right}")

    return quick(left) + mid + quick(right)
print

o = [8, 3, 1, 7, 0, 10, 2, 18, 19, 3]
print(quick(o))
print(type(o))
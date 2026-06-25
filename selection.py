import os
os.system("cls")
#SelectionSort

mylist = [77, 34, 9, 5, 22, 11, 80, 2]

n = len(mylist)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
     if mylist[j] < mylist[min_index]:
       min_index = j
  min_value = mylist.pop(min_index)
  mylist.insert(i, min_value)

print(mylist)
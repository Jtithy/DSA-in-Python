# Author: Tithy
# Date: 2026-02-19
# Description: Selection/Deletion Sort Algorithm Implementation in Python

arr=[10,50,30,20,40]
sorted_arr=[]

while arr:
    smallest = min(arr)
    sorted_arr.append(smallest)
    arr.remove(smallest)
    print("Current sorted array: ", sorted_arr)
    
print("Final sorted array: ", sorted_arr)
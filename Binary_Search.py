# Author: Tithy
# Date: 2026-02-19
# Description: Binary Search Algorithm Implementation in Python

arr = [5,3,8,4,2,9,1]
arr.sort()

key = 6
low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low+high) // 2
    if arr[mid] == key:
        print("Element forund at index: ", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid+1
    else:
        high = mid-1

if not found:
    print("Element not found.")
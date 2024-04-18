from math import log
import random
from traceback import print_tb
from turtle import st

from zmq import has
import utils.file_rename as file_rename
from utils.printers import print_dict, _remove_duplicates, printArrayWithPointers  

file_rename.rename_file("33. Search in Rotated Sorted Array", __file__)

def rotate_array(arr, rotations):
    # Calculate the actual number of rotations
    rotations = rotations % len(arr)
    
    # Rotate the array using slicing
    rotated_arr = arr[-rotations:] + arr[:-rotations]
    
    return rotated_arr

def solution(nums, target):
    sz = len(nums)
    start = 0
    end = sz - 1
    fail_safe = 0


    while start <= end and fail_safe < sz:
        logs = []
        mid = start + ((end - start) // 2)
        m = nums[mid]
        s = nums[start]
        e = nums[end]

        print((start, 's'), (mid, 'm'), (end, 'e'))
        printArrayWithPointers(nums, [
            (start, 's'), (mid, 'm'), (end, 'e')
        ])

        if( target == m): 
            print("!! found !!")
            return mid

        if(s < e): # sorted
            print("  > sorted")
            if(target < m):
                print("    >> go left")
                end = mid - 1
            else:
                print("    >> go right")
                start = mid + 1
        elif(m < s): # pivot on left
            print("  > pivot on left")
            if(target < m or target >= s):
                print("    >> go left")
                end = mid - 1
            else:
                print("    >> go right")
                start = mid + 1
        else:
            print("  > left sorted")
            if(target < m and target >= s):
                print("    >> go left")
                end = mid - 1
            else:
                print("    >> go right")
                start = mid + 1


        fail_safe += 1
    
    return -1

r = 10
for i in range(20):
    arr = rotate_array([x for x in range(0, 20)], i)
    target = random.randint(0, 19)
    print("=" * 10, "Problem", "=" * 30)
    print("array:", arr) 
    print("target:", target)
    print("rotation:", i)
    print("\nsolution")
    print("\nReturn Value:", solution(arr, target))
    print("=" * 50 + "\n")
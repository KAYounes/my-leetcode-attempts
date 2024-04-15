from math import log
from turtle import st
import utils.file_rename as file_rename
from utils.printers import print_dict  

file_rename.rename_file("153. Find Minimum in Rotated Sorted Array", __file__)

def rotate_array(arr, rotations):
    # Calculate the actual number of rotations
    rotations = rotations % len(arr)
    
    # Rotate the array using slicing
    rotated_arr = arr[-rotations:] + arr[:-rotations]
    
    return rotated_arr

def solution(array):
    sz = len(array)
    start = 0
    end = sz - 1
    fail_safe = 0
    ans = array[0];


    while start <= end and fail_safe < sz:
        logs = []
        mid = start + ((end - start) // 2)
        m = array[mid]
        s = array[start]
        e = array[end]
        
        if(s < e):
            return min(s, ans)
        if(m < s): 
            end = mid - 1
        else:
            start = mid + 1
    
    return ans

r = 10
for i in range(20):
    arr = rotate_array([x for x in range(0, 20)], i)
    print(arr)
    print(solution(arr))

# In List, we have "in" operator but there is no method as such in an Array.

import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def find_number(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            print("Index at which the target number is present: ", i)

find_number(myArray, 10)
##Way 1: Using Array Module

import array

my_array = array.array('i') ##initialize array, where i means int data type
print("Array:", my_array)
print("Len Array", len(my_array))

## Time Complexity - O(1)
## Space Complexity - O(1)

#####################################################################

my_array1 = array.array('i', [1,2,3,4])
print("Array:", my_array1)
print("Len Array", len(my_array1))

## Time Complexity - O(n)
## Space Complexity - O(n)

#####################################################################

##Way 2: Using Numpy

import numpy as np

np_array = np.array([], dtype=int)
print("Array:", np_array)
print("Len Array", len(np_array))

## Time Complexity - O(1)
## Space Complexity - O(1)

#####################################################################

np_array1 = np.array([1,2,3,4], dtype=int)
print("Array:", np_array1)
print("Len Array", len(np_array1))

## Time Complexity - O(n)
## Space Complexity - O(n)

#####################################################################
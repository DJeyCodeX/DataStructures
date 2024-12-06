import array

my_array = array.array('i', [1,2,3,4])

def access_array_element(arr, index):
    if index >= len(arr):         #### O(1)
        print("Indext OOB Error") #### O(1)
    else:
        print(arr[index])         #### O(1)

# O(1) = O(1) + O(1) --> O(1)

access_array_element(my_array, 2)

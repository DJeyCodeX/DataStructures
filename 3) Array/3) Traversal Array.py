import array

my_arr = array.array('i', [1,2,3,4,5,6])

def traversal_array(arr):
    for i in arr: # O(n)
        print(i) # O(1)

# O(N) + O(1) --> DROP NON DOMINANT --> Hence, O(n)

traversal_array(my_arr)

## Time Complexity - O(n)
## Space Complexity - O(1)
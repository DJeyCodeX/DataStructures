# Find the maximum product of two integers in an array where all elements are positive.

def max_product(arr):
    nn = sorted(arr)
    last_2 = nn[-2:]
    return last_2[0] * last_2[1]

arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))

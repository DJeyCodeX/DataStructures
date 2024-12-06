def print_items(n):
    for i in range(n): #O(n)
        for j in range(n): #O(n) inside O(n) --> O(n * n) --> O(n^2)
            print(i,j) 

print_items(10) #O(n ^ 2) --> O(10 ^ 2) --> O (10 * 10) --> O(100)

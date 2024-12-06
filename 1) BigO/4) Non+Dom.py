def print_items(n):
    for i in range(n): #O(n)
        for j in range(n): #O(n) inside O(n) --> O(n * n) --> O(n^2)
            print(i,j)
    
    for k in range(n): # O(n)
        print(k)

# O(n ^2) + O(n) --> O(n^2 + n) --> Here n is non dominating and n ^ 2 is dominating --> Hence O(n ^ 2)

print_items(10)

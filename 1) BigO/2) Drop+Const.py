def print_items(n):
    for i in range(n):
        print(i) # O(n)

    for j in range(n):
        print(j) # O(n)

# O(n) + O(n) = O(2n) --> DROP CONSTANTS where 2 is a contant --> Hence, O(n)

print_items(10)


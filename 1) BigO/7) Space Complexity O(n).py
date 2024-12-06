##recursive function
## Space Complexity - O(n)

def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)


sum(3)  ##try to debug, will find that every time it runs it will store that in the memory.
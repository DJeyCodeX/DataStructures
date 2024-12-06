n = 2
m =2

sum = 0
for i in range(n):
    sum += i
# Time Complexity - O(n)

sum = 0
for i in range(n):
    for j in range(n):
        sum += i * j

# Time Complexity - O(n^2)

sum = 0
i = 1
while i <= n:
    sum += i
    i *= 2

# Time Complexity - O(log n)


sum = 0
for i in range(n):
    for j in range(m):
        sum += i * j

# Time Complexity - O(n *m)

sum = 0
for i in range(n):
    print(i)
for j in range(m):
    print(j)

# Time Complexity - O(n + m)

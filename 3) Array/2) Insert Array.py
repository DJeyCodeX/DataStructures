import array

my_array = array.array('i', [1,2,3,4])
print(my_array)
my_array.insert(0, 6) #beginning
print(my_array)

my_array = array.array('i', [1,2,3,4])
print(my_array)
my_array.insert(2, 6) #middle
print(my_array)

my_array = array.array('i', [1,2,3,4])
print(my_array)
my_array.insert(len(my_array)+1, 6) #end
print(my_array)

##In all three Cases
## Time Complexity - O(n)
## Space Complexity - O(1)
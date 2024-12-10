class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    ## Insert at the end
    def append(self, value):
        new_node = Node(value) #---------------> O(1)
        if self.head is None: #---------------> O(1)
            self.head = new_node #---------------> O(1)
            self.tail = new_node #---------------> O(1)
        else:
            self.tail.next = new_node #---------------> O(1)
            self.tail = new_node
        self.length += 1 #---------------> O(1)


    ##Insert at the beginning
    def prepend(self, value):
        new_node = Node(value) #---------------> O(1)
        if self.head is None: #---------------> O(1)
            self.head = new_node #---------------> O(1)
            self.tail = new_node #---------------> O(1)
        else:
            new_node.next = self.head #---------------> O(1)
            self.head = new_node #---------------> O(1)
        self.length += 1 #---------------> O(1)


    ##Insert in middle
    def insert(self, value, index=0):
        new_node = Node(value) #---------------> O(1)
        if index < 0 or index > self.length: #---------------> O(1)
            return False
        elif self.length == 0:
            self.head = new_node #---------------> O(1)
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head #---------------> O(1)
            self.head = new_node
        else:
            temp_node = self.head  #---------------> O(1)
            for _ in range(index-1): #---------------> O(n)
                temp_node = temp_node.next
            print("temp_node", temp_node.value)
            new_node.next = temp_node.next #---------------> O(1)
            temp_node.next = new_node
        self.length += 1 #---------------> O(1)


    #Traverse List
    def traverse(self):
        current = self.head  #---------------> O(1)
        while current is not None: #---------------> O(n)
            print(current.value) #---------------> O(1)
            current = current.next

## So overall, Traversing value has Time Complexity of O(n) and Space Complexity of O(1)



ll = LinkedList()
print(ll.print_list())
print("-------------------")
ll.append(10)
print(ll.print_list())
print("-------------------")
ll.append(20)
print(ll.print_list())
print("-------------------")
ll.prepend(5)
print(ll.print_list())
print("-------------------")
ll.insert(50, 0)
print(ll.print_list())
print("-------------------")
ll.traverse()

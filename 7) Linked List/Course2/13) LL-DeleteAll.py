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


    #Search
    def search(self, target):
        current = self.head  #---------------> O(1)
        index = 0
        while current is not None: #---------------> O(n)
            if current.value == target:
                return index #---------------> O(1)
            current = current.next
            index += 1 #---------------> O(1)
        return -1


    #Get Value based on Index
    def get(self, index):
        if index == -1:  #---------------> O(1)
            return self.tail
        if index < -1 or index >= self.length:  #---------------> O(1)
            return None
        current = self.head
        for _ in range(index):  #---------------> O(n)
            current = current.next  #---------------> O(1)
        return current


    #Set Value based on Index
    def set(self, value, index):
        temp = self.get(index) #---------------> O(n)
        if temp:
            temp.value = value #---------------> O(1)
            return True
        return False


    #Pop First Node
    def pop_first(self):
        if self.length == 0: #---------------> O(1)
            return None
        popped_node = self.head #---------------> O(1)
        if self.length == 1:
            self.head = None #---------------> O(1)
            self.tail = None
        else:
            self.head = self.head.next #---------------> O(1)
            popped_node.next = None
        self.length -= 1 #---------------> O(1)
        return popped_node


    #Pop Method
    def pop(self):
        if self.length == 0:  #---------------> O(1)
            return None
        popped_node = self.tail #---------------> O(1)
        if self.length == 1:
            self.head = self.tail = None #---------------> O(1)
        else:
            temp = self.head #---------------> O(1)
            while temp.next is not self.tail: #---------------> O(n)
                temp = temp.next
            self.tail = temp
            temp.next = None #---------------> O(1)
        self.length -= 1
        return popped_node

    # Remove Method
    def remove(self, index):
        if index >= self.length or index < -1: #---------------> O(1)
            return None
        if index == 0:
            return self.pop_first() #---------------> O(1)
        if index == self.length -1 or index == -1:
            return self.pop() #---------------> O(n)
        prev_node = self.get(index-1) #---------------> O(n)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None #---------------> O(1)
        self.length -= 1
        return popped_node


    #DeleteAll Method
    def deleteAll(self):
        self.head = None
        self.tail = None
        self.length = 0

## So overall, DeleteAll has Time Complexity of O(1) and Space Complexity of O(1)


ll = LinkedList()
print(ll.print_list())
print("-------------------")
ll.append(10)
# print(ll.print_list())
print("-------------------")
ll.append(20)
# print(ll.print_list())
print("-------------------")
ll.prepend(5)
# print(ll.print_list())
print("-------------------")
ll.insert(50, 0)
print(ll.print_list())
print("-------------------")
# ll.traverse()
print("-------------------")
# print(ll.search(20))
print("-------------------")
# print(ll.get(3))
print("-------------------")
# print(ll.set(25,3))
# print(ll.print_list())
print("-------------------")
# print(ll.pop_first())
# print(ll.print_list())
print("-------------------")
# print(ll.pop())
# print(ll.print_list())
print("-------------------")
# print(ll.remove(1))
# print(ll.print_list())
print("-------------------")
print(ll.deleteAll())
print(ll.print_list())

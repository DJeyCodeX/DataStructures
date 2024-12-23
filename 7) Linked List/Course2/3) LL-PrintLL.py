class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next




ll = LinkedList()
ll.append(10)
print(ll.head.value)
print(ll.tail.value)
print("-------------------")
ll.append(20)
print(ll.head.value)
print(ll.tail.value)
print("-------------------")
print(ll.print_list())

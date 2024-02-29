############################################

# Doubly Linked Lists Append Lesson

############################################

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print("-------------------")
    def append(self,value):
        new_node = Node(value)
        # Edge case for when DLL is empty
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
            self.length +=1
            return True
        # if not empty, follow these steps
        #   main change is setting new node prev to tail before changing tail to new node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length+=1
        return True

my_doubly_linked_list=DoublyLinkedList(7)
my_doubly_linked_list.print_list()
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()

        
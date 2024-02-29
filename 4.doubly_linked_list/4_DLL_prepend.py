############################################

# Doubly Linked List Prepend Lesson

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
        print("-------------------")
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print("-------------------")
    def append(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
            self.length +=1
            return True

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length+=1
        return True
    
    def pop(self):
            if self.length ==0:
                return None
            
            temp = self.tail
            if self.length==1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                temp.prev= None
                self.tail.next = None
            self.length-=1
            return temp
    
    def prepend(self,value):
        new_node = Node(value)
        # Edge case if DLL length is 0, point head and tail to new node
        if self.length ==0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length+=1
        return True

my_doubly_linked_list=DoublyLinkedList(7)
my_doubly_linked_list.print_list()
my_doubly_linked_list.prepend(4)
my_doubly_linked_list.print_list()
my_doubly_linked_list.prepend(6)
my_doubly_linked_list.print_list()

        
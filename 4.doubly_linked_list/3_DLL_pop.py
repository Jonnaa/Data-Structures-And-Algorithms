############################################

# Doubly Linked List Pop Lesson

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
    
    # This method will be much easier to implement since we have prev nodes ready to use
    # Singly Linked List would take O(n), but in DLL it would be O(1)
    # def pop(self):
    #     if self.length==0:
    #         return None
    #     elif self.length ==1:
    #         temp = self.head
    #         self.head = None
    #         self.tail = None
    #         self.length-=1
    #         return temp
    #     temp = self.tail
    #     self.tail = self.tail.prev
    #     self.tail.next =None
    #     temp.prev = None
    #     self.length-=1
    #     return temp
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
my_doubly_linked_list=DoublyLinkedList(7)
my_doubly_linked_list.print_list()
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()
print(my_doubly_linked_list.pop())
print(my_doubly_linked_list.pop())
print(my_doubly_linked_list.pop())

        
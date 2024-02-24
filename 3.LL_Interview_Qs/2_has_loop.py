class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self):
        #Edge case: If list is empty, no loop exists
        if self.length <=1:
            return False
        #Edge case: if list has 1 node and tail.next is not None, return True
        elif self.length==1:
            if self.tail.next == None:
                return False
            return True
        #Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm)
        #Both variables start at head
        tortoise = self.head
        hare = self.head
        #Loop runs while hare is not None and it also isnt the tail
        #Avoiding infinite loop by:
        #   Having pointer changes in loop
        #   if to check if tortoise and hare have met eachother again, which would indicate a loop(True)
        while hare is not None and hare!=self.tail:
            tortoise=tortoise.next
            hare=hare.next.next
            if tortoise==hare:
                return True
        return False
    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""

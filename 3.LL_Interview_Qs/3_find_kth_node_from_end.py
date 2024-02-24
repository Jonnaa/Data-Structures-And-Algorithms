class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
        
#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
#                                             #
#    This is a separate function that is      #
#    not a method within the                  #
#    LinkedList class.                        #
#    INDENT ALL THE WAY TO THE LEFT.          #
#                                             #
###############################################
def find_kth_from_end(LL,k):
    #Edge case if LL is empty
    if LL.head == None:
        return None
    #2 pointers needed
    slow_pointer= LL.head
    fast_pointer= LL.head

    #First moving fast pointer ahead k nodes, if fast pointer becomes None
    #   Before reaching k, then K is out of bounds
    counter = 0
    while counter<k:
        if(fast_pointer is None):
            return None
        fast_pointer=fast_pointer.next
        counter+=1
    # slow and fast will now move 1 node at a time, while fast pointer is not none
    while fast_pointer is not None:
        slow_pointer=slow_pointer.next
        fast_pointer=fast_pointer.next
    # once fast_pointer is none, then slow pointer will be at index k from tail
    return slow_pointer


# my_linked_list = LinkedList(None)
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 3
result = find_kth_from_end(my_linked_list, k)

if result:
    print(result.value)
else:
    print(result)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""


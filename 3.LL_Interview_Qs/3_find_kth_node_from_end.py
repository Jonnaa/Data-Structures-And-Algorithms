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
    if LL.head == 0:
        return None
    slow_pointer= LL.head
    fast_pointer= LL.head

    counter = 0
    while counter<k:
        if(fast_pointer is None):
            return None
        fast_pointer=fast_pointer.next
        counter+=1
    # fast_pointer=LL.head

    while fast_pointer is not None:
        slow_pointer=slow_pointer.next
        fast_pointer=fast_pointer.next
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


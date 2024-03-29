############################################

# Linked Lists Append Lesson

############################################

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #Print list method that iterates through the linked list array and prints each value - O(n)
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #Append to the end of the linked list - O(1)
    def append(self,value):
        #Create a new node using Node class
        new_node = Node(value)
        #If linked list empty(no last item to point to new node) : set head and tail to new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        #Else: point tail's next to new node, then point tail to new node to change end
        else: 
            self.tail.next = new_node
            self.tail = new_node
        #Increase length of linked list by 1
        self.length+=1
        #For later exercises
        return True
    

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    1
    2   
"""
############################################

# Linked Lists Prepend Lesson

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
        print("---------------")
        if self.length==0:
            print("Empty LL")
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("---------------")

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
    
    def pop(self):
        #Edge case 1, if list is empty return none
        if self.length==0:
            return None
        #Edge case 2, if list only has 1 node, remove node and change length, return popped node
        elif self.length==1:
            popped = self.head
            self.head=None
            self.tail=None
            self.length=0
            return popped
        else:
            temp = self.head
            # if temp.next is equal to tail, then we have found the node before tail(which will be our new tail)
            while temp.next != self.tail:
                temp = temp.next
            # Save our old tail to return later
            popped = self.tail
            # Change tail pointer to our new tail
            self.tail = temp
            # Change new tail.next to None
            self.tail.next=None
            self.length-=1
            return popped
        
    def prepend(self,value):
        #Create the new node
        new_node = Node(value)
        #If LL length is 0, simply point head and tail to new node
        if self.length==0:
            self.head = new_node
            self.tail = new_node
            self.length+=1
        #Else: point new node next to current head, then move head to new node
        else:
            new_node.next=self.head
            self.head = new_node
            self.length+=1
            return True
        
my_linked_list = LinkedList(1)
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.print_list()
my_linked_list.prepend(5)
my_linked_list.print_list()
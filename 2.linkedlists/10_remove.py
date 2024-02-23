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
            return True
        #Else: point new node next to current head, then move head to new node
        else:
            new_node.next=self.head
            self.head = new_node
            self.length+=1
            return True

    def pop_first(self):
        # if LL length is 0, return None
        if self.length==0:
            return None
        # if LL contains one node, save that node to temp, then point head and tail to None and return temp
        elif self.length==1:
            temp = self.head
            self.head=None
            self.tail = None
            self.length-=1
            return temp
        # if LL contains more than 1 node, save current head to temp, point head to head.next, point temp to None then return temp
        else: 
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length-=1
            return temp
    
    def get(self,index):
        #Edge cases, if LL length 0 or index is either a negative number or greater than LL length, return None
        if self.length ==0 or index<0 or index>self.length:
            return None
        else:
            #Start by saving first node to temp
            temp = self.head
            #Keep a counter that starts from 0
            count = 0
            #While counter is not index, we will keep pointing temp to temp.next and increasing counter
            while count!=index:
                temp = temp.next
                count+=1
            #Return temp, which is the node we are getting
            return temp
    
    def set_value(self,index,value):
        #Edge cases, if LL length 0 or index is either a negative number or greater than LL length, return None
        if self.length ==0 or index<0 or index>self.length:
            return False
        else:
            #Start by saving first node to temp
            temp = self.head
            #Keep a counter that starts from 0
            count = 0
            #While counter is not index, we will keep pointing temp to temp.next and increasing counter
            # This means once counter is index, we have reached the node we want to set a new value to
            while count!=index:
                temp = temp.next
                count+=1
            #Save current value to a var
            old_value = temp.value
            #Change current value to value passed as param
            temp.value = value
            #Return old value
            return True
        
    def insert(self,index, value):
        #Edge cases
        if index<0 or index>self.length:
            return False
        elif index==0:
            return self.prepend(value)
        else:
            new_node = Node(value)
            # temp = self.head 
            # count = 0
            # while index-count-1!=0:
            #     temp = temp.next
            #     count+=1
            temp = self.get(index-1)
            rest = temp.next
            new_node.next = rest
            temp.next = new_node
            self.length+=1
            return True
    
    def remove(self,index):
        if self.length ==0 or index<0 or index>=self.length:
            return None
        elif index==0:
            return self.pop_first()
        
        before = self.get(index-1)
        temp = before.next
        before.next = temp.next
        temp.next = None
        return temp

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list() # prints LL: 1 2
my_linked_list.remove(1)
my_linked_list.print_list() # prints LL: 1


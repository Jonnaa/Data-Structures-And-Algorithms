############################################

# Doubly Linked List Remove Lesson

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
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length-=1
        return temp
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        
        else:
            temp= self.tail
            #        range(start, stop, step)
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self,index,value):
        if index<0 or index>=self.length:
            return False
        temp = self.get(index)
        temp.value = value
        return True
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False

        if index==0:
            return self.prepend(value)

        if index ==self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index-1)
        temp = before.next
        new_node.prev = before
        new_node.next = temp
        before.next = new_node
        temp.prev = new_node
        self.length+=1
        return True

    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        
        if index ==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length-=1
        return temp

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    DLL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    DLL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    DLL after remove() of last node:
    2
    4

"""
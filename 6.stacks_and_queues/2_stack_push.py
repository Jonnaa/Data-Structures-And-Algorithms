############################################

# Stacks Push Lesson

############################################

class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class Stack:
    # Initializing stack, only need to keep track of top and height
    #   top is similar to head for a linked list, and dont need to keep track of
    #   bottom since we only push and remove from the top
    #   height is similar to length on a linked list.
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    # Method to print stack
        # basically identical to printing a singly linked and doubly linked list
        # except difference is temp is top and not head
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    # Method to push onto the stack
            # Identical to singly linked list prepend
    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node  
        else:
            new_node.next = self.top
            self.top = new_node
        self.height+=1
        return True


my_stack = Stack(2)

print('Stack before push(1):')
my_stack.print_stack()

my_stack.push(1)

print('\nStack after push(1):')
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before push(1):
    2

    Stack after push(1):
    1
    2   

"""
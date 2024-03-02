############################################

# Stacks and queues constructor Lesson

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

my_stack = Stack(4)
my_stack.print_stack()
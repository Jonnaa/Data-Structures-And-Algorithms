############################################

# Queues Enqueue Lesson

############################################

# Building a queue using a linked list(linked list is a data structure)
    # Some things to note before we start:
        # Adding and removing from the start of the linked list is O(1)
        #   that is because it takes the same amount of steps everytime
        # Adding to the end of the stack is O(1) but removing is O(n)
        
        # We use this knowledge to determine where to enqueue(add to q)
        # and where to dequeue(remove from q)
        # We will enqueue to the beginning of the LL(O(1)) but call it last instead of beginning
        # We will dequeue from the end of the LL(O(1)) but call it first instead of end

# Same Node constructor we used for singly linked list and stacks
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    # Method to enqueue (add to q)
        # Keep in mind that first is the start of the queue
        # Enqueue(adding to q) means adding to end of queue and changing who the last is   
    def enqueue(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length+=1
        return True
    
my_queue = Queue(1)

print('Queue before enqueue(2):')
my_queue.print_queue()

my_queue.enqueue(2)

print('\nQueue after enqueue(2):')
my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    Queue before enqueue(2):
    1

    Queue after enqueue(2):
    1
    2

"""
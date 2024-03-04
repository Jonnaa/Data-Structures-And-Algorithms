# Stack: Sort Stack ( ** Interview Question)
# The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack. 

# The function should use the pop, push, peek, and is_empty methods of the Stack object.

# Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT.

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


# The function should perform the following tasks:

# Create a new instance of the Stack class called sorted_stack.

# While the input stack is not empty, perform the following:

    # Pop the top element from the input stack and store it in a variable temp.

    # While the sorted_stack is not empty and its top element is greater than temp, pop the top element from sorted_stack and push it back onto the input stack.

    # Push the temp variable onto the sorted_stack.

# Once the input stack is empty, transfer the elements back from sorted_stack to the input stack. To do this, while sorted_stack is not empty, pop the top element from sorted_stack and push it onto the input stack.

##### WRITE SORT_STACK FUNCTION HERE #####
def sort_stack(input_stack):
    sorted_stack = Stack()
    while input_stack.is_empty()==False:
        temp = input_stack.pop()
        print("Sorted stack before while loop")
        sorted_stack.print_stack()
        print("Input stack before while loop")
        input_stack.print_stack()
        while sorted_stack.is_empty()==False and sorted_stack.peek() > temp:
            print("Sorted Stack before pop: ")
            sorted_stack.print_stack()
            input_stack.push(sorted_stack.pop())
            print("Input stack after pop: ")
        print("Sorted stack after while loop")
        sorted_stack.print_stack()
        print("Input stack after while loop")
        input_stack.print_stack()

        sorted_stack.push(temp)

    while sorted_stack.is_empty()==False:
        input_stack.push(sorted_stack.pop())
    return input_stack

# Overall, this implementation has a time complexity of O(n^2), where n is the number of elements in the original stack, because the function performs nested loops to compare all the elements with each other. However, it has the advantage of using only one additional stack, which could be useful in certain situations where memory is limited.

my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
# Stack: Reverse String ( ** Interview Question)
# The reverse_string function takes a single parameter string, which is the string you want to reverse.

# Return a new string with the letters in reverse order.

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



## WRITE REVERSE_STRING FUNCTION HERE ###
def reverse_string(str):
    # Instantiating a Stack as normal_string
    normal_string = Stack()
    # For the range of the string length, go through and push each character
    # Since the string was originally in correct order, pushing onto a stack means
    # popping will bring the characters out in reverse order
    for i in range(len(str)):
        normal_string.push(str[i])
    # normal_string.print_stack()
    # creating a string to hold the popped characters
    r_string = ""
    # For the length of the stack, go through and pop the nodes and concatenate to the string
    for i in range(normal_string.size()):
        r_string +=normal_string.pop()
    # Return the reversed string
    return r_string
#########################################




my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""

# stack definition
class Stack:
    def __init__(self):
        self.stack = []

    def print_stack(self):
        """
        Prints the stack
        """
        
        # iterate through the stack
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i], end="->")

    def push(self, value):
        """
        Pushes a new node with the given value to the top of the stack
        """
        
        self.stack.append(value)
        return True
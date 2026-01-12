# stack definition
class Stack:
    def __init__(self):
        self.stack = []

    def print_stack(self):
        """
        Prints the stack
        """
        
        # iterate through the stack
        for i in range(len(self.stack)):
            print(self.stack[i], end="->")
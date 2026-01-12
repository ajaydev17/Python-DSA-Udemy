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

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise
        """
        
        return len(self.stack) == 0

    def pop(self):
        """
        Pops the top node from the stack
        """

        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        """
        Returns the value of the top node without removing it
        """
        
        if self.is_empty():
            return None
        return self.stack[-1]
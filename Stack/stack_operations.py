# node definition
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
# stack definition
class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def print_stack(self):
        """
        Prints the stack
        """
        
        # pointer to the top node
        current = self.top
        
        # iterate through the stack while current is not None
        while current:
            print(current.value, end="->")
            current = current.next
        print("None")
        
    def push(self, value):
        """
        Pushes a new node with the given value to the top of the stack
        """
        
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
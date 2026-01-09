# node definition
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# queue definition
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def print_queue(self):
        """
        Prints the queue
        """
        
        # pointer to the first node
        current = self.first
        
        # iterate through the queue while current is not None
        while current:
            print(current.value, end="->")
            current = current.next
        print("None")
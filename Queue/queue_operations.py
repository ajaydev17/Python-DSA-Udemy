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

    def enqueue(self, value):
        """
        Enqueues a new node with the given value to the end of the queue
        """
        
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        """
        Dequeues the first node from the queue
        """
        
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp
# node definition
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
        
# linked list definition
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def print_list(self):
        """
        Prints the linked list
        """
        
        # pointer to the head node
        current = self.head
        
        # iterate through the linked list while current is not None
        while current:
            print(current.value, end="->")
            current = current.next
        print("None")
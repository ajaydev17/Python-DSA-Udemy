# node definition
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
# linked list definition
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def binary_to_decimal(self):
        """
        Converts a binary number to decimal
        """
        
        # if the list is empty, return 0
        if self.head is None:
            return 0
        
        # set the current node to the head
        current = self.head
        decimal = 0
        
        # iterate through the list while the next node is not None
        while current is not None:
            decimal = decimal * 2 + current.value
            current = current.next
            
        return decimal
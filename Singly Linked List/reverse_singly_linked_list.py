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

    def reverse(self):
        """
        Reverses the linked list in place
        """
        
        # if the list is empty, return None
        if self.length == 0:
            return None
        
        # if the list has only one node, return None
        if self.head == self.tail:
            return None
        
        # set the current and previous nodes to the head and tail respectively
        current = self.head
        previous = None
        
        # set the tail to the head
        self.tail = self.head
        
        # iterate through the list while the next node is not None
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            
        self.head = previous
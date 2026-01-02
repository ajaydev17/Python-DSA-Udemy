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
        
    def reverse_between(self, start, end):
        """
        Reverses the linked list between start and end

        Args:
            start (int): index of the first node to be reversed
            end (int): index of the last node to be reversed
        """
        
        # if the list is empty, return None
        if self.head is None:
            return None
        
        # if the start index is out of bounds, return None
        if start < 0 or start >= self.length:
            return None
        
        # if the end index is out of bounds, return None
        if end < 0 or end >= self.length:
            return None
        
        # if the start index is greater than the end index, return None
        if start > end:
            return None
        
        # create a dummy node
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy
        
        # iterate start times
        for _ in range(start):
            previous = previous.next
            
        current = previous.next
        
        # iterate end - start times
        for _ in range(end - start):
            node_to_move = current.next
            
            current.next = node_to_move.next
            node_to_move.next = previous.next
            previous.next = node_to_move
            
        self.head = dummy.next
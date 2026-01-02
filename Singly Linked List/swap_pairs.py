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
        
    def swap_pairs(self):
        """
        Swaps the pairs of nodes in the linked list
        """
        
        # if the list is empty, return None
        if self.head is None:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy
        first = self.head
        
        # iterate through the list while the next node is not None
        while first and first.next:
            second = first.next
            
            previous.next = second
            first.next = second.next
            second.next = first
            
            previous = first
            first = first.next
            
        self.head = dummy.next
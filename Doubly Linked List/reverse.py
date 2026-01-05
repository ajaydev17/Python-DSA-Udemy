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
        
    def reverse(self):
        """
        Reverses the linked list
        """
        
        if self.head is None:
            return None
        
        if self.length == 1:
            return None
            
        current = self.head
        previous = None
        
        old_head = self.head
        
        while current is not None:
            temp = current.next
            current.next = previous
            current.prev = temp
            previous = current
            current = temp
            
        self.head = previous
        self.tail = old_head
        
        self.head.prev = None
        self.tail.next = None
        
    def reverse_using_swap(self):
        """
        Reverses the linked list using swap
        """
        
        if self.head is None:
            return None
        
        if self.length == 1:
            return None
            
        current = self.head
        
        while current is not None:
            current.next, current.prev = current.prev, current.next
            current = current.prev
            
        self.head, self.tail = self.tail, self.head
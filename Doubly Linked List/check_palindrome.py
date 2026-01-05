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
        
    def check_palindrome(self):
        """
        Checks if the linked list is a palindrome
        """
        
        if self.head is None:
            return True
        
        if self.length == 1:
            return True
        
        forward = self.head
        backward = self.tail
        
        while forward != backward:
            if forward.value != backward.value:
                return False
            forward = forward.next
            backward = backward.prev
            
        return True
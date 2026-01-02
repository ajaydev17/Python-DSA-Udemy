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
        
    def check_palindrome(self):
        """
        Checks if the linked list is a palindrome
        """
        
        if self.head is None or self.head.next is None:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        previous = None
        current = slow
        
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
            
        left = self.head
        right = previous
        
        while right is not None:
            if left.value != right.value:
                return False
            left = left.next
            right = right.next
            
        return True
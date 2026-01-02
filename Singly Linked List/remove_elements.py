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
        
    def remove_elements(self, value):
        """
        Removes all nodes with the given value from the linked list
        """
        
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy
        current = self.head
        
        while current is not None:
            if current.value == value:
                previous.next = current.next
                self.length -= 1
            else:
                previous = current
            current = current.next
            
        self.head = dummy.next
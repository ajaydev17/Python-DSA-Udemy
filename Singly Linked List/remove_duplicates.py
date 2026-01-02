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
        
    def remove_duplicates_o_n2(self):
        """
        Removes duplicates from the linked list in O(n^2) time complexity
        """
        
        # if the list is empty, return None
        if self.head is None:
            return None
        
        # set the current node to the head
        current = self.head
        
        # iterate through the list while the next node is not None
        while current is not None and current.next is not None:
            runner = current
            
            while runner is not None and runner.next is not None:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
                    
            current = current.next
            
    def remove_duplicates_o_n(self):
        """
        Removes duplicates from the linked list in O(n) time complexity
        """
        
        # if the list is empty, return None
        if self.head is None:
            return None
        
        # create a set to store the values
        values = set()
        current = self.head
        previous = None
        
        # iterate through the list while the next node is not None
        while current is not None:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
                
            current = current.next
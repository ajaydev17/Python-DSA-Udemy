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
        
    def intersection(self, list1, list2):
        """
        Finds the intersection of two linked lists
        """
        
        if list1 is None or list2 is None:
            return None
        
        pointer1 = list1
        pointer2 = list2
        
        while pointer1 != pointer2:
            pointer1 = pointer1.next if pointer1 else list2
            pointer2 = pointer2.next if pointer2 else list1
            
        return pointer1
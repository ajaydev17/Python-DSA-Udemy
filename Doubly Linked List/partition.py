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
        
    def partition(self, x):
        """
        Partitions the linked list around a value x
        """
        
        if self.head is None:
            return None
        
        dummy1 = Node(0)
        dummy2 = Node(0)
        previous1 = dummy1
        previous2 = dummy2
        current = self.head
        
        while current is not None:
            if current.value < x:
                previous1.next = current
                previous1 = current
            else:
                previous2.next = current
                previous2 = current
            current = current.next
        
        if dummy1.next is None:
            previous1.next = None
            self.tail = previous1
        else:
            dummy1.next.prev = previous1
            previous1.next = dummy2.next
            dummy2.next.prev = previous1
            previous2.next = None
            self.tail = previous2
            
        self.head = dummy1.next
        self.head.prev = None
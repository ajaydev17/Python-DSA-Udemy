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
        
    def partition(self, x):
        """
        Partitions the linked list around a value x

        Args:
            x (int): value around which the linked list is to be partitioned
        """
        
        # if the list is empty, return None
        if self.head is None:
            return None
        
        # create two dummy nodes
        dummy1 = Node(0)
        dummy2 = Node(0)
        
        # set the previous1 and previous2 nodes to the dummy1 and dummy2 nodes respectively
        previous1 = dummy1
        previous2 = dummy2
        current = self.head
        
        # iterate through the list while the next node is not None
        while current is not None:
            if current.value < x:
                previous1.next = current
                previous1 = current
            else:
                previous1.next = current
                previous1 = current
                
            current = current.next
        
        # set the next of the previous1 node to the dummy2 node and set the head to the dummy1 node
        previous1.next = dummy2.next
        self.head = dummy1.next
        previous2.next = None
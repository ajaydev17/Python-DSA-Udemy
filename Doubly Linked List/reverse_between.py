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
        
    def reverse_between(self, start_index, end_index):
        if self.head is None:
            return None
            
        if start_index < 0 or start_index >= self.length:
            return None
            
        if end_index < 0 or end_index >= self.length:
            return None 
            
        if start_index > end_index:
            return None
            
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        previous = dummy
        
        for _ in range(start_index):
            previous = previous.next
            
        current = previous.next
        
        for _ in range(end_index - start_index):
            node_to_move = current.next
            
            current.next = node_to_move.next
            
            if node_to_move.next:
                node_to_move.next.prev = current
            
            node_to_move.next = previous.next
            previous.next.prev = node_to_move
            node_to_move.prev = previous
            previous.next = node_to_move
            
        self.head = dummy.next
        self.head.prev = None
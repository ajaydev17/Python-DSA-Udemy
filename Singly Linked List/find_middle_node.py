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
        
    def find_middle_node(self):
        """
        Finds the middle node of the linked list

        Returns:
            Node: middle node of the linked list
        """
        
        # if the list is empty, return None
        if self.head is None:
            return None
        
        # set the slow and fast nodes to the head and tail respectively
        slow = self.head
        fast = self.head
        
        # iterate through the list while the next node is not None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
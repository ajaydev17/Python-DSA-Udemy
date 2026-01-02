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
        
    def find_kth_to_last(self, k):
        """
        Finds the kth to last node of the linked list

        Args:
            k (int): index of the node to be found

        Returns:
            Node: kth to last node of the linked list
        """
        
        # set the slow and fast nodes to the head and tail respectively
        slow = self.head
        fast = self.head
        
        # iterate k times
        for _ in range(k):
            if fast is None:
                return None
            
            fast = fast.next
        
        # iterate until the fast node is None
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        return slow
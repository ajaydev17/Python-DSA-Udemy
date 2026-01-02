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
        
    def merge_two_lists(self, list1, list2):
        
        """
        Merges two sorted linked lists into a single sorted linked list
        """
        
        dummy = Node(0)
        previous = dummy
        
        while list1 and list2:
            if list1.value <= list2.value:
                previous.next = list1
                list1 = list1.next
            else:
                previous.next = list2
                list2 = list2.next
                
            previous = previous.next
            
        previous.next = list1 if list1 else list2
        return dummy.next
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
        
    def swap_pairs(self):
        if self.head is None or self.head.next is None:
            return

        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy

        previous = dummy
        first = self.head

        while first and first.next:
            second = first.next

            # connect previous → second
            previous.next = second
            second.prev = previous

            # connect first → node after second
            first.next = second.next
            if second.next:
                second.next.prev = first
            else:
                # updating tail when last pair is swapped
                self.tail = first

            # connect second → first
            second.next = first
            first.prev = second

            # move forward
            previous = first
            first = first.next

        self.head = dummy.next
        self.head.prev = None

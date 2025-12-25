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
        
    def print_list(self):
        """
        Prints the linked list
        """
        
        # pointer to the head node
        current = self.head
        
        # iterate through the linked list while current is not None
        while current:
            print(current.value, end="->")
            current = current.next
        print("None")
            
    def append(self, value):
        """
        Appends a value to the linked list

        Args:
            value (int): value to be appended
        """
        
        # create a new node with the given value
        new_node = Node(value)
        
        # if the linked list is empty, set the head and tail to the new node 
        # else set the tail's next to the new node and set the tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        return True
        
    def pop(self):
        """
        Pops the last value from the linked list
        
        Returns:
            int: value of the last node
        """
        
        # if the list is empty, return None
        if self.length == 0:
            return None
        
        # set the current and previous nodes to the head and tail respectively
        current = self.head
        previous = self.head
        
        # iterate through the list while the next node is not None
        while current.next is not None:
            previous = current
            current = current.next
        
        # set the tail to the previous node and set the next of the previous node to None 
        # so that the list is shorter by 1
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return current
    
    def prepend(self, value):
        """
        Prepends a value to the linked list

        Args:
            value (int): value to be prepended
        """
        
        # create a new node with the given value
        new_node = Node(value)
        
        # if the list is empty, set the head and tail to the new node 
        # else set the next of the tail to the new node and set the tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        return True
        
    def pop_first(self):
        """
        Pops the first value from the linked list

        Returns:
            int: value of the first node
        """
        
        # if the list is empty, return None
        if self.length == 0:
            return None
        
        # set the current node to the head and set the head to the next node 
        # set the next of the current node to None so that the list is shorter by 1
        current = self.head
        self.head = self.head.next
        current.next = None
        self.length -= 1
        
        # if the list is now empty, set the head and tail to None
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return current
    
    def get(self, index):
        """
        Gets the value at the given index

        Args:
            index (int): index of the value to be returned

        Returns:
            Node: node at the given index
        """
        
        # if the index is out of bounds, return None
        if index < 0 or index >= self.length:
            return None
        
        # set the current node to the head
        current = self.head
        
        # iterate through the list until the index is reached
        for _ in range(index):
            current = current.next
            
        return current
    
    def set(self, index, value):
        """
        Sets the value at the given index

        Args:
            index (int): index of the value to be set
            value (int): value to be set

        Returns:
            bool: True if the value was set, False otherwise
        """
        
        # get the node at the given index
        current = self.get(index)
        
        # if the node exists, set the value of the node and return True
        if current:
            current.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        """
        Inserts a value at the given index

        Args:
            index (int): index at which the value is to be inserted
            value (int): value to be inserted

        Returns:
            bool: True if the value was inserted, False otherwise
        """
        
        # if the index is out of bounds, return False
        if index < 0 or index >= self.length:
            return False
        
        # if the index is 0, prepend the value to the list and return True
        if index == 0:
            return self.prepend(value)
        elif index == self.length - 1:
            return self.append(value)
        
        # get the node at the previous index
        current = self.get(index - 1)
        new_node = Node(value)
        
        # if the node exists, set the next of the node to the next node 
        # set the next of the current node to the new node and increment the length by 1 and return True
        if current:
            new_node.next = current.next
            current.next = new_node
            self.length += 1
            return True
        
        return False
    
    def remove(self, index):
        """
        Removes the value at the given index

        Args:
            index (int): index of the value to be removed

        Returns:
            Node: node at the given index
        """
        
        # if the index is out of bounds, return None
        if index < 0 or index >= self.length:
            return None
        
        # if the index is 0, pop the first node and return it
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        # get the node at the previous index
        previous = self.get(index - 1)
        
        # if the node exists, set the next of the previous node to the next node 
        # set the next of the current node to None and decrement the length by 1 and return the current node
        if previous:
            target = previous.next
            previous.next = target.next
            target.next = None
            self.length -= 1
            return target
        
        return None
    
    def reverse(self):
        """
        Reverses the linked list in place
        """
        
        # if the list is empty, return None
        if self.length == 0:
            return None
        
        # if the list has only one node, return None
        if self.head == self.tail:
            return None
        
        # set the current and previous nodes to the head and tail respectively
        current = self.head
        previous = None
        
        # set the tail to the head
        self.tail = self.head
        
        # iterate through the list while the next node is not None
        while current.next is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            
        self.head = previous
        
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
    
    def has_cycle(self):
        """
        Checks if the linked list has a cycle

        Returns:
            bool: True if the linked list has a cycle, False otherwise
        """
        
        # if the list is empty, return False
        if self.head is None:
            return False
        
        # set the slow and fast nodes to the head and tail respectively
        slow = self.head
        fast = self.head
        
        # iterate through the list while the next node is not None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False
    
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
            
    def binary_to_decimal(self):
        """
        Converts a binary number to decimal
        """
        
        # if the list is empty, return 0
        if self.head is None:
            return 0
        
        # set the current node to the head
        current = self.head
        decimal = 0
        
        # iterate through the list while the next node is not None
        while current is not None:
            decimal = decimal * 2 + current.value
            current = current.next
            
        return decimal
    
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
        
    def reverse_between(self, start, end):
        """
        Reverses the linked list between start and end

        Args:
            start (int): index of the first node to be reversed
            end (int): index of the last node to be reversed
        """
        
        # if the list is empty, return None
        if self.head is None:
            return None
        
        # if the start index is out of bounds, return None
        if start < 0 or start >= self.length:
            return None
        
        # if the end index is out of bounds, return None
        if end < 0 or end >= self.length:
            return None
        
        # if the start index is greater than the end index, return None
        if start > end:
            return None
        
        # create a dummy node
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy
        
        # iterate start times
        for _ in range(start):
            previous = previous.next
            
        current = previous.next
        
        # iterate end - start times
        for _ in range(end - start):
            node_to_move = current.next
            
            current.next = node_to_move.next
            node_to_move.next = previous.next
            previous.next = node_to_move
            
        self.head = dummy.next
        
    def swap_pairs(self):
        """
        Swaps the pairs of nodes in the linked list
        """
        
        # if the list is empty, return None
        if self.head is None:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy
        first = self.head
        
        # iterate through the list while the next node is not None
        while first and first.next:
            second = first.next
            
            previous.next = second
            first.next = second.next
            second.next = first
            
            previous = first
            first = first.next
            
        self.head = dummy.next
        
        
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()

linked_list.pop()
linked_list.print_list()
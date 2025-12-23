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
        
        current = self.head
        
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
        
        new_node = Node(value)
        
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
        
        if self.length == 0:
            return None
        
        current = self.head
        previous = self.head
        
        while current.next is not None:
            previous = current
            current = current.next
            
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
        
        new_node = Node(value)
        
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
        
        if self.length == 0:
            return None
        
        current = self.head
        self.head = self.head.next
        current.next = None
        self.length -= 1
        
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
        
        if index < 0 or index >= self.length:
            return None
        
        current = self.head
        
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
        
        current = self.get(index)
        
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
        
        if index < 0 or index >= self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        elif index == self.length - 1:
            return self.append(value)
        
        current = self.get(index - 1)
        new_node = Node(value)
        
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
        
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        previous = self.get(index - 1)
        
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
        
        if self.length == 0:
            return None
        
        if self.head == self.tail:
            return None
        
        current = self.head
        previous = None
        
        self.tail = self.head
        
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
        
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head
        
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
        
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head
        
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
        
        slow = self.head
        fast = self.head
        
        for _ in range(k):
            if fast is None:
                return None
            
            fast = fast.next
            
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        return slow
    
    def remove_duplicates_o_n2(self):
        """
        Removes duplicates from the linked list in O(n^2) time complexity
        """
        
        if self.head is None:
            return None
        
        current = self.head
        
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
        
        if self.head is None:
            return None
        
        values = set()
        current = self.head
        previous = None
        
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
        
        if self.head is None:
            return 0
        
        current = self.head
        decimal = 0
        
        while current is not None:
            decimal = decimal * 2 + current.value
            current = current.next
            
        return decimal
        
        
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()

linked_list.pop()
linked_list.print_list()
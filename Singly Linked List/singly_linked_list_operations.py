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
        if index < 0 or index > self.length:
            return False
        
        # if the index is 0, prepend the value to the list and return True
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
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
    
    
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()

linked_list.pop()
linked_list.print_list()
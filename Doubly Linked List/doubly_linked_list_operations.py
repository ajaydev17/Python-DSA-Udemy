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
        Appends a new node to the end of the linked list
        """
        
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        """
        Pops the last node from the linked list
        """
        
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        """
        Prepends a new node to the beginning of the linked list
        """
        
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        """
        Pops the first node from the linked list
        """
        
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        """
        Gets the node at the given index
        """
        
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
            return current
        
    def set(self, index, value):
        """
        Sets the value at the given index
        """
        
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        """
        Inserts a new node with the given value at the given index
        """
        
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        
        new_node.next = after
        new_node.prev = before
        after.prev = new_node
        before.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        """
        Removes the node at the given index
        """
        
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
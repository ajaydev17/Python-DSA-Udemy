class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        """
        Adds an element to the end of the queue
        """
        
        if len(self.stack1) == 0:
            self.stack1.append(value)
        else:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

            self.stack1.append(value)

            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())
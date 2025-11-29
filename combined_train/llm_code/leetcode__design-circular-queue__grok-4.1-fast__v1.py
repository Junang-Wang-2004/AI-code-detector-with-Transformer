class C1:

    def __init__(self, a1):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [0] * a1
        self.head = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, a1):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == len(self.data):
            return False
        self.rear = (self.rear + 1) % len(self.data)
        self.data[self.rear] = a1
        self.count += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.head = (self.head + 1) % len(self.data)
        self.count -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        """
        return -1 if self.count == 0 else self.data[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        """
        return -1 if self.count == 0 else self.data[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == len(self.data)

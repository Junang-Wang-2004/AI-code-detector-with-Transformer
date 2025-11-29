class MyCircularDeque:

    def __init__(self, k):
        self.capacity = k
        self.storage = [0] * k
        self.head = 0
        self.tail = 0
        self.length = 0

    def insertFront(self, value):
        if self.length == self.capacity:
            return False
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.storage[self.head] = value
        self.length += 1
        return True

    def insertLast(self, value):
        if self.length == self.capacity:
            return False
        self.storage[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.length += 1
        return True

    def deleteFront(self):
        if self.length == 0:
            return False
        self.head = (self.head + 1) % self.capacity
        self.length -= 1
        return True

    def deleteLast(self):
        if self.length == 0:
            return False
        self.tail = (self.tail - 1 + self.capacity) % self.capacity
        self.length -= 1
        return True

    def getFront(self):
        if self.length == 0:
            return -1
        return self.storage[self.head]

    def getRear(self):
        if self.length == 0:
            return -1
        rear_idx = (self.tail - 1 + self.capacity) % self.capacity
        return self.storage[rear_idx]

    def isEmpty(self):
        return self.length == 0

    def isFull(self):
        return self.length == self.capacity

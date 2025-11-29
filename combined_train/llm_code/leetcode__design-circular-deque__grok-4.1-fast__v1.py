class C1:

    def __init__(self, a1):
        self.capacity = a1
        self.storage = [0] * a1
        self.head = 0
        self.tail = 0
        self.length = 0

    def insertFront(self, a1):
        if self.length == self.capacity:
            return False
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.storage[self.head] = a1
        self.length += 1
        return True

    def insertLast(self, a1):
        if self.length == self.capacity:
            return False
        self.storage[self.tail] = a1
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
        v1 = (self.tail - 1 + self.capacity) % self.capacity
        return self.storage[v1]

    def isEmpty(self):
        return self.length == 0

    def isFull(self):
        return self.length == self.capacity

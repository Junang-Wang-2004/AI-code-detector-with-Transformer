class C1(object):

    def __init__(self, a1):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.__start = 0
        self.__size = 0
        self.__buffer = [0] * a1

    def enQueue(self, a1):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.__buffer[(self.__start + self.__size) % len(self.__buffer)] = a1
        self.__size += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.__start = (self.__start + 1) % len(self.__buffer)
        self.__size -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        """
        return -1 if self.isEmpty() else self.__buffer[self.__start]

    def Rear(self):
        """
        Get the last item from the queue.
        """
        return -1 if self.isEmpty() else self.__buffer[(self.__start + self.__size - 1) % len(self.__buffer)]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        return self.__size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return self.__size == len(self.__buffer)

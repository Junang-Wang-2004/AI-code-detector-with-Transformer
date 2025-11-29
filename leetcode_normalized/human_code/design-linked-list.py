class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = self.prev = None

class C2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__head = self.__tail = C1(-1)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def get(self, a1):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0 <= a1 <= self.__size // 2:
            return self.__forward(0, a1, self.__head.__next__).val
        elif self.__size // 2 < a1 < self.__size:
            return self.__backward(self.__size, a1, self.__tail).val
        return -1

    def addAtHead(self, a1):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        self.__add(self.__head, a1)

    def addAtTail(self, a1):
        """
        Append a node of value val to the last element of the linked list.
        """
        self.__add(self.__tail.prev, a1)

    def addAtIndex(self, a1, a2):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if 0 <= a1 <= self.__size // 2:
            self.__add(self.__forward(0, a1, self.__head.__next__).prev, a2)
        elif self.__size // 2 < a1 <= self.__size:
            self.__add(self.__backward(self.__size, a1, self.__tail).prev, a2)

    def deleteAtIndex(self, a1):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= a1 <= self.__size // 2:
            self.__remove(self.__forward(0, a1, self.__head.__next__))
        elif self.__size // 2 < a1 < self.__size:
            self.__remove(self.__backward(self.__size, a1, self.__tail))

    def __add(self, a1, a2):
        v1 = C1(a2)
        v1.prev = a1
        v1.next = a1.__next__
        v1.prev.next = v1.next.prev = v1
        self.__size += 1

    def __remove(self, a1):
        a1.prev.next = a1.__next__
        a1.next.prev = a1.prev
        self.__size -= 1

    def __forward(self, a1, a2, a3):
        while a1 != a2:
            a1 += 1
            a3 = a3.__next__
        return a3

    def __backward(self, a1, a2, a3):
        while a1 != a2:
            a1 -= 1
            a3 = a3.prev
        return a3

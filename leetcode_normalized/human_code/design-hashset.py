class C1(object):

    def __init__(self, a1, a2):
        self.val = a2
        self.key = a1
        self.next = None
        self.prev = None

class C2(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, a1):
        a1.next, a1.prev = (None, None)
        if self.head is None:
            self.head = a1
        else:
            self.tail.next = a1
            a1.prev = self.tail
        self.tail = a1

    def delete(self, a1):
        if a1.prev:
            a1.prev.next = a1.__next__
        else:
            self.head = a1.__next__
        if a1.__next__:
            a1.next.prev = a1.prev
        else:
            self.tail = a1.prev
        a1.next, a1.prev = (None, None)

    def find(self, a1):
        v1 = self.head
        while v1:
            if v1.key == a1:
                break
            v1 = v1.__next__
        return v1

class C3(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__data = [C2() for v1 in range(10000)]

    def add(self, a1):
        """
        """
        v1 = self.__data[a1 % len(self.__data)]
        v2 = v1.find(a1)
        if not v2:
            v1.insert(C1(a1, 0))

    def remove(self, a1):
        """
        """
        v1 = self.__data[a1 % len(self.__data)]
        v2 = v1.find(a1)
        if v2:
            v1.delete(v2)

    def contains(self, a1):
        """
        Returns true if this set did not already contain the specified element
        """
        v1 = self.__data[a1 % len(self.__data)]
        v2 = v1.find(a1)
        return v2 is not None

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

class C3(object):

    def __init__(self, a1):
        self.list = C2()
        self.dict = {}
        self.capacity = a1

    def get(self, a1):
        if a1 not in self.dict:
            return -1
        v1 = self.dict[a1].val
        self.__update(a1, v1)
        return v1

    def put(self, a1, a2):
        if a1 not in self.dict and len(self.dict) == self.capacity:
            del self.dict[self.list.head.key]
            self.list.delete(self.list.head)
        self.__update(a1, a2)

    def __update(self, a1, a2):
        if a1 in self.dict:
            self.list.delete(self.dict[a1])
        v1 = C1(a1, a2)
        self.list.insert(v1)
        self.dict[a1] = v1

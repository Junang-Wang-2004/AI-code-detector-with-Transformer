class C1(object):
    """
    double linked list node
    """

    def __init__(self, a1, a2):
        self.value = a1
        self.keys = a2
        self.prev = None
        self.next = None

class C2(object):

    def __init__(self):
        self.head, self.tail = (C1(0, set()), C1(0, set()))
        self.head.next, self.tail.prev = (self.tail, self.head)

    def insert(self, a1, a2):
        a2.prev, a2.next = (a1.prev, a1)
        a1.prev.next, a1.prev = (a2, a2)
        return a2

    def erase(self, a1):
        a1.prev.next, a1.next.prev = (a1.__next__, a1.prev)
        del a1

    def empty(self):
        return self.head.__next__ is self.tail

    def begin(self):
        return self.head.__next__

    def end(self):
        return self.tail

    def front(self):
        return self.head.__next__

    def back(self):
        return self.tail.prev

class C3(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_of_key = {}
        self.buckets = C2()

    def inc(self, a1):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if a1 not in self.bucket_of_key:
            self.bucket_of_key[a1] = self.buckets.insert(self.buckets.begin(), C1(0, set([a1])))
        v1, v2 = (self.bucket_of_key[a1], self.bucket_of_key[a1].__next__)
        if v2 is self.buckets.end() or v2.value > v1.value + 1:
            v2 = self.buckets.insert(v2, C1(v1.value + 1, set()))
        v2.keys.add(a1)
        self.bucket_of_key[a1] = v2
        v1.keys.remove(a1)
        if not v1.keys:
            self.buckets.erase(v1)

    def dec(self, a1):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if a1 not in self.bucket_of_key:
            return
        v1, v2 = (self.bucket_of_key[a1], self.bucket_of_key[a1].prev)
        self.bucket_of_key.pop(a1, None)
        if v1.value > 1:
            if v1 is self.buckets.begin() or v2.value < v1.value - 1:
                v2 = self.buckets.insert(v1, C1(v1.value - 1, set()))
            v2.keys.add(a1)
            self.bucket_of_key[a1] = v2
        v1.keys.remove(a1)
        if not v1.keys:
            self.buckets.erase(v1)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        """
        if self.buckets.empty():
            return ''
        return next(iter(self.buckets.back().keys))

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        """
        if self.buckets.empty():
            return ''
        return next(iter(self.buckets.front().keys))

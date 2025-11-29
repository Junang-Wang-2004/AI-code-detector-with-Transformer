class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, self.__next__)

class C2(object):

    def swapPairs(self, a1):
        v1 = C1(0)
        v1.next = a1
        v2 = v1
        while v2.__next__ and v2.next.__next__:
            v3, v4, v5 = (v2.__next__, v2.next.__next__, v2.next.next.__next__)
            v2.next = v4
            v4.next = v3
            v3.next = v5
            v2 = v3
        return v1.__next__

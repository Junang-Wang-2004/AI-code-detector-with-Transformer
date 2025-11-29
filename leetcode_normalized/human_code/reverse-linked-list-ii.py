class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, repr(self.__next__))

class C2(object):

    def reverseBetween(self, a1, a2, a3):
        v1, v2, v3 = (a3 - a2 + 1, C1(-1), a1)
        v2.next = a1
        v4 = v2
        while v3 and a2 > 1:
            v3, v4, a2 = (v3.__next__, v3, a2 - 1)
        v6, v7 = (v4, v3)
        while v3 and v1 > 0:
            v3.next, v6, v3, v1 = (v6, v3, v3.next, v1 - 1)
        v4.next, v7.next = (v6, v3)
        return v2.__next__

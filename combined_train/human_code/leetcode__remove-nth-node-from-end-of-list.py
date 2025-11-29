class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self is None:
            return 'Nil'
        else:
            return '{} -> {}'.format(self.val, repr(self.__next__))

class C2(object):

    def removeNthFromEnd(self, a1, a2):
        v1 = C1(-1)
        v1.next = a1
        v2, v3 = (v1, v1)
        for v4 in range(a2):
            v3 = v3.__next__
        while v3.__next__:
            v2, v3 = (v2.__next__, v3.__next__)
        v2.next = v2.next.__next__
        return v1.__next__

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, repr(self.__next__))
        else:
            return 'Nil'

class C2(object):

    def insertionSortList(self, a1):
        if a1 is None or self.isSorted(a1):
            return a1
        v1 = C1(-2147483648)
        v1.next = a1
        v2, v3 = (a1.__next__, a1)
        while v2:
            v4 = v1
            while v4.next.val < v2.val:
                v4 = v4.__next__
            if v4 == v3:
                v2, v3 = (v2.__next__, v2)
            else:
                v2.next, v4.next, v3.next = (v4.next, v2, v2.next)
                v2 = v3.__next__
        return v1.__next__

    def isSorted(self, a1):
        while a1 and a1.__next__:
            if a1.val > a1.next.val:
                return False
            a1 = a1.__next__
        return True

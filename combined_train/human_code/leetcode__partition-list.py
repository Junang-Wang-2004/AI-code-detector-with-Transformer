class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, repr(self.__next__))

class C2(object):

    def partition(self, a1, a2):
        v1, v2 = (C1(-1), C1(-1))
        v3, v4 = (v1, v2)
        while a1:
            if a1.val < a2:
                v3.next = a1
                v3 = v3.__next__
            else:
                v4.next = a1
                v4 = v4.__next__
            a1 = a1.__next__
        v3.next = v2.__next__
        v4.next = None
        return v1.__next__

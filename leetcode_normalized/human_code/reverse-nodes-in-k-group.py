class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, repr(self.__next__))

class C2(object):

    def reverseKGroup(self, a1, a2):
        v1 = C1(-1)
        v1.next = a1
        v2, v3 = (a1, v1)
        v4 = 0
        while v2:
            v5 = v2.__next__
            v4 = (v4 + 1) % a2
            if v4 == 0:
                v6 = v3.__next__
                self.reverse(v3, v2.__next__)
                v3 = v6
            v2 = v5
        return v1.__next__

    def reverse(self, a1, a2):
        v1 = a1.__next__
        v2 = v1.__next__
        while v2 != a2:
            v1.next = v2.__next__
            v2.next = a1.__next__
            a1.next = v2
            v2 = v1.__next__

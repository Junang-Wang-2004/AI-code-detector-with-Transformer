class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, repr(self.__next__))

class C2(object):

    def rotateRight(self, a1, a2):
        """
        """
        if not a1 or not a1.__next__:
            return a1
        v1, v2 = (1, a1)
        while v2.__next__:
            v2 = v2.__next__
            v1 += 1
        v2.next = a1
        v2, v3 = (a1, v2)
        for v4 in range(v1 - a2 % v1):
            v3 = v2
            v2 = v2.__next__
        v3.next = None
        return v2

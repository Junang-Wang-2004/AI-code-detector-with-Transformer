class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, repr(self.__next__))

class C2(object):

    def reverseList(self, a1):
        v1 = C1(float('-inf'))
        while a1:
            v1.next, a1.next, a1 = (a1, v1.next, a1.next)
        return v1.__next__

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, self.__next__)

class C2(object):

    def mergeTwoLists(self, a1, a2):
        """
        """
        v1 = v2 = C1(0)
        while a1 and a2:
            if a1.val < a2.val:
                v1.next = a1
                a1 = a1.__next__
            else:
                v1.next = a2
                a2 = a2.__next__
            v1 = v1.__next__
        v1.next = a1 or a2
        return v2.__next__

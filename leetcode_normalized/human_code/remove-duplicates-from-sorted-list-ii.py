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

    def deleteDuplicates(self, a1):
        """
        """
        v1 = C1(0)
        v2, v3 = (v1, a1)
        while v3:
            if v3.__next__ and v3.next.val == v3.val:
                v4 = v3.val
                while v3 and v3.val == v4:
                    v3 = v3.__next__
                v2.next = v3
            else:
                v2.next = v3
                v2 = v3
                v3 = v3.__next__
        return v1.__next__

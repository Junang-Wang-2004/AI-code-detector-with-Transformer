class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, self.__next__)

class C2(object):

    def mergeKLists(self, a1):
        """
        """

        def mergeTwoLists(a1, a2):
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
        if not a1:
            return None
        v1, v2 = (0, len(a1) - 1)
        while v2 > 0:
            a1[v1] = mergeTwoLists(a1[v1], a1[v2])
            v1 += 1
            v2 -= 1
            if v1 >= v2:
                v1 = 0
        return a1[0]

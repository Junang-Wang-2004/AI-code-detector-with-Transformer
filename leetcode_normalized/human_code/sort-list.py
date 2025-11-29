class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, repr(self.__next__))

class C2(object):

    def sortList(self, a1):
        if a1 == None or a1.__next__ == None:
            return a1
        v1, v2, v3 = (a1, a1, None)
        while v1 != None and v1.__next__ != None:
            v3, v1, v2 = (v2, v1.next.__next__, v2.__next__)
        v3.next = None
        v4 = self.sortList(a1)
        v5 = self.sortList(v2)
        return self.mergeTwoLists(v4, v5)

    def mergeTwoLists(self, a1, a2):
        v1 = C1(0)
        v2 = v1
        while a1 != None and a2 != None:
            if a1.val <= a2.val:
                v2.next, v2, a1 = (a1, a1, a1.__next__)
            else:
                v2.next, v2, a2 = (a2, a2, a2.__next__)
        if a1 != None:
            v2.next = a1
        if a2 != None:
            v2.next = a2
        return v1.__next__

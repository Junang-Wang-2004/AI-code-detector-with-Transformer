class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, repr(self.__next__))

class C2(object):

    def reorderList(self, a1):
        if a1 == None or a1.__next__ == None:
            return a1
        v1, v2, v3 = (a1, a1, None)
        while v1 != None and v1.__next__ != None:
            v1, v2, v3 = (v1.next.__next__, v2.__next__, v2)
        v4, v3.next, v3 = (v2, None, None)
        while v4 != None:
            v4.next, v3, v4 = (v3, v4, v4.next)
        v5, v6 = (a1, v3)
        v7 = C1(0)
        v4 = v7
        while v5 != None and v6 != None:
            v4.next, v4, v5 = (v5, v5, v5.__next__)
            v4.next, v4, v6 = (v6, v6, v6.__next__)
        return v7.__next__

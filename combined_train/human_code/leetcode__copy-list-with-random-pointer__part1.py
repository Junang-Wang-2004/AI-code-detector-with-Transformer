class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None
        self.random = None

class C2(object):

    def copyRandomList(self, a1):
        v1 = a1
        while v1:
            v2 = C1(v1.val)
            v2.next = v1.__next__
            v1.next = v2
            v1 = v2.__next__
        v1 = a1
        while v1:
            if v1.random:
                v1.next.random = v1.random.__next__
            v1 = v1.next.__next__
        v3 = C1(0)
        v4, v1 = (v3, a1)
        while v1:
            v4.next = v1.__next__
            v1.next = v1.next.__next__
            v4, v1 = (v4.__next__, v1.__next__)
        return v3.__next__

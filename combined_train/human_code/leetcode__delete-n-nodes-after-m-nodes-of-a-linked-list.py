class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def deleteNodes(self, a1, a2, a3):
        """
        """
        a1 = v2 = C1(next=a1)
        while a1:
            for v3 in range(a2):
                if not a1.__next__:
                    return v2.__next__
                a1 = a1.__next__
            v4 = a1
            for v3 in range(a3):
                if not a1.__next__:
                    v4.next = None
                    return v2.__next__
                a1 = a1.__next__
            v4.next = a1.__next__
        return v2.__next__

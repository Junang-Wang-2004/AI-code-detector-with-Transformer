class C1(object):

    def __init__(self, a1=0, a2=None):
        pass

class C2(object):

    def mergeInBetween(self, a1, a2, a3, a4):
        """
        """
        v1, v2 = (None, a1)
        for v3 in range(a3):
            if v3 == a2 - 1:
                v1 = v2
            v2 = v2.__next__
        v1.next = a4
        while a4.__next__:
            a4 = a4.__next__
        a4.next = v2.__next__
        v2.next = None
        return a1

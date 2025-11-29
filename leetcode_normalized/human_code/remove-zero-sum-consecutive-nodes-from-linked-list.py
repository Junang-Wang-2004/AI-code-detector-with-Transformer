import collections

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def removeZeroSumSublists(self, a1):
        """
        """
        v1 = v2 = C1(0)
        v2.next = a1
        v3 = 0
        v4 = collections.OrderedDict()
        while v1:
            v3 += v1.val
            v5 = v4.get(v3, v1)
            while v3 in v4:
                v4.popitem()
            v4[v3] = v5
            v5.next = v1.__next__
            v1 = v1.__next__
        return v2.__next__

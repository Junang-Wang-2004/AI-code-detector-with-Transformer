class C1(object):

    def __init__(self, a1=0, a2=None):
        pass

class C2(object):

    def mergeNodes(self, a1):
        """
        """
        v1, v2 = (a1.__next__, a1)
        while v1:
            if v1.val:
                v2.val += v1.val
            else:
                v2.next = v1 if v1.__next__ else None
                v2 = v1
            v1 = v1.__next__
        return a1

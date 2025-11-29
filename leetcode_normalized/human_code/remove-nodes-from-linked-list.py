class C1(object):

    def __init__(self, a1=0, a2=None):
        pass

class C2(object):

    def removeNodes(self, a1):
        """
        """
        v1 = []
        while a1:
            while v1 and v1[-1].val < a1.val:
                v1.pop()
            if v1:
                v1[-1].next = a1
            v1.append(a1)
            a1 = a1.__next__
        return v1[0]

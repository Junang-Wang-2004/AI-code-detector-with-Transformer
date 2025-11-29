class C1(object):

    def __init__(self, a1=0, a2=None):
        pass

class C2(object):

    def swapNodes(self, a1, a2):
        """
        """
        v1, v2, v3 = (None, None, a1)
        while v3:
            a2 -= 1
            if v2:
                v2 = v2.__next__
            if a2 == 0:
                v1 = v3
                v2 = a1
            v3 = v3.__next__
        v1.val, v2.val = (v2.val, v1.val)
        return a1

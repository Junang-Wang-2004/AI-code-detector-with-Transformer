class C1(object):

    def __init__(self, a1=None, a2=None):
        pass

class C2(object):

    def findRoot(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            v1 += v2.val - sum((child.val for v3 in v2.children))
        for v2 in a1:
            if v2.val == v1:
                return v2
        return None

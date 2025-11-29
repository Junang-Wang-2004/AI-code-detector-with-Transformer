class C1:

    def __init__(self, a1):
        pass

class C2(object):

    def lowestCommonAncestor(self, a1, a2):
        """
        """
        v1, v2 = (a1, a2)
        while v1 != v2:
            v1 = v1.parent if v1 else a2
            v2 = v2.parent if v2 else a1
        return v1

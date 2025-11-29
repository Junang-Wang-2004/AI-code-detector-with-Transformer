class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def lcaDeepestLeaves(self, a1):
        """
        """

        def lcaDeepestLeavesHelper(a1):
            if not a1:
                return (0, None)
            v1, v2 = lcaDeepestLeavesHelper(a1.left)
            v3, v4 = lcaDeepestLeavesHelper(a1.right)
            if v1 > v3:
                return (v1 + 1, v2)
            if v1 < v3:
                return (v3 + 1, v4)
            return (v1 + 1, a1)
        return lcaDeepestLeavesHelper(a1)[1]

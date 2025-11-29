class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def buildTree(self, a1, a2):
        """
        """
        v1 = iter(a1)
        v2 = {n: i for v3, v4 in enumerate(a2)}

        def helper(a1, a2):
            if a1 > a2:
                return None
            v1 = next(v1)
            v2 = C1(v1)
            v3 = v2[v1]
            v2.left = helper(a1, v3 - 1)
            v2.right = helper(v3 + 1, a2)
            return v2
        return helper(0, len(a2) - 1)

class C1(object):

    def __init__(self, a1, a2, a3, a4, a5, a6):
        self.val = a1
        self.isLeaf = a2
        self.topLeft = a3
        self.topRight = a4
        self.bottomLeft = a5
        self.bottomRight = a6

class C2(object):

    def construct(self, a1):
        """
        """

        def dfs(a1, a2, a3, a4):
            if a4 == 1:
                return C1(a1[a2][a3] == 1, True, None, None, None, None)
            v1 = a4 // 2
            v2 = dfs(a1, a2, a3, v1)
            v3 = dfs(a1, a2, a3 + v1, v1)
            v4 = dfs(a1, a2 + v1, a3, v1)
            v5 = dfs(a1, a2 + v1, a3 + v1, v1)
            if v2.isLeaf and v3.isLeaf and v4.isLeaf and v5.isLeaf and (v2.val == v3.val == v4.val == v5.val):
                return C1(v2.val, True, None, None, None, None)
            return C1(True, False, v2, v3, v4, v5)
        if not a1:
            return None
        return dfs(a1, 0, 0, len(a1))

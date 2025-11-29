class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def lcaDeepestLeaves(self, a1):

        def dfs(a1):
            if not a1:
                return (0, None)
            v1, v2 = dfs(a1.left)
            v3, v4 = dfs(a1.right)
            v5 = max(v1, v3)
            if v1 == v5 and v3 == v5:
                return (v5 + 1, a1)
            if v1 == v5:
                return (v5 + 1, v2)
            return (v5 + 1, v4)
        return dfs(a1)[1]

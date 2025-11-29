import collections

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maxLevelSum(self, a1):
        """
        """

        def dfs(a1, a2, a3):
            if not a1:
                return
            if a2 == len(a3):
                a3.append(0)
            a3[a2] += a1.val
            dfs(a1.left, a2 + 1, a3)
            dfs(a1.right, a2 + 1, a3)
        v1 = []
        dfs(a1, 0, v1)
        return v1.index(max(v1)) + 1

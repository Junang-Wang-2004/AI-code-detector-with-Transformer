class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass
import collections

class C2(object):

    def minimumFlips(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = {2: lambda x, y: x or y, 3: lambda x, y: x and y, 4: lambda x, y: x ^ y, 5: lambda x, y: not x if x is not None else not y}

        def dfs(a1):
            if not a1:
                return {None: 0}
            if a1.left == a1.right:
                return {True: a1.val ^ 1, False: a1.val ^ 0}
            v1 = dfs(a1.left)
            v2 = dfs(a1.right)
            v3 = collections.defaultdict(lambda: v1)
            for v4, v5 in v1.items():
                for v6, v7 in v2.items():
                    v3[v2[a1.val](v4, v6)] = min(v3[v2[a1.val](v4, v6)], v5 + v7)
            return v3
        return dfs(a1)[a2]

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

        def iter_dfs(a1, a2):
            v1 = collections.defaultdict(lambda: v1)
            v2 = [(1, (a1, v1))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v1 = v4
                    if not v5:
                        v1[None] = 0
                        continue
                    if v5.left == v5.right:
                        v1[True] = v5.val ^ 1
                        v1[False] = v5.val ^ 0
                        continue
                    v6 = collections.defaultdict(lambda: v1)
                    v7 = collections.defaultdict(lambda: v1)
                    v2.append((2, (v5, v6, v7, v1)))
                    v2.append((1, (v5.right, v7)))
                    v2.append((1, (v5.left, v6)))
                elif v3 == 2:
                    v5, v6, v7, v1 = v4
                    for v8, v9 in v6.items():
                        for v10, v11 in v7.items():
                            v1[v2[v5.val](v8, v10)] = min(v1[v2[v5.val](v8, v10)], v9 + v11)
            return v1[a2]
        return iter_dfs(a1, a2)
import collections

import collections

class C1(object):

    def countPairs(self, a1, a2):
        """
        """

        def dfs(a1, a2):
            if not a2:
                return (0, collections.Counter())
            if not a2.left and (not a2.right):
                return (0, collections.Counter([0]))
            v1, v2 = (dfs(a1, a2.left), dfs(a1, a2.right))
            v3 = v1[0] + v2[0]
            for v4, v5 in v1[1].items():
                for v6, v7 in v2[1].items():
                    if v4 + v6 + 2 <= a1:
                        v3 += v5 * v7
            return (v3, collections.Counter({k + 1: v for v8, v9 in (v1[1] + v2[1]).items()}))
        return dfs(a2, a1)[0]

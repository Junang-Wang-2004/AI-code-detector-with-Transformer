import collections

class C1(object):

    def sumOfDistancesInTree(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4, a5):
            for v1 in a1[a2]:
                if v1 != a3:
                    dfs(a1, v1, a2, a4, a5)
                    a4[a2] += a4[v1]
                    a5[a2] += a5[v1] + a4[v1]

        def dfs2(a1, a2, a3, a4, a5):
            for v1 in a1[a2]:
                if v1 != a3:
                    a5[v1] = a5[a2] - a4[v1] + len(a4) - a4[v1]
                    dfs2(a1, v1, a2, a4, a5)
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = [1] * a1
        v5 = [0] * a1
        dfs(v1, 0, None, v4, v5)
        dfs2(v1, 0, None, v4, v5)
        return v5

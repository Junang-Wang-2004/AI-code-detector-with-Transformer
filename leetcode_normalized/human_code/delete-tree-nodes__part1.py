import collections

class C1(object):

    def deleteTreeNodes(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3):
            v1, v2 = (a1[a3], 1)
            for v3 in a2[a3]:
                v4, v5 = dfs(a1, a2, v3)
                v1 += v4
                v2 += v5 if v4 else 0
            return (v1, v2 if v1 else 0)
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a2):
            if v2:
                v1[v3].append(v2)
        return dfs(a3, v1, 0)[1]

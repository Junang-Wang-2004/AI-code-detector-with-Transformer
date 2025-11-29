from functools import reduce

class C1(object):

    def minimumScore(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3):
            v1 = a1[a1]
            for v2 in adj[a1]:
                if v2 == a2:
                    continue
                v1 ^= dfs(v2, a1, a3)
            a3.append(v1)
            return v1
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = reduce(lambda x, y: x ^ y, a1)
        v6 = float('inf')
        for v3, v4 in a2:
            v7 = []
            dfs(v3, v4, v7)
            v8 = []
            dfs(v4, v3, v8)
            for v9 in (v7, v8):
                v10 = v9.pop()
                for v11 in v9:
                    v12, v13, v14 = (v5 ^ v10, v11, v10 ^ v11)
                    v6 = min(v6, max(v12, v13, v14) - min(v12, v13, v14))
        return v6

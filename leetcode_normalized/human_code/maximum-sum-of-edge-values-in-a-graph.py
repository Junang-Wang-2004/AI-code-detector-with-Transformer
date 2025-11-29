"""
n = 11
edges = [[0,1],[1,2],[2,3],[5,6],[6,7]]
max is 367 but ans is 366, which is wrong by greedy
"""

class C1(object):

    def maxScore(self, a1, a2):
        """
        """

        def bfs(a1):
            lookup[a1] = True
            v1 = [a1]
            for a1 in v1:
                for v3 in adj[a1]:
                    if lookup[v3]:
                        continue
                    lookup[v3] = True
                    v1.append(v3)
            return v1

        def f(a1, a2, a3):
            v1 = v2 = a2
            v3 = 0
            for v4 in reversed(range(a1, a2)):
                v3 += v1 * v4
                v1, v2 = (v2, v4)
            if a3:
                v3 += v1 * v2
            return v3
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5, v6 = ([], [])
        v7 = [False] * a1
        for v3 in range(a1):
            if v7[v3]:
                continue
            v8 = bfs(v3)
            if all((len(v1[x]) == 2 for v9 in v8)):
                v5.append(len(v8))
            else:
                v6.append(len(v8))
        v10 = 0
        for v11 in v5:
            v10 += f(a1 - v11 + 1, a1, True)
            a1 -= v11
        v13 = [0] * ((max(v6) if v6 else 0) + 1)
        for v11 in v6:
            v13[v11] += 1
        for v11 in reversed(range(len(v13))):
            for v2 in range(v13[v11]):
                v10 += f(a1 - v11 + 1, a1, False)
                a1 -= v11
        return v10

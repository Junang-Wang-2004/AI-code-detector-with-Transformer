class C1(object):

    def mostProfitablePath(self, a1, a2, a3):
        """
        """

        def iter_dfs():
            v1 = [[float('-inf'), float('inf')] for v2 in range(len(adj))]
            v3 = [(1, (0, -1, 0))]
            while v3:
                v4, (v5, v6, v7) = v3.pop()
                if v4 == 1:
                    v3.append((2, (v5, v6, v7)))
                    for v8 in adj[v5]:
                        if v8 == v6:
                            continue
                        v3.append((1, (v8, v5, v7 + 1)))
                elif v4 == 2:
                    if len(adj[v5]) + (v5 == 0) == 1:
                        v1[v5][0] = 0
                    if v5 == a2:
                        v1[v5][1] = 0
                    for v8 in adj[v5]:
                        if v8 == v6:
                            continue
                        v1[v5][0] = max(v1[v5][0], v1[v8][0])
                        v1[v5][1] = min(v1[v5][1], v1[v8][1])
                    if v7 == v1[v5][1]:
                        v1[v5][0] += a3[v5] // 2
                    elif v7 < v1[v5][1]:
                        v1[v5][0] += a3[v5]
                    v1[v5][1] += 1
            return v1[0][0]
        v1 = [[] for v2 in range(len(a1) + 1)]
        v3 = [False] * len(v1)
        for v4, v5 in a1:
            v1[v4].append(v5)
            v1[v5].append(v4)
        return iter_dfs()

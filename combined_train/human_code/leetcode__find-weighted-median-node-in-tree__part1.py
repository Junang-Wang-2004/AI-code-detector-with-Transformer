class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1

    def find_set(self, a1):
        v1 = []
        while self.set[a1] != a1:
            v1.append(a1)
            a1 = self.set[a1]
        while v1:
            self.set[v1.pop()] = a1
        return a1

    def union_set(self, a1, a2):
        a1, a2 = (self.find_set(a1), self.find_set(a2))
        if a1 == a2:
            return False
        if self.rank[a1] > self.rank[a2]:
            a1, a2 = (a2, a1)
        self.set[a1] = self.set[a2]
        if self.rank[a1] == self.rank[a2]:
            self.rank[a2] += 1
        return True

def f3(a1, a2, a3):
    while a1 <= a2:
        v1 = a1 + (a2 - a1) // 2
        if a3(v1):
            a2 = v1 - 1
        else:
            a1 = v1 + 1
    return a1

class C2(object):

    def findMedian(self, a1, a2, a3):
        """
        """

        def iter_dfs():
            v1 = [False] * len(adj)
            v2 = [[] for v3 in range(len(adj))]
            for v4, v5 in enumerate(a3):
                for v6 in v5:
                    v2[v6].append(v4)
            v7 = C1(len(adj))
            v8 = list(range(len(adj)))
            v9 = [0] * len(adj)
            v10 = [0] * len(adj)
            v11 = [0] * len(a3)
            v12 = [0] * len(a3)
            v13 = [(1, (0,))]
            while v13:
                v14, v15 = v13.pop()
                if v14 == 1:
                    v16 = v15[0]
                    for v4 in v2[v16]:
                        if a3[v4][0] == a3[v4][1]:
                            v11[v4] = v16
                            continue
                        v12[v4] += v10[v16]
                        for v6 in a3[v4]:
                            if v1[v6]:
                                v11[v4] = v8[v7.find_set(v6)]
                                v12[v4] -= 2 * v10[v11[v4]]
                    v1[v16] = True
                    v13.append((2, (v16, 0)))
                elif v14 == 2:
                    v16, v4 = v15
                    if v4 == len(adj[v16]):
                        continue
                    v17, v18 = adj[v16][v4]
                    v13.append((2, (v16, v4 + 1)))
                    if v1[v17]:
                        continue
                    v10[v17] = v10[v16] + v18
                    v9[v17] = v9[v16] + 1
                    v13.append((3, (v17, v16)))
                    v13.append((1, (v17, v16)))
                elif v14 == 3:
                    v17, v16 = v15
                    v7.union_set(v17, v16)
                    v8[v7.find_set(v16)] = v16
            return (v12, v11, v10, v9)

        def iter_dfs2():
            v1 = [[] for v2 in range(len(adj))]
            for v3, (v4, v5) in enumerate(a3):
                if 2 * (dist[v4] - dist[lca[v3]]) >= result[v3]:
                    v1[v4].append((v3, 0))
                else:
                    v1[v5].append((v3, 1))
            v6 = [0] * len(a3)
            v7 = []
            v8 = [(1, (0,))]
            while v8:
                v9, v10 = v8.pop()
                if v9 == 1:
                    v4 = v10[0]
                    v7.append(v4)
                    for v3, v11 in v1[v4]:
                        v12 = depth[v4] - depth[lca[v3]]
                        if v11 == 0:
                            v13 = f3(0, v12, lambda x: 2 * (dist[v4] - dist[v7[-(x + 1)]]) >= result[v3])
                            v6[v3] = v7[-(v13 + 1)]
                        else:
                            v14 = dist[a3[v3][0]] - dist[lca[v3]]
                            v13 = f3(0, v12 - 1, lambda x: 2 * (v14 + (dist[v7[-(v12 - 1 + 1) + x]] - dist[lca[v3]])) >= result[v3])
                            v6[v3] = v7[-(v12 - 1 + 1) + v13]
                    v8.append((3, None))
                    v8.append((2, (v4, 0)))
                elif v9 == 2:
                    v4, v3 = v10
                    if v3 == len(adj[v4]):
                        continue
                    v5, v15 = adj[v4][v3]
                    v8.append((2, (v4, v3 + 1)))
                    if len(v7) >= 2 and v7[-2] == v5:
                        continue
                    dist[v5] = dist[v4] + v15
                    depth[v5] = depth[v4] + 1
                    v8.append((1, (v5, v4)))
                elif v9 == 3:
                    v7.pop()
            return v6
        v1 = [[] for v2 in range(len(a2) + 1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6, v7, v8, v9 = iter_dfs()
        return iter_dfs2()

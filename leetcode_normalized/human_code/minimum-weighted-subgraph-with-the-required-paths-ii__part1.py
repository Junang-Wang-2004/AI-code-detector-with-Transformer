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

class C2(object):

    def minimumWeight(self, a1, a2):
        """
        """

        def iter_dfs():
            v1 = [False] * len(adj)
            v2 = [[] for v3 in range(len(adj))]
            for v4, v5 in enumerate(a2):
                for v6 in v5:
                    v2[v6].append(v4)
            v7 = C1(len(adj))
            v8 = list(range(len(adj)))
            v9 = [0] * len(adj)
            v10 = [0] * len(a2)
            v11 = [(1, (0,))]
            while v11:
                v12, v13 = v11.pop()
                if v12 == 1:
                    v14 = v13[0]
                    for v4 in v2[v14]:
                        v10[v4] += v9[v14]
                        for v6 in a2[v4]:
                            if v1[v6]:
                                v10[v4] -= v9[v8[v7.find_set(v6)]]
                    v1[v14] = True
                    v11.append((2, (v14, 0)))
                elif v12 == 2:
                    v14, v4 = v13
                    if v4 == len(adj[v14]):
                        continue
                    v15, v16 = adj[v14][v4]
                    v11.append((2, (v14, v4 + 1)))
                    if v1[v15]:
                        continue
                    v9[v15] = v9[v14] + v16
                    v11.append((3, (v15, v14)))
                    v11.append((1, (v15, v14)))
                elif v12 == 3:
                    v15, v14 = v13
                    v7.union_set(v15, v14)
                    v8[v7.find_set(v14)] = v14
            return v10
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4, v5 in a1:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        return iter_dfs()

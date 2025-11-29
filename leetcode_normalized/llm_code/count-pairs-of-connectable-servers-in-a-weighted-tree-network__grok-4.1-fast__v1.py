class C1:

    def countPairsOfConnectableServers(self, a1, a2):
        v1 = len(a1) + 1
        v2 = [[] for v3 in range(v1)]
        for v4, v5, v6 in a1:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = [0] * v1

        def subtree_goods(a1, a2, a3):
            v1 = int(a3 % a2 == 0)
            for v2, v3 in v2[a1]:
                if v2 != a2:
                    v1 += subtree_goods(v2, a1, a3 + v3)
            return v1
        for v8 in range(v1):
            v9 = [subtree_goods(nei, v8, w) for v10, v11 in v2[v8]]
            v7[v8] = sum((v9[i] * sum(v9[:i]) for v12 in range(len(v9))))
        return v7

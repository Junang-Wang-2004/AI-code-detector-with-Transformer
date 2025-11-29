import collections

class C1:

    def minChanges(self, a1, a2):
        v1 = len(a1)
        v2 = [collections.Counter() for v3 in range(a2)]
        for v4, v5 in enumerate(a1):
            v2[v4 % a2][v5] += 1
        v6 = [max(g.values() or [0]) for v7 in v2]
        v8 = sum(v6) - min(v6)
        v9 = v1 - v8
        v10 = {0: 0}
        for v11 in v2:
            v12 = collections.defaultdict(int)
            for v13, v14 in v10.items():
                for v15, v16 in v11.items():
                    v17 = v13 ^ v15
                    v12[v17] = max(v12[v17], v14 + v16)
            v10 = v12
        v18 = v10.get(0, 0)
        v19 = v1 - v18
        return min(v9, v19)

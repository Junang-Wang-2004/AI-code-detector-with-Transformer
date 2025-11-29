import collections
v1 = float('inf')

class C1(object):

    def minimumCost(self, a1, a2, a3, a4, a5):
        v1 = len(a1)
        v2 = collections.defaultdict(dict)
        v3 = collections.defaultdict(set)
        v4 = set()
        v5 = len(a3)
        for v6 in range(v5):
            v7 = len(a3[v6])
            v4.add(v7)
            v3[v7].add(a3[v6])
            v3[v7].add(a4[v6])
        v8 = {}
        for v7, v9 in v3.items():
            v10 = sorted(v9)
            v11 = len(v10)
            v12 = {s: idx for v13, v14 in enumerate(v10)}
            v2[v7] = v12
            v15 = [[v1] * v11 for v16 in range(v11)]
            for v17 in range(v11):
                v15[v17][v17] = 0
            v8[v7] = v15
        for v6 in range(v5):
            v7 = len(a3[v6])
            v18 = v2[v7][a3[v6]]
            v19 = v2[v7][a4[v6]]
            v8[v7][v18][v19] = min(v8[v7][v18][v19], a5[v6])

        def floyd_warshall(a1):
            v1 = len(a1)
            for v2 in range(v1):
                for v3 in range(v1):
                    for v4 in range(v1):
                        a1[v3][v4] = min(a1[v3][v4], a1[v3][v2] + a1[v2][v4])
        for v7 in v8:
            floyd_warshall(v8[v7])
        v20 = [v1] * (v1 + 1)
        v20[0] = 0
        for v6 in range(v1):
            if v20[v6] == v1:
                continue
            if a1[v6] == a2[v6]:
                v20[v6 + 1] = min(v20[v6 + 1], v20[v6])
            for v7 in v4:
                if v6 + v7 > v1:
                    continue
                v21 = a1[v6:v6 + v7]
                v22 = a2[v6:v6 + v7]
                if v21 in v2[v7] and v22 in v2[v7]:
                    v18 = v2[v7][v21]
                    v19 = v2[v7][v22]
                    v23 = v8[v7][v18][v19]
                    if v23 < v1:
                        v20[v6 + v7] = min(v20[v6 + v7], v20[v6] + v23)
        return v20[v1] if v20[v1] < v1 else -1

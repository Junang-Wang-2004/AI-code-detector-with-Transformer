import collections

class C1:

    def invalidTransactions(self, a1):
        v1, v2 = (1000, 60)
        v3 = [(x[0], int(x[1]), int(x[2]), x[3]) for v4 in (transaction.split(',') for v5 in a1)]
        v3.sort(key=lambda t: t[1])
        v6 = collections.defaultdict(list)
        for v7, v8 in enumerate(v3):
            v6[v8[0]].append(v7)
        v9 = []
        for v10, v11 in v6.items():
            v12, v13 = (0, 0)
            for v7, v14 in enumerate(v11):
                v8 = v3[v14]
                if v8[2] > v1:
                    v9.append('{},{},{},{}'.format(*v8))
                    continue
                while v12 + 1 < len(v11) and v3[v11[v12]][1] < v8[1] - v2:
                    v12 += 1
                while v13 + 1 < len(v11) and v3[v11[v13 + 1]][1] <= v8[1] + v2:
                    v13 += 1
                for v7 in range(v12, v13 + 1):
                    if v3[v11[v7]][3] != v8[3]:
                        v9.append('{},{},{},{}'.format(*v8))
                        break
        return v9

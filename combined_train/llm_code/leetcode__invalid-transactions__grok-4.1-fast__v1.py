from collections import defaultdict

class C1:

    def invalidTransactions(self, a1):
        v1 = 1000
        v2 = 60
        v3 = defaultdict(list)
        for v4 in a1:
            v5, v6, v7, v8 = v4.split(',')
            v9 = int(v6)
            v10 = int(v7)
            v3[v5].append((v9, v10, v8))
        v11 = []
        for v5, v12 in v3.items():
            v12.sort(key=lambda x: x[0])
            v13 = len(v12)
            v14 = 0
            v15 = 0
            for v16 in range(v13):
                v17, v18, v19 = v12[v16]
                if v18 > v1:
                    v11.append(f'{v5},{v17},{v18},{v19}')
                    continue
                while v14 < v13 and v12[v14][0] < v17 - v2:
                    v14 += 1
                while v15 < v13 and v12[v15][0] <= v17 + v2:
                    v15 += 1
                v20 = any((v12[j][2] != v19 for v21 in range(v14, v15)))
                if v20:
                    v11.append(f'{v5},{v17},{v18},{v19}')
        return v11

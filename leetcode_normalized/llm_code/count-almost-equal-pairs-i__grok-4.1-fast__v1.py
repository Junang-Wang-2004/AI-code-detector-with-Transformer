import collections

class C1:

    def countPairs(self, a1):
        v1 = collections.Counter(a1)
        v2 = sum((v * (v - 1) // 2 for v3 in v1.values()))
        for v4, v5 in v1.items():
            v6 = f'{v4:07d}'
            v7 = [int(ch) for v8 in v6]
            for v9 in range(7):
                for v10 in range(v9 + 1, 7):
                    if v7[v9] == v7[v10]:
                        continue
                    v11 = v7[:]
                    v11[v9], v11[v10] = (v11[v10], v11[v9])
                    v12 = int(''.join(map(str, v11)))
                    if v12 > v4:
                        v2 += v5 * v1[v12]
        return v2

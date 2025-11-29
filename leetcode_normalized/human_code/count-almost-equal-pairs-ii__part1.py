import collections

class C1(object):

    def countPairs(self, a1):
        """
        """
        v1 = 7
        v2 = [0] * v1
        v2[0] = 1
        for v3 in range(v1 - 1):
            v2[v3 + 1] = v2[v3] * 10
        v4 = collections.Counter(a1)
        v5 = collections.defaultdict(list)
        v6 = list(v4.items())
        for v7 in range(len(v6)):
            v5[v6[v7][0]].append(v7)
            for v3 in range(v1):
                v8 = v6[v7][0] // v2[v3] % 10
                for v9 in range(v3 + 1, v1):
                    v10 = v6[v7][0] // v2[v9] % 10
                    if v8 == v10:
                        continue
                    v5[v6[v7][0] - v8 * (v2[v3] - v2[v9]) + v10 * (v2[v3] - v2[v9])].append(v7)
        v11 = sum((v * (v - 1) // 2 for v12 in v4.values()))
        v13 = set()
        for v14 in v5.keys():
            for v3 in range(len(v5[v14])):
                v15 = v6[v5[v14][v3]][1]
                for v9 in range(v3 + 1, len(v5[v14])):
                    v16 = v6[v5[v14][v9]][1]
                    if (v5[v14][v3], v5[v14][v9]) in v13:
                        continue
                    v13.add((v5[v14][v3], v5[v14][v9]))
                    v11 += v15 * v16
        return v11

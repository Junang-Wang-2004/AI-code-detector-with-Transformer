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
        v5 = collections.Counter()
        for v6, v7 in v4.items():
            for v3 in range(v1):
                v8 = v6 // v2[v3] % 10
                for v9 in range(v3 + 1, v1):
                    v10 = v6 // v2[v9] % 10
                    if v8 == v10 or v6 - v8 * (v2[v3] - v2[v9]) + v10 * (v2[v3] - v2[v9]) not in v4:
                        continue
                    v5[v6 - v8 * (v2[v3] - v2[v9]) + v10 * (v2[v3] - v2[v9])] += v7
        return sum((v7 * (v7 - 1) // 2 for v7 in v4.values())) + sum((v7 * v5[v6] for v6, v7 in v4.items())) // 2

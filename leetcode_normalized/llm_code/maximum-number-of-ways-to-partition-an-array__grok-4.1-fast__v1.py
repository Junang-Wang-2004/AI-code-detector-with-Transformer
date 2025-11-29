import collections

class C1:

    def waysToPartition(self, a1, a2):
        v1 = len(a1)
        v2 = sum(a1)
        v3 = [0] * (v1 + 1)
        for v4 in range(v1):
            v3[v4 + 1] = v3[v4] + a1[v4]
        v5 = collections.Counter((2 * v3[v4] - v2 for v4 in range(1, v1)))
        v6 = v5[0]
        v7 = collections.Counter()
        for v8 in range(v1):
            v9 = a1[v8]
            v6 = max(v6, v7[a2 - v9] + v5[v9 - a2])
            if v8 < v1 - 1:
                v10 = 2 * v3[v8 + 1] - v2
                v7[v10] += 1
                v5[v10] -= 1
        return v6

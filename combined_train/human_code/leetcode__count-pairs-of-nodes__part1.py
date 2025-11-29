import collections
import itertools

class C1(object):

    def countPairs(self, a1, a2, a3):
        """
        """
        v1 = [0] * (a1 + 1)
        v2 = collections.Counter(((min(n1, n2), max(n1, n2)) for v3, v4 in a2))
        for v5, v6 in a2:
            v1[v5] += 1
            v1[v6] += 1
        v7 = [0] * (2 * (max(v1[1:]) + 1))
        v8 = collections.Counter(v1[1:])
        for v9, v10 in itertools.product(v8, v8):
            if v9 < v10:
                v7[v9 + v10] += v8[v9] * v8[v10]
            elif v9 == v10:
                v7[v9 + v10] += v8[v9] * (v8[v9] - 1) // 2
        for (v9, v10), v11 in v2.items():
            v7[v1[v9] + v1[v10]] -= 1
            v7[v1[v9] + v1[v10] - v11] += 1
        for v9 in reversed(range(len(v7) - 1)):
            v7[v9] += v7[v9 + 1]
        return [v7[q + 1] if q + 1 < len(v7) else 0 for v12 in a3]

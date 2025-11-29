from functools import reduce

class C1(object):

    def maxHappyGroups(self, a1, a2):
        """
        """
        v1 = [0] * a1
        for v2 in a2:
            v1[v2 % len(v1)] += 1
        v3 = v1[0]
        v1[0] = 0
        for v2 in range(1, len(v1) // 2 + 1):
            v4 = min(v1[v2], v1[len(v1) - v2]) if 2 * v2 != len(v1) else v1[v2] // 2
            v3 += v4
            v1[v2] -= v4
            v1[len(v1) - v2] -= v4
        v5 = {v2: c for v2, v6 in enumerate(v1) if v6}
        v7 = reduce(lambda total, c: total * (v6 + 1), iter(v5.values()), 1)
        v8 = [0] * v7
        for v9 in range(len(v8)):
            v10 = 0
            v11, v12 = (v9, 1)
            for v2, v6 in v5.items():
                v13 = v11 % (v6 + 1)
                if v13:
                    v8[v9] = max(v8[v9], v8[v9 - v12])
                v10 = (v10 + v13 * v2) % a1
                v12 *= v6 + 1
                v11 //= v6 + 1
            if v9 != len(v8) - 1 and v10 == 0:
                v8[v9] += 1
        return v3 + v8[-1]

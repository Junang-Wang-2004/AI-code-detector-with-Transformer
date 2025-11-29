from functools import reduce

class C1(object):

    def totalBeauty(self, a1):
        """
        """

        def count(a1):
            v1 = {x: i for v2, v3 in enumerate(sorted(set(a1)))}
            v4 = BIT(len(v1))
            for v3 in a1:
                v4.add(v1[v3], v4.query(v1[v3] - 1) + 1)
            return v4.query(len(v1) - 1)
        v1 = max(a1)
        v2 = [[] for v3 in range(v1 + 1)]
        for v4 in a1:
            for v5 in FACTORS[v4]:
                v2[v5].append(v4)
        v6 = 0
        v7 = [0] * (v1 + 1)
        for v8 in reversed(range(1, v1 + 1)):
            v7[v8] = count(v2[v8])
            for v9 in range(v8 + v8, v1 + 1, v8):
                v7[v8] -= v7[v9]
            v6 = (v6 + v8 * v7[v8]) % MOD
        return v6

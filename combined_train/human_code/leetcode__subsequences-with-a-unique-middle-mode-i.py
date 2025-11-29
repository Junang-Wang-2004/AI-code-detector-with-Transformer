import collections

class C1(object):

    def subsequencesWithMiddleMode(self, a1):
        """
        """

        def nC2(a1):
            return a1 * (a1 - 1) // 2
        v1 = 10 ** 9 + 7
        v2 = 0
        v3 = collections.defaultdict(int)
        v4 = collections.defaultdict(int)
        for v5 in a1:
            v4[v5] += 1
        v6 = 0
        v7 = sum((v ** 2 for v8 in v4.values()))
        v9 = 0
        v10 = 0
        v11 = 0
        for v12, v8 in enumerate(a1):
            v6 -= v3[v8] ** 2
            v7 -= v4[v8] ** 2
            v9 -= v3[v8] * v4[v8]
            v10 -= v3[v8] ** 2 * v4[v8]
            v11 -= v3[v8] * v4[v8] ** 2
            v4[v8] -= 1
            v13, v14 = (v12, len(a1) - (v12 + 1))
            v2 += nC2(v13) * nC2(v14)
            v2 -= nC2(v13 - v3[v8]) * nC2(v14 - v4[v8])
            v2 -= ((v6 - (v13 - v3[v8])) * (v14 - v4[v8]) - (v10 - v9)) * v4[v8] // 2
            v2 -= ((v7 - (v14 - v4[v8])) * (v13 - v3[v8]) - (v11 - v9)) * v3[v8] // 2
            v2 -= v3[v8] * v9 * (v14 - v4[v8]) - v3[v8] * v11
            v2 -= v4[v8] * v9 * (v13 - v3[v8]) - v4[v8] * v10
            v2 -= v4[v8] * (v10 - v9) // 2
            v2 -= v3[v8] * (v11 - v9) // 2
            v3[v8] += 1
            v6 += v3[v8] ** 2
            v7 += v4[v8] ** 2
            v9 += v3[v8] * v4[v8]
            v10 += v3[v8] ** 2 * v4[v8]
            v11 += v3[v8] * v4[v8] ** 2
        return v2 % v1

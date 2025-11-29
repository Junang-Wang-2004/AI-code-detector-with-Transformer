from collections import Counter

class C1:

    def maxEqualFreq(self, a1):
        v1 = Counter()
        v2 = Counter()
        v3 = 0
        v4 = len(a1)
        for v5 in range(1, v4 + 1):
            v6 = a1[v5 - 1]
            v7 = v1[v6]
            if v7 > 0:
                v2[v7] -= 1
            v1[v6] += 1
            v8 = v1[v6]
            v2[v8] += 1
            v9 = False
            if len(v2) == 1:
                v9 = True
            elif len(v2) == 2:
                v10 = sorted(v2)
                v11, v12 = (v10[0], v10[1])
                if v2[v12] == 1 and v12 == v11 + 1:
                    v9 = True
                elif v11 == 1 and v2[1] == 1:
                    v9 = True
            if v9:
                v3 = v5
        return v3

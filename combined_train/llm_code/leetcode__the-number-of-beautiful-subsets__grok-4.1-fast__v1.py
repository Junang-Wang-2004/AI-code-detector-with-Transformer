from collections import Counter

class C1:

    def beautifulSubsets(self, a1, a2):
        v1 = Counter(a1)
        v2 = 1
        v3 = set()
        for v4 in list(v1):
            if v4 - a2 in v1 or v4 in v3:
                continue
            v5 = []
            v6 = v4
            while v6 in v1:
                v5.append(v1[v6])
                v3.add(v6)
                v6 += a2
            v7 = 1
            v8 = 0
            for v9 in v5:
                v10 = (1 << v9) - 1
                v11 = v7 + v8
                v12 = v7 * v10
                v7 = v11
                v8 = v12
            v2 *= v7 + v8
        return v2 - 1

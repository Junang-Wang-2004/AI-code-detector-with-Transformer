from collections import Counter

class C1:

    def numberOfPairs(self, a1, a2, a3):
        if not a1:
            return 0
        v1 = max(a1) + 1
        v2 = [0] * v1
        v3 = Counter(a2)
        for v4, v5 in v3.items():
            v6 = a3 * v4
            v7 = v6
            while v7 < v1:
                v2[v7] += v5
                v7 += v6
        return sum((v2[val] for v8 in a1))

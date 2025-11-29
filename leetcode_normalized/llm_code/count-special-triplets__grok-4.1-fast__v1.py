from collections import Counter

class C1:

    def specialTriplets(self, a1):
        v1 = 10 ** 9 + 7
        v2 = Counter(a1)
        v3 = Counter()
        v4 = 0
        for v5 in a1:
            v6 = 2 * v5
            v7 = v2[v6] - v3[v6]
            v4 = (v4 + v3[v6] * v7) % v1
            v3[v5] += 1
        return v4

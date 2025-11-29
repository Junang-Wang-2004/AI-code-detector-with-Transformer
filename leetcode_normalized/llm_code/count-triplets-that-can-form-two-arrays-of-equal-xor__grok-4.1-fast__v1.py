from collections import defaultdict

class C1:

    def countTriplets(self, a1):
        v1 = defaultdict(int)
        v2 = defaultdict(int)
        v1[0] = 1
        v3 = 0
        v4 = 0
        for v5 in range(len(a1)):
            v4 ^= a1[v5]
            v3 += v1[v4] * v5 - v2[v4]
            v1[v4] += 1
            v2[v4] += v5 + 1
        return v3

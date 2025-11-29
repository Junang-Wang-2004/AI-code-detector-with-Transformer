from collections import Counter

class C1(object):

    def maximumSubarraySum(self, a1, a2):
        v1 = len(a1)
        if v1 < a2:
            return 0
        v2 = Counter()
        v3 = 0
        v4 = 0
        for v5 in range(a2):
            v2[a1[v5]] += 1
            v3 += a1[v5]
        if len(v2) == a2:
            v4 = v3
        for v5 in range(a2, v1):
            v6 = a1[v5 - a2]
            v2[v6] -= 1
            if v2[v6] == 0:
                del v2[v6]
            v3 -= v6
            v7 = a1[v5]
            v2[v7] += 1
            v3 += v7
            if len(v2) == a2:
                v4 = max(v4, v3)
        return v4
